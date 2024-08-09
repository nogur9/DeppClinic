import pandas as pd
import numpy as np

from source.utils.consts.standard_names import TIMESTAMP_COLUMN_NAME


class TimestampCreator:
    """
    this happening before splitting into measurement times
    """
    INTAKE_TIMESTAMPS = ['opening_timestamp', 'mfq_short_timestamp', 'complaint_date']

    FOLLOWUP_TIMESTAMPS = ['sciafca_timestamp', 'mfq_short_timestamp', 'chameleon_timestamp',
                    'chameleon_suicide_er_date_stu', 'chameleon_psychiatric_date_stu',
                    'opening_child_pre_timestamp', 'cssrs_timestamp', 'siq_timestamp']

    def __init__(self, timestamp_column=TIMESTAMP_COLUMN_NAME):
        self.timestamp_column = timestamp_column

    def get(self, df: pd.DataFrame):
        pass

    @staticmethod
    def convert_datetime(date_str):
        try:
            return pd.to_datetime(date_str)
        except ValueError:
            try:
                return pd.to_datetime(int(date_str))
            except ValueError:
                try:
                    return pd.to_datetime(date_str.split(" ")[0], errors='coerce')

                except AttributeError:
                    return pd.NaT

    @staticmethod
    def parse_datetime(date_str):
        try:
            return pd.to_datetime(date_str)
        except ValueError:
            try:
                return pd.to_datetime(date_str.split(" ")[0], errors='coerce')

            except AttributeError:
                return pd.NaT

    def impute(self, questionnaire_columns, replace_columns, df, multiple_options=False):

        is_empty = df[questionnaire_columns].isna().all(axis=1)

        for questionnaire_column, replace_column in zip(questionnaire_columns, replace_columns):
            df[questionnaire_column] = np.where(np.array(is_empty), df[replace_column], df[questionnaire_column])
            if multiple_options:
                is_empty = df[questionnaire_columns].isna().all(axis=1)

        return df

