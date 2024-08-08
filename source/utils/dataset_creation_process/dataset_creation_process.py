import pandas as pd
from source.utils.classes.export_columns_manager import ExportColumnsManager
from source.utils.consts.standard_names import INTAKE
from source.utils.dataset_creation_process.dataset_creation_input_parameter import InputParameters
from source.utils.dataset_creation.handle_events import group_by_measurment_times
from source.utils.utils.questionnaire_imputer import QuestionnaireImputer
from source.utils.pathology_assessment import PathologiesMap
from source.utils.pathology_assessment import PsychologicalAssessment
from source.utils.utils.patient_counter import PatientCounter
from source.utils.dataset_creation.save_processed_data import save_results
from source.utils.utils.groups_manager import GroupManager
import os

from source.utils.questionnaire.questionnaires_map import QuestionnairesMap
from source.utils.scores.compute_scores_handler import ComputeScoresHandler


class DatasetCreationProcess:
    def __init__(self, input_parameters: InputParameters):
        self.parameters = input_parameters
        self.export_columns_manager = None
        self.df = None
        self._init_params()

    def _init_params(self):
        self.events_names = list(self.parameters.measurement_times.keys())
        self.content_root = self.parameters.content_root
        self.pathologies = [PathologiesMap[i] for i in self.parameters.pathologies]
        self.questionnaires_map = QuestionnairesMap(self.parameters.questionnaires_for_scoring +
                                                    self.parameters.indicator_questionnaires)
        if self.parameters.include_individual_questions:
            self.export_columns_manager = ExportColumnsManager(questionnaires=self.questionnaires_map)
        else:
            self.export_columns_manager = ExportColumnsManager()

    def run(self):
        df_path = os.path.join(self.content_root, self.parameters.df_path)
        self.df = pd.read_csv(df_path, na_values=self.parameters.custom_na_values, keep_default_na=True)

        if self.parameters.include_app_data:
            self._add_app_data()

        self._manage_groups()

        if self.parameters.impute_from_parallel_questionnaires:
            self._impute_from_parallel_questionnaires()

        self._sort_to_measurement_times()

        if self.parameters.compute_target_variable:
            self._compute_pathology_variables()

        if self.parameters.calculate_questionnaires_scores or len(self.parameters.indicator_questionnaires):
            self._calculate_questionnaires_scores()

        if len(self.parameters.indicator_questionnaires):
            self._count_patients()

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
        compute_scores_handler = ComputeScoresHandler(self.questionnaires_map)

        self.df, self.export_columns_manager = compute_scores_handler.compute_questionnaires_scores(
            self.df, self.export_columns_manager)

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

    def _count_patients(self):
        dir_path = self._create_directory(self.content_root, self.parameters.directory_path)
        patient_counter = PatientCounter(self.parameters.indicator_questionnaires,
                                         self.parameters.measurement_times,
                                         self.parameters.overlapping_counting)
        patient_counter.count(self.df)
        patient_counter.export(directory_path=dir_path)

    def _add_app_data(self):
        def used_app(x):
            app_ids = pd.read_csv(r"../../../Data/helper_docs/APP_patient_ids.csv")
            if x['id'] in list(app_ids['patient_id']):
                return True
            else:
                return False

        self.df['did_used_app'] = self.df.apply(used_app, axis=1)
        self.export_columns_manager.add_columns(['did_used_app'], is_info=True)
