import numpy as np
from source.utils.consts.assistment_consts import Questionnaires


class QuestionnaireImputer:

    questionnaire_imputation_map = [
        # if the 'origin' is missing, impute the missing data from the 'replacement'
        {'primary_questionnaire': 'scs_clin', 'backup_questionnaire': 'scs_stu'},
        {'primary_questionnaire': 'c_ssrs_clin', 'backup_questionnaire': 'c_ssrs_stu'},
        {'primary_questionnaire': 'demographics_m', 'backup_questionnaire': 'demographics_f'},
        {'primary_questionnaire': 'sci_mother', 'backup_questionnaire': 'sci_father'},
        {'primary_questionnaire': 'dass_m', 'backup_questionnaire': 'dass_f'},
        {'primary_questionnaire': 'ecr_m', 'backup_questionnaire': 'ecr_f'},
        {'primary_questionnaire': 'swan_m', 'backup_questionnaire': 'swan_f'},
        {'primary_questionnaire': 'ARI_P_m', 'backup_questionnaire': 'ARI_P_f'}
    ]

    def __init__(self, df):
        self.df = df.copy()
        self.questionnaires = Questionnaires().questionnaires

    def do_questionnaires_imputations(self):
        for questionnaire_imputation in self.questionnaire_imputation_map:
            try:
                self._impute_from_questionnaire(questionnaire_imputation['primary_questionnaire'],
                                                questionnaire_imputation['backup_questionnaire'])
            except KeyError:
                pass
        return self.df

    def _impute_from_questionnaire(self, primary_questionnaire, backup_questionnaire):
        questionnaire_columns = self.questionnaires[primary_questionnaire]['columns']
        replace_columns = self.questionnaires[backup_questionnaire]['columns']
        is_empty = self.df[primary_questionnaire].isna().all(axis=1)
        self._impute_columns(questionnaire_columns, replace_columns, is_empty)

    def _impute_columns(self, primary_questionnaire, backup_questionnaire, is_empty):
        for questionnaire_column, replace_column in zip(primary_questionnaire, backup_questionnaire):
            self.df[questionnaire_column] = np.where(is_empty, self.df[replace_column], self.df[questionnaire_column])

