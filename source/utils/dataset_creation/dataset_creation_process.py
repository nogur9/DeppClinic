import pandas as pd
from source.utils.classes.export_columns_manager import ExportColumnsManager
from source.utils.consts.assistment_consts import Questionnaires
from source.utils.consts.standard_names import INTAKE
from source.utils.dataset_creation.handle_events import group_by_measurment_times
from source.utils.dataset_creation.impute import QuestionnaireImputer
from source.utils.dataset_creation.pathology_assessment.pathologies_map import PathologiesMap
from source.utils.dataset_creation.pipeline_functions import compute_questions_scores
from source.utils.dataset_creation.pathology_assessment.psychological_assessment import PsychologicalAssessment
from source.utils.dataset_creation.groups import GroupManager
import os

from source.utils.dataset_creation.save_processed_data import save_results


class DatasetCreationProcess:
    def __init__(self, input_parameters):
        self.parameters = input_parameters

        self.events_names = list(self.parameters.measurement_times.keys())
        self.content_root = self.parameters.content_root
        self.pathologies = [PathologiesMap[i] for i in self.parameters.pathologies]

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

        self._sort_to_measurement_times()

        if self.parameters.compute_target_variable:
            self._compute_pathology_variables()

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

    def _compute_pathology_variables(self):
        if any([question.only_intake_evaluation for question in self.pathologies]):
            assert (INTAKE in self.events_names, "expect intake times")
        if any([question.only_follow_up_evaluation for question in self.pathologies]):
            non_intake_events = [event for event in self.events_names if event != INTAKE]
            assert len(non_intake_events) > 0, "expect follow-up times"

        for pathology in self.pathologies:
            self.df = self._compute_single_pathology(pathology, self.df)

    def _compute_single_pathology(self, pathology, df):
        df = df.copy()
        assessment = PsychologicalAssessment(pathology)
        df = assessment.calculate_target_pathology(df)
        self.export_columns_manager.add_columns([pathology.name])

        if self.parameters.add_pathology_missing_ratio:
            self.export_columns_manager.add_columns([f'ratio_of_missing_{pathology.name}_values'])

        return df

    def _calculate_questionnaires_scores(self):
        questionnaires = Questionnaires().questionnaires
        self.df, self.variables_to_export = compute_questions_scores(self.df,
                                                                     questionnaires,
                                                                     self.export_columns_manager)

    def _sort_to_measurement_times(self):
        df = self.df.copy()
        df = group_by_measurment_times(df, self.parameters.measurement_times)
        self.export_columns_manager.add_columns(['measurement'])
        self.df = df

    def _save_data(self):
        dir_path = self._create_directory(self.content_root, self.parameters.directory_path)
        save_results(self.df, self.export_columns_manager, axis='patient', directory_path=dir_path)

    @staticmethod
    def _create_directory(root, path):
        dir_path = os.path.join(root, path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        return dir_path


