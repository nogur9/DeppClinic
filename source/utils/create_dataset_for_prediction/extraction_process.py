import pandas as pd

from source.utils.classes.export_columns_manager import ExportColumnsManager
from source.utils.consts.assistment_consts import Questionnaires
from source.utils.create_dataset_for_prediction.handle_groups import GROUP_NAMES_MAP, create_decode_group_column, \
    impute_missing_groups_data, GroupManager
from source.utils.create_dataset_for_prediction.pipeline_functions import VariablesToExport, \
    do_questionnaires_imputations, save_df, split_to_multiple_measurement_times, compute_questions_scores
from source.utils.consts.pathology_variables import pathology_variables_times
from source.utils.classes.target_variable import TargetVariable
import os


class ExtractionProcess:
    def __init__(self, input_parameters):
        self.parameters = input_parameters
        self.are_repeated_measures = len(self.parameters.measurement_times) > 1

        self.export_columns_manager = None
        self.df = None
        self.intake = None
        self.df_time2 = None

    def run(self):
        self.df = pd.read_csv(self.parameters.df_path, na_values=self.parameters.custom_na_values,
                              keep_default_na=True)
        self.export_columns_manager = ExportColumnsManager(questionnaires=self.parameters.questionnaires)

        self._manage_groups()

        if self.parameters.impute_from_parallel_questionnaires:
            self._impute_from_parallel_questionnaires()

        if self.parameters.compute_target_variable:
            self._compute_all_target_variables()

        if self.parameters.calculate_questionnaires_scores:
            self._calculate_questionnaires_scores()

        self._save_data()

    def _manage_groups(self):
        group_manager = GroupManager(self.df)
        group_manager.process()
        self.df = group_manager.df
        self.export_columns_manager.add(['group'])

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
        self.df, self.variables_to_export = compute_questions_scores(self.df, questionnaires, self.variables_to_export)

    def _split_to_times(self):
        if self.are_repeated_measures:
            self.intake, self.df_time2 = split_to_multiple_measurement_times(self.df, self.variables_to_export,
                                                                             self.parameters.measurement_times)
            self.variables_to_export.add(['measurement'])

        else:
            self.intake = self.df.copy()

    def _merge_times(self):
        df = pd.concat([self.intake, self.df_time2])
        df = df[list(self.variables_to_export.unique_columns_with_id)]
        self.df = df

    def _save_data(self):
        if not os.path.exists(self.parameters.directory_path):
            os.makedirs(self.parameters.directory_path)

        save_df(self.df, self.variables_to_export, axis='patient', directory_path= self.parameters.directory_path)
        # save_df(df, columns, axis='time', profile=False, directory_path=directory_path, suffix=suffix)


