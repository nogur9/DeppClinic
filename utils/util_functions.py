import numpy as np


def impute_from_questionnaire(df, questionnaire_name, replacement_questionnaire):
    from utils.consts.assistment_consts import questionnaires
    questionnaire_columns = questionnaires[questionnaire_name]['columns']
    replace_columns = questionnaires[replacement_questionnaire]['columns']

    is_empty = df[questionnaire_columns].isna().all(axis=1)

    for questionnaire_column, replace_column in zip(questionnaire_columns, replace_columns):
        df[questionnaire_column] = np.where(np.array(is_empty), df[replace_column], df[questionnaire_column])

    return df


def questionnaire_is_empty(df, questionnaire_name, impute_from, impute_to):
    from utils.consts.assistment_consts import questionnaires

    is_empty = df[questionnaires[questionnaire_name]['columns']].isna().all(axis=1)
    np.where(df[questionnaires[questionnaire_name]['columns']].isnull().all(axis=1), df[impute_from], df[impute_to])
    return is_empty


