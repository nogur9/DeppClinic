import numpy as np
import pandas as pd
from utils.consts.assistment_consts import questionnaires


def impute_mean_questionnaire_score(df, questionnaire_name):
    """


    """
    if "reverse_questions" in questionnaires[questionnaires].keys():
        # later_ToDo - implement
        pass

    df[impute_to] = np.where(df[impute_to].isnull(), df[impute_from], df[impute_to])

    return df


def impute_from_column(df, impute_to, impute_from):
    """
    test:
    df[(df['c_ssrs_6'].isna()) & (~df['c_ssrs_last_visit_6'].isna())][['c_ssrs_6', 'c_ssrs_last_visit_6']]
    df = impute_from_column(df, impute_to = 'c_ssrs_6', impute_from = 'c_ssrs_last_visit_6')
    df[(df['c_ssrs_6'].isna()) & (~df['c_ssrs_last_visit_6'].isna())][['c_ssrs_6', 'c_ssrs_last_visit_6']]

    """
    df[impute_to] = np.where(df[impute_to].isnull(), df[impute_from], df[impute_to])

    return df