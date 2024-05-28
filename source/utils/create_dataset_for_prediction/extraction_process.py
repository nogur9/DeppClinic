import pandas as pd
from source.utils.classes.export_columns_manager import ExportColumnsManager
from source.utils.consts.assistment_consts import Questionnaires
from source.utils.create_dataset_for_prediction.impute import QuestionnaireImputer
from source.utils.create_dataset_for_prediction.pipeline_functions import compute_questions_scores, \
    split_to_multiple_measurement_times
from source.utils.handle_groups import GroupManager
from source.utils.consts.pathology_variables import pathology_variables_times
from source.utils.classes.target_variable import TargetVariable
import os

from source.utils.save_processed_data import save_df


class ExtractionProcess:
    def __init__(self, input_parameters):
        self.parameters = input_parameters
        self.are_repeated_measures = len(self.parameters.measurement_times) > 1
        self.content_root = self.parameters.content_root
        self.export_columns_manager = None
        self.df = None
        self.intake = None
        self.df_time2 = None

    def run(self):
        df_path = os.path.join(self.content_root, self.parameters.df_path)
        self.df = pd.read_csv(df_path, na_values=self.parameters.custom_na_values, keep_default_na=True)
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
        group_manager = GroupManager(self.df, self.content_root)
        group_manager.process()
        self.df = group_manager.df
        self.export_columns_manager.add_columns(['group'])

    def _impute_from_parallel_questionnaires(self):
        df = self.df.copy()
        questionnaire_imputer = QuestionnaireImputer(df)
        self.df = questionnaire_imputer.do_questionnaires_imputations()

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
        self.export_columns_manager.add_columns([questionnaire_name])
        df = tv.calculate_value(df)
        return df

    def _calculate_questionnaires_scores(self):
        questionnaires = Questionnaires().questionnaires
        self.df, self.variables_to_export = compute_questions_scores(self.df,
                                                                     questionnaires,
                                                                     self.export_columns_manager)

    def _split_to_times(self):
        if self.are_repeated_measures:
            self.intake, self.df_time2 = split_to_multiple_measurement_times(
                                            self.df,
                                            self.export_columns_manager,
                                            self.parameters.measurement_times)
            self.export_columns_manager.add_columns(['measurement'])

        else:
            self.intake = self.df.copy()

    def _merge_times(self):
        df = pd.concat([self.intake, self.df_time2])
        self.df = df

    def _save_data(self):
        if not os.path.exists(self.parameters.directory_path):
            os.makedirs(self.parameters.directory_path)

        save_df(self.df, self.export_columns_manager, axis='patient', directory_path=self.parameters.directory_path)
        # save_df(df, columns, axis='time', profile=False, directory_path=directory_path, suffix=suffix)


