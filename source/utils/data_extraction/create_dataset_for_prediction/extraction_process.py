import pandas as pd
import numpy as np

from source.utils.consts.assistment_consts import Questionnaires
from source.utils.data_extraction.create_dataset_for_prediction.handle_groups import GROUPS, fill_group,\
    GROUP_NAMES_MAP, rename_groups, fill_missing_groups
from source.utils.data_extraction.create_dataset_for_prediction.pipeline_functions import SelectedQuestionnaires, \
    do_questionnaires_imputations, save_df, split_to_multiple_measurement_times, compute_questions_scores
from source.utils.consts.pathology_variables import pathology_variables_times
from source.utils.target_variable import TargetVariable
import os


class ExtractionProcess:
    def __init__(self, input_parameters):
        self.parameters = input_parameters

        self.columns = None
        self.df = None

    def run(self):

        self.df = pd.read_csv(self.parameters.df_path, na_values='chameleon_ideation_stu_2022', keep_default_na=True)
        self._init_columns()
        self._assign_groups()

        if self.parameters.impute_from_parallel_questionnaires:
            self._impute_from_parallel_questionnaires()

        self._split_to_times()

        if self.parameters.compute_target_variable:
            self._compute_target_variables()

        if self.parameters.calculate_questionnaires_scores:
            self._calculate_questionnaires_scores()

    def _init_columns(self):
        self.columns = SelectedQuestionnaires(questionnaires=self.parameters.questionnaires)

        self.columns.add(['sciafca_timestamp'])

    def _assign_groups(self):
        df = self.df.copy()
        df = rename_groups(df, GROUP_NAMES_MAP)
        self.df = fill_missing_groups(df, GROUP_NAMES_MAP)
        self.columns.add(['group'])

    def _impute_from_parallel_questionnaires(self):
        df = self.df.copy()
        self.df = do_questionnaires_imputations(df)

    def _compute_target_variables(self):
        # Compute target variables based on measurement times
        for time in self.parameters.measurement_times:
            print(f"Computing target variables for {time}")
        pass

    def _calculate_questionnaires_scores(self):
        # Logic to calculate scores
        pass

    def _split_to_times(self):
        n_times = len(self.parameters.measurement_times)
        if n_times > 1:
            df_time1, df_time2 = split_to_multiple_measurement_times(df, columns, times)
            columns.add(['measurement'])


def main(times, directory_path=None, suffix=''):
    # Change the current directory to the source root

    df = pd.read_csv(r"C:\Users\nogur\Documents\DeppClinic\Data\postgres_db\merged_data\merged_2021_and_2022.csv",
                     na_values='chameleon_ideation_stu_2022', keep_default_na=True)

    columns = SelectedQuestionnaires()
    df = do_questionnaires_imputations(df)

    # handle groups
    for group in GROUPS:
        df = fill_group(df, group)

    df = rename_groups(df, GROUP_NAMES_MAP)
    df = fill_missing_groups(df, GROUP_NAMES_MAP)
    columns.add(['group'])

    columns.add(['sciafca_timestamp'])
    df_time1, df_time2 = split_to_multiple_measurement_times(df, columns, times)
    columns.add(['measurement'])
    #
    # # calculate pathology variables
    # for questionnaire_name, items in pathology_variables_times['intake'].items():
    #     tv = TargetVariable(questionnaire_name, {'measurement': 'time1'}, items)
    #     df_time1 = tv.calculate_value(df_time1)
    #     columns.add([questionnaire_name])
    #
    # for questionnaire_name, items in pathology_variables_times['time2'].items():
    #     tv = TargetVariable(questionnaire_name, {'measurement': 'time2'}, items)
    #     df_time2 = tv.calculate_value(df_time2)
    #     columns.add([questionnaire_name])

    df = pd.concat([df_time1, df_time2])
    df = df[list(columns.unique_columns_with_id)]

    questionnaires = Questionnaires().questionnaires
    df, columns = compute_questions_scores(df, questionnaires, columns)

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    save_df(df, columns, axis='patient', profile=False, directory_path=directory_path, suffix=suffix)
    #save_df(df, columns, axis='time', profile=False, directory_path=directory_path, suffix=suffix)

main(treatment_times, r"C:\Users\nogur\Documents\DeppClinic\Data\processed_data\only_final_scores", '_treatment')
main(control_times, r"C:\Users\nogur\Documents\DeppClinic\Data\processed_data\only_final_scores", '_control')
main(all_times, r"C:\Users\nogur\Documents\DeppClinic\Data\processed_data\only_final_scores")


