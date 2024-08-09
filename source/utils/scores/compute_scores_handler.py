from source.utils.questionnaire.questionnaires_map import QuestionnairesMap
from source.utils.utils.export_columns_manager import ExportColumnsManager


class ComputeScoresHandler:
    def __init__(self, questionnaires_map: QuestionnairesMap):
        self.questionnaires_map = questionnaires_map

    def compute_questionnaires_scores(self, df, export_columns_manager: ExportColumnsManager):
        for name, questionnaire in self.questionnaires_map.questionnaires.items():
            df, score_columns = questionnaire.compute_scores(df)
            export_columns_manager.add_columns(score_columns)
        return df, export_columns_manager

