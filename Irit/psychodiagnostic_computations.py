import numpy as np

from Irit.Variables import SDQ_thresholds, cbcl_thresholds, swan_m, swan_factors_, CBCL, CBCL_factors_
from Irit.utils_Irit import is_number_within_range, impute_mean_questionnaire_score


def get_sdq_diagnosis(x, factor):
    if np.isnan(x[factor]):
        return np.NaN
    sdq_age_thresholds = SDQ_thresholds[factor]
    normal_score = sdq_age_thresholds["Normal"]
    borderline_score = sdq_age_thresholds["Borderline"]
    abnormal_score = sdq_age_thresholds["Abnormal"]

    if x[factor] <= normal_score:
        return 'Normal'
    elif x[factor] <= borderline_score:
        return 'Borderline'
    elif x[factor] <= abnormal_score:
        return 'Abnormal'
    else:
        raise ValueError


def get_cbcl_diagnosis(x, factor):

    cbcl_age_thresholds = cbcl_thresholds[factor][x['gender']]
    outliers_young_range = "4-6"
    young_age_range = "6-11"
    older_age_range = "11-18"
    if is_number_within_range(young_age_range, x['age_child_pre']) or \
        is_number_within_range(outliers_young_range, x['age_child_pre']):
        normal_score = cbcl_age_thresholds[young_age_range]['Normal']
        borderline_score = cbcl_age_thresholds[young_age_range]['Borderline']
        abnormal_score = cbcl_age_thresholds[young_age_range]['Abnormal']
    elif is_number_within_range(older_age_range, x['age_child_pre']):
        normal_score = cbcl_age_thresholds[older_age_range]['Normal']
        borderline_score = cbcl_age_thresholds[older_age_range]['Borderline']
        abnormal_score = cbcl_age_thresholds[older_age_range]['Abnormal']
    else:
        raise ValueError

    if x[factor] <= normal_score:
        return 'Normal'
    elif x[factor] <= borderline_score:
        return 'Borderline'
    elif x[factor] <= abnormal_score:
        return 'Abnormal'
    else:
        raise ValueError


def get_swan_diagnosis(x, factor, return_int=True):

    num_significant_questions = (x[swan_factors_[factor]] >= 1).sum()
    is_pathological = num_significant_questions >= 6

    if return_int:
        return is_pathological
    else:
        return "Abnormal" if is_pathological else "Normal"


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

    df['swan_score'] = df[swan_columns].sum(axis=1)
    df['swan_sum'] = df[swan_columns].sum(axis=1)

    params = ["swan_score", "swan_sum", "ratio_of_missing_swan_values"]

    for key in swan_factors:
        factor_columns = swan_factors_[key]
        df[f"{key}_sum"] = df[factor_columns].sum(axis=1)
        df[f"{key}_diagnosis"] = df[factor_columns].apply(get_swan_diagnosis, args=[key], axis=1)
        params.extend([f"{key}_sum", f"{key}_diagnosis"])

    return df, params


def compute_cbcl_scores(df, impute=True):

    cbcl_columns = CBCL
    missing_values = df[cbcl_columns].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_cbcl_values'] = missing_values_sum / len(cbcl_columns)

    if impute:
        df = impute_mean_questionnaire_score(df, cbcl_columns)

    cbcl_factors = list(CBCL_factors_.keys())
    for key in cbcl_factors:
        factor_columns = CBCL_factors_[key]

        df[key] = df[factor_columns].sum(axis=1)

    df['CBCL_int_raw_score'] = df[['CBCL_Anxious/Depressed', 'CBCL_Withdrawn/Depressed']].sum(axis=1)
    df['CBCL_Anxious/Depressed_Diagnosis'] = df.apply(get_cbcl_diagnosis, args=['CBCL_Anxious/Depressed'], axis=1)
    df['CBCL_Withdrawn/Depressed_Diagnosis'] = df.apply(get_cbcl_diagnosis, args=['CBCL_Withdrawn/Depressed'], axis=1)

    params = cbcl_factors + ["ratio_of_missing_cbcl_values", "CBCL_int_raw_score"]

    return df, params


def compute_sdq_scores(df):
    params = []
    for key in SDQ_thresholds.keys():
        df[f"{key[:-3]}_Diagnosis"] = df.apply(get_sdq_diagnosis, args=[key], axis=1)
        params.append(f"{key[:-3]}_Diagnosis")
    return df, params


