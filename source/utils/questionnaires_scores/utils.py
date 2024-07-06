import numpy as np


def impute_mean_questionnaire_score(df, questionnaire_columns, reverse_questions=None):

    if reverse_questions is not None:
        # ToDo - implement
        pass

    def impute_row_with_mean(row):
        mean_value = row.dropna().mean()
        row = row.fillna(mean_value)
        return row

    # Assuming 'df' is your DataFrame and 'columns_name' is the name of the questionnaire columns

    df[questionnaire_columns] = df[questionnaire_columns].apply(impute_row_with_mean, axis=1)

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

