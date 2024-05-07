import pandas as pd
import numpy as np

from source.utils.consts.assistment_consts import Questionnaires
from source.utils.data_extraction.create_dataset_for_prediction.handle_groups import GROUPS, fill_group,\
    GROUP_NAMES_MAP, rename_groups, fill_missing_groups
from source.utils.data_extraction.create_dataset_for_prediction.pipeline_functions import VariablesToExport, \
    do_questionnaires_imputations, save_df, split_to_multiple_measurement_times, compute_questions_scores
from source.utils.consts.pathology_variables import pathology_variables_times
from source.utils.target_variable import TargetVariable
import os


class ExtractionProcess:
    def __init__(self, input_parameters):
        self.parameters = input_parameters
        self.are_repeated_measures = len(self.parameters.measurement_times) > 1

        self.variables_to_export = None
        self.df = None
        self.intake = None
        self.df_time2 = None


    def run(self):

        self.df = pd.read_csv(self.parameters.df_path, na_values='chameleon_ideation_stu_2022', keep_default_na=True)
        self._init_columns()
        self._assign_groups()

        if self.parameters.impute_from_parallel_questionnaires:
            self._impute_from_parallel_questionnaires()

        if self.parameters.compute_target_variable:
            self._compute_all_target_variables()

        if self.parameters.calculate_questionnaires_scores:
            self._calculate_questionnaires_scores()

        self._save_data()

    def _init_columns(self):
        self.variables_to_export = VariablesToExport(questionnaires=self.parameters.questionnaires)

        self.variables_to_export.add(['sciafca_timestamp'])

    def _assign_groups(self):
        df = self.df.copy()
        df = rename_groups(df, GROUP_NAMES_MAP)
        self.df = fill_missing_groups(df, GROUP_NAMES_MAP)
        self.variables_to_export.add(['group'])

    def _impute_from_parallel_questionnaires(self):
        df = self.df.copy()
        self.df = do_questionnaires_imputations(df)

    def _compute_all_target_variables(self):
        self._split_to_times()

        for questionnaire_name, questions in pathology_variables_times['intake'].items():
            self.intake = self._compute_single_target_variable(questionnaire_name, questions, self.intake)

        if self.are_repeated_measures > 1:
            for questionnaire_name, questions in pathology_variables_times['time2'].items():
                self._compute_single_target_variable(questionnaire_name, questions, self.df_time2)

        self._merge_times()

    def _compute_single_target_variable(self, questionnaire_name, questions, df):
        df = df.copy()
        tv = TargetVariable(questionnaire_name, questions)
        self.variables_to_export.add([questionnaire_name])
        df = tv.calculate_value(df)
        return df

    def _calculate_questionnaires_scores(self):
        questionnaires = Questionnaires().questionnaires
        df, columns = compute_questions_scores(self.df, questionnaires, self.variables_to_export)

    def _split_to_times(self):
        if self.are_repeated_measures > 1:
            self.intake, self.df_time2 = split_to_multiple_measurement_times(self.df, self.variables_to_export, self.parameters.measurement_times)
            self.variables_to_export.add(['measurement'])
        else:
            self.intake = self.df.copy()

    def _merge_times(self):
        df = pd.concat([self.intake, self.df_time2])
        df = df[list(self.variables_to_export.unique_columns_with_id)]
        self.df = df

    def _save_data(self):
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        save_df(df, columns, axis='patient', profile=False, directory_path=directory_path, suffix=suffix)
        # save_df(df, columns, axis='time', profile=False, directory_path=directory_path, suffix=suffix)


