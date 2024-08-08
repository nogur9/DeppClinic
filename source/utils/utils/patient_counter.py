import pandas as pd
from source.utils.consts.standard_names import ID_COLUMN
import os

class PatientCounter:
    """
    produces a table of:
    measurement_times X
    indicator_questionnaire X
    N-patients

    with the option to calculate how many patients exists in all the measurement times
    """

    def __init__(self, indicator_questionnaires: list, measurement_times: dict, overlapping_counting: bool = False):
        self.indicator_questionnaires = indicator_questionnaires
        self.measurement_times = measurement_times
        self.overlapping_counting = overlapping_counting
        self.count_table = None

    def count(self, df):
        rows = []
        for indicator_questionnaire in self.indicator_questionnaires:

            for time in self.measurement_times.keys():
                row = {"measurement": time, "questionnaire": indicator_questionnaire}
                n_patients = self._count_by_questionnaire_per_measurement_time(df, indicator_questionnaire, time)
                row['N-patients'] = n_patients
                rows.append(row)
            else:
                row = self._calculate_overlapping(df, indicator_questionnaire)
                rows.append(row)

        count_table = pd.DataFrame(rows)
        self.count_table = count_table

    def _count_by_questionnaire_per_measurement_time(self, df: pd.DataFrame,
                                                     indicator_questionnaire: str, time: str):
        df = df.query(f"measurement == '{time}'")
        n_patients = df[~df[f"{indicator_questionnaire}_score"].isna()][ID_COLUMN].nunique()
        return n_patients

    def _calculate_overlapping(self, df: pd.DataFrame, indicator_questionnaire: str):
        row = {"measurement": "all times", "questionnaire": indicator_questionnaire}

        df = df[~df[f"{indicator_questionnaire}_score"].isna()]

        # Pivot the table to get the counts of measurements for each patient
        pivot_df = df.pivot_table(index=ID_COLUMN, columns='measurement', aggfunc='size', fill_value=0)

        # Count the number of patients with all measurements
        n_patients = (pivot_df > 0).all(axis=1).sum()
        row['N-patients'] = n_patients

        return row

    def export(self, directory_path):
        self.count_table.to_csv(os.path.join(directory_path, "descriptive.csv"), index=False)
