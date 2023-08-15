import numpy as np
import warnings

from Irit.Variables import columns_need_t_score


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


def calc_t_scores(df, columns=columns_need_t_score):

    def clac_single_t_score(df, column, skipna):
        """
        # t-score  = (x - u) / (S / sqrtN)
        """
        N = df[column].count()
        if df[column].isna().sum() > N / 2:
            warnings.warn(f"more than 50% missing values in column {column}", category=UserWarning)

        mean = df[column].mean(skipna=skipna)
        std = df[column].std(skipna=skipna)

        t_scores = (df[column] - mean) / (std / N ** 0.5)

        df[f"{column}_t_score"] = t_scores

        return df, f"{column}_t_score"

    t_score_columns = []
    for column in columns:
        if column in df.columns:
            df, new_column_name = clac_single_t_score(df, column, skipna=True)
            t_score_columns.append(new_column_name)

    return df, t_score_columns

