import numpy as np
rename_align = {'gender': 'sex.1',
                'age_child_pre': 'age',
                'parent_religion_m': 'religion',

                "swan_1_m": 't1_p_swan_1',
                "swan_2_m": 't1_p_swan_2',
                "swan_3_m": 't1_p_swan_3',
                "swan_4_m": 't1_p_swan_4',
                "swan_5_m": 't1_p_swan_5',
                "swan_6_m": 't1_p_swan_6',
                "swan_7_m": 't1_p_swan_7',
                "swan_8_m": 't1_p_swan_8',
                "swan_9_m": 't1_p_swan_9',
                "swan_10_m": 't1_p_swan_10',
                "swan_11_m": 't1_p_swan_11',
                "swan_12_m": 't1_p_swan_12',
                "swan_13_m": 't1_p_swan_13',
                "swan_14_m": 't1_p_swan_14',
                "swan_15_m": 't1_p_swan_15',
                "swan_16_m": 't1_p_swan_16',
                "swan_17_m": 't1_p_swan_17',
                "swan_18_m": 't1_p_swan_18',

                "swan_attention": 't1_p_swan_sum1-9',
                "swan_impulsivity": 't1_p_swan_sum10-18'
}


info_columns = ['gender', 'age_child_pre']

swan_m = ["swan_1_m", "swan_2_m", "swan_3_m", "swan_4_m", "swan_5_m", "swan_6_m", "swan_7_m",
          "swan_8_m", "swan_9_m", "swan_10_m", "swan_11_m", "swan_12_m", "swan_13_m",
          "swan_14_m", "swan_15_m", "swan_16_m", "swan_17_m", "swan_18_m"]
idx_CBCL_anx = [14, 29, 30, 31, 32,33,35, 45, 50, 52, 71, 91, 112]
CBCL_anx = [f"t1_p_rawscore_cbcl_{i}" for i in  idx_CBCL_anx]


idx_CBCL_with = [5, 42, 65, 69, 75, 102, 103, 111]
CBCL_with = [f"t1_p_rawscore_cbcl_{i}" for i in  idx_CBCL_anx]


swan_factors_ = {
    'swan_attention': [f'swan_{i}_m' for i in range(1, 10)],
    'swan_impulsivity': [f'swan_{i}_m' for i in range(10, 19)]

}


CBCL = CBCL_with + CBCL_anx


def compute_swan_scores(df, impute=True):
    """
    questionnaires['swan_m']['columns']
    """

    swan_columns = swan_m
    missing_values = df[swan_columns].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_swan_values'] = missing_values_sum / len(swan_columns)

    if impute:
        df = impute_mean_questionnaire_score(df, swan_columns)

    swan_factors = list(swan_factors_.keys())
    for key in swan_factors:
        factor_columns = swan_factors_[key]

        df[key] = df[factor_columns].sum(axis=1)

    df['swan_score'] = df[swan_columns].sum(axis=1)
    df['swan_sum'] = df[swan_columns].sum(axis=1)

    params = swan_factors + ["swan_attention", "swan_impulsivity", "ratio_of_missing_swan_values", "swan_score", "swan_sum"]

    return df, params


def compute_CBCL_scores(df, impute=True):
    """
    questionnaires['swan_m']['columns']
    """

    swan_columns = swan_m
    missing_values = df[swan_columns].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_swan_values'] = missing_values_sum / len(swan_columns)

    if impute:
        df = impute_mean_questionnaire_score(df, swan_columns)

    swan_factors = list(swan_factors_.keys())
    for key in swan_factors:
        factor_columns = swan_factors_[key]

        df[key] = df[factor_columns].sum(axis=1)

    df['swan_score'] = df[swan_columns].sum(axis=1)
    df['swan_sum'] = df[swan_columns].sum(axis=1)

    params = swan_factors + ["swan_attention", "swan_impulsivity", "ratio_of_missing_swan_values", "swan_score", "swan_sum"]

    return df, params


def impute_mean_questionnaire_score(df, questionnaire_columns):

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