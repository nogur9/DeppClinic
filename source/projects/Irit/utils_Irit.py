import numpy as np
import warnings
from sklearn.preprocessing import StandardScaler
from Irit.Variables import columns_need_normalization


def impute_from_column(df, impute_to, impute_from):
    """
    test:
    df[(df['c_ssrs_6'].isna()) & (~df['c_ssrs_last_visit_6'].isna())][['c_ssrs_6', 'c_ssrs_last_visit_6']]
    df = impute_from_column(df, impute_to = 'c_ssrs_6', impute_from = 'c_ssrs_last_visit_6')
    df[(df['c_ssrs_6'].isna()) & (~df['c_ssrs_last_visit_6'].isna())][['c_ssrs_6', 'c_ssrs_last_visit_6']]

    """
    df[impute_to] = np.where(df[impute_to].isnull(), df[impute_from], df[impute_to])
    return df


def impute_mean_questionnaire_score(df, questionnaire_columns):

    def impute_row_with_mean(row):
        mean_value = row.dropna().mean()
        row = row.fillna(mean_value)
        return row

    # Assuming 'df' is your DataFrame and 'columns_name' is the name of the questionnaire columns

    df[questionnaire_columns] = df[questionnaire_columns].apply(impute_row_with_mean, axis=1)
    return df


def is_number_within_range(target_range, number):
    lower_bound, upper_bound = map(int, target_range.split('-'))
    return lower_bound <= number <= upper_bound


def normalize_scores(df, columns=columns_need_normalization):
    columns = [i for i in columns if i in df.columns]
    scaler = StandardScaler()
    normalized_column_names = [f"{column}_normalized" for column in columns]
    normalized_columns = scaler.fit_transform(df[columns])
    df[normalized_column_names] = normalized_columns

    return df, normalized_column_names
