import numpy as np
from source.utils.consts.subsets_of_questionnaires import sci_af_ac_factors, C_ssrs_clinician, sci_af_ca_new_questions, \
    maris_soq_sf_reverse, maris_soq_sf_normal, MAST_factors, SDQ_factors, DERS_factors, swan_factors, \
    erc_rc_reversed_items, erc_rc_factors, dass_factors
from source.utils.consts.subsets_of_questionnaires import sdq_reverse, c_ssrs_life_values_map, \
    c_ssrs_2weeks_values_map, DERS_reverse_items, wai_reversed_items, wai_factors
from source.utils.consts.questions_columns import c_ssrs, maris_sci_sf, maris_soq_sf, MAST, DERS, wai, swan_m, \
    sci_mother, scs_clin, sci_af_ca, ATHENS, SAS, scared, mfq, siq, erc_rc, ARI_S, ARI_P_m
from source.utils.old_questionnaires_scores.utils import impute_mean_questionnaire_score
from source.utils.old_questionnaires_scores.cssrs import calculate_clinician_c_ssrs_individual_score, \
    calculate_intake_c_ssrs_individual_score, c_ssrs_roll_negative, calculate_c_ssrs_individual_score


def compute_sdq_score(df, skipna=False):

    sdq_reverse_columns = [f"{i}_reverse" for i in sdq_reverse]

    df[sdq_reverse_columns] = 2 - df[sdq_reverse]
    sdq_columns = sdq_normal + sdq_reverse_columns
    df['sdq_score'] = df[sdq_columns].sum(axis=1, skipna=skipna)
    df['sdq_sum'] = df[sdq_columns].sum(axis=1, skipna=skipna)
    missing_values = df[sdq_columns].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_sdq_values'] = missing_values_sum / len(sdq_columns)

    for key in SDQ_factors.keys():
        df[key] = df[SDQ_factors[key]].sum(axis=1, skipna=skipna)
    df = df.drop(sdq_reverse_columns, axis=1)
    params = list(SDQ_factors.keys()) + ['sdq_score', 'ratio_of_missing_sdq_values']

    return df, params


def compute_mfq_score(df, skipna=False):


    df['mfq_score'] = df[mfq].sum(axis=1, skipna=skipna)

    missing_values = df[mfq].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_mfq_values'] = missing_values_sum / len(mfq)
    df.loc[df[f'ratio_of_missing_mfq_values'] >= 0.99, 'mfq_score'] = np.nan

    return df, ['mfq_score', 'ratio_of_missing_mfq_values']


def compute_siq_score(df):

    df['siq_score'] = df[siq].sum(axis=1, skipna=False)

    missing_values = df[siq].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_siq_values'] = missing_values_sum / len(siq)

    return df, ['siq_score', 'ratio_of_missing_siq_values']


def compute_scared_score(df, skipna=False):

    df['scared_score'] = df[scared].sum(axis=1, skipna=skipna)

    missing_values = df[scared].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_scared_values'] = missing_values_sum / len(scared)

    return df, ['scared_score', 'ratio_of_missing_scared_values']


def compute_sas_score(df, skipna=False):

    df['sas_score'] = df[SAS].mean(axis=1, skipna=skipna)

    missing_values = df[SAS].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_sas_values'] = missing_values_sum / len(SAS)

    return df, ['sas_score', 'ratio_of_missing_sas_values']  # sas_mean_score


def compute_athens_score(df, skipna=False):

    df['athens_score'] = df[ATHENS].sum(axis=1, skipna=skipna)

    missing_values = df[ATHENS].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_athens_values'] = missing_values_sum / len(ATHENS)

    return df, ['athens_score', 'ratio_of_missing_athens_values']


# SCS questionnaire


def compute_sci_af_ac_score(df, skipna=False):
    for key in sci_af_ac_factors.keys():
        df[key] = df[sci_af_ac_factors[key]].mean(axis=1, skipna=skipna)

    df['sci_af_ac_score'] = df[sci_af_ca].mean(axis=1, skipna=skipna)

    missing_values = df[sci_af_ca].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_sci_af_ac_values'] = missing_values_sum / len(sci_af_ca)

    df['sci_af_ca_is_new_questions_missing'] = df[sci_af_ca_new_questions].isna().all(axis=1)

    params = list(sci_af_ac_factors.keys()) + ['sci_af_ac_score', 'ratio_of_missing_sci_af_ac_values',
                                               'sci_af_ca_is_new_questions_missing']

    return df, params


def compute_scs_clin_score(df, skipna=False):
    df['scs_clin_score'] = df[scs_clin].mean(axis=1, skipna=skipna)

    missing_values = df[scs_clin].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_scs_clin_values'] = missing_values_sum / len(scs_clin)

    return df, ['scs_clin_score', 'ratio_of_missing_scs_clin_values']


def compute_scs_mother_score(df, skipna=False):
    df['sci_mother_score'] = df[sci_mother].mean(axis=1, skipna=skipna)
    missing_values = df[sci_mother].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_sci_mother_values'] = missing_values_sum / len(sci_mother)

    return df, ['sci_mother_score', 'ratio_of_missing_sci_mother_values']


def compute_mast_score(df, skipna=False):

    # Compute mean for MAST_AL
    df['MAST_AL'] = df[MAST_factors['MAST_AL']].mean(axis=1, skipna=skipna)

    # Compute mean for MAST_RL
    df['MAST_RL'] = df[MAST_factors['MAST_RL']].mean(axis=1, skipna=skipna)

    # Compute mean for MAST_AD
    df['MAST_AD'] = df[MAST_factors['MAST_AD']].mean(axis=1, skipna=skipna)

    # Compute mean for MAST_RD
    df['MAST_RD'] = df[MAST_factors['MAST_RD']].mean(axis=1, skipna=skipna)

    missing_values = df[MAST].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_mast_values'] = missing_values_sum / len(MAST)

    return df, ['ratio_of_missing_mast_values', 'MAST_AL', 'MAST_RL', 'MAST_AD', 'MAST_RD']


# ARI-S


def compute_ari_p_score(df, skipna=False):

    # Compute the sum for ARI_P_SUM
    df['ARI_P_SUM'] = df[ARI_P_m].sum(axis=1, skipna=skipna)
    df['ari_p_score'] = df[ARI_P_m].sum(axis=1, skipna=skipna)

    missing_values = df[ARI_P_m].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_ari_p_values'] = missing_values_sum / len(ARI_P_m)

    return df, ['ARI_P_SUM', 'ari_p_score', 'ratio_of_missing_ari_p_values']


def compute_ari_s_score(df, skipna=False):
    """
    COMPUTE ARI_S_SUM=SUM(ari_s_1,ari_s_2,ari_s_3,ari_s_4,ari_s_5,ari_s_6).
    EXECUTE.

    """

    # Compute the sum for ARI_S_SUM
    df['ARI_S_SUM'] = df[ARI_S].sum(axis=1, skipna=skipna)
    df['ari_s_score'] = df[ARI_S].sum(axis=1, skipna=skipna)

    missing_values = df[ARI_S].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_ari_s_values'] = missing_values_sum / len(ARI_S)

    return df, ['ARI_S_SUM', 'ari_s_score', 'ratio_of_missing_ari_s_values']


# maris


def compute_maris_sci_sf_score(df, skipna=False):
    """


    RECODE maris_sci_sf_1 maris_sci_sf_2 maris_sci_sf_3 maris_sci_sf_4 maris_sci_sf_5 maris_sci_sf_6 maris_sci_sf_7 maris_sci_sf_8 maris_sci_sf_9
        (1=0) (2=1) (3=2) (4=3) (5=4).
    EXECUTE.

    COMPUTE MARIS_SCI_TOTAL=SUM(maris_sci_sf_1,maris_sci_sf_2,maris_sci_sf_3,maris_sci_sf_4,maris_sci_sf_5,maris_sci_sf_6,maris_sci_sf_7,maris_sci_sf_8,
       maris_sci_sf_9).
    EXECUTE.


    """
    # ToDo: Fix computation - wrong columns

    maris_sci_sf_columns = Questionnaires().questionnaires['maris_soq_sf']['columns']

    df[maris_sci_sf_columns] = df[maris_sci_sf_columns] - 1

    # Calculate MARIS_SCI_TOTAL
    df['MARIS_SCI_TOTAL'] = df[maris_sci_sf].sum(axis=1, skipna=skipna)
    df['maris_sci_sf_score'] = df[maris_sci_sf].sum(axis=1, skipna=skipna)

    missing_values = df[maris_sci_sf_columns].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_maris_sci_sf_values'] = missing_values_sum / len(maris_sci_sf_columns)

    return df, ['maris_sci_sf_score', 'MARIS_SCI_TOTAL', 'ratio_of_missing_maris_sci_sf_values']


def compute_maris_soq_sf_score(df, skipna=False):
    """

RECODE maris_soq_sf_1 maris_soq_sf_2 maris_soq_sf_3 maris_soq_sf_4 maris_soq_sf_5 maris_soq_sf_6 maris_soq_sf_7 maris_soq_sf_8 (1=0) (2=1) (3=2)
    (4=3) (5=4).
EXECUTE.

RECODE maris_soq_sf_2 maris_soq_sf_3 maris_soq_sf_5 (0=4) (1=3) (2=2) (3=1) (4=0) INTO maris_soq_sf_2R maris_soq_sf_3R maris_soq_sf_5R.
EXECUTE.

COMPUTE MARIS_SOQ_SUM=SUM(maris_soq_sf_1,maris_soq_sf_2R,maris_soq_sf_3R,maris_soq_sf_4,maris_soq_sf_5R,maris_soq_sf_6,maris_soq_sf_7,
    maris_soq_sf_8).
EXECUTE.

    """
    # Recode values in maris_soq_sf using a dictionary comprehension
    # ToDo: Fix computation - wrong columns

    maris_soq_sf_columns = Questionnaires().questionnaires['maris_soq_sf']['columns']
    df[maris_soq_sf_columns] = df[maris_soq_sf_columns] - 1

    # Create new variables maris_soq_sf_2R, maris_soq_sf_3R, maris_soq_sf_5R by recoding values

    maris_soq_sf_reverse_columns = [f"{i}_reverse" for i in maris_soq_sf_reverse]
    df[maris_soq_sf_reverse_columns] = 2 - df[maris_soq_sf_reverse]

    # Calculate MARIS_SOQ_SUM
    df['MARIS_SOQ_SUM'] = df[maris_soq_sf_reverse_columns + maris_soq_sf_normal].sum(axis=1, skipna=skipna)
    df['maris_soq_sf_score'] = df[maris_soq_sf_reverse_columns + maris_soq_sf_normal].sum(axis=1, skipna=skipna)

    missing_values = df[maris_soq_sf].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_maris_soq_sf_values'] = missing_values_sum / len(maris_soq_sf)

    return df, ['maris_soq_sf_score', 'maris_soq_sf_score', 'ratio_of_missing_maris_soq_sf_values']


# C_SSRS questionnaire


def calculate_c_ssrs_scores(df, impute_question_6=True, rolling_negative=True):
    from to_delete.data_manipulation.data_imputation import impute_from_column

    if impute_question_6:
        df = impute_from_column(df, impute_to='c_ssrs_6', impute_from='c_ssrs_last_visit_6')

    if rolling_negative:
        df = c_ssrs_roll_negative(df, c_ssrs)

    df['c_ssrs_idea_score'] = calculate_c_ssrs_individual_score(df, severity='idea')
    df['c_ssrs_stb_score'] = calculate_c_ssrs_individual_score(df, severity='stb')

    missing_values = df[c_ssrs[:6]].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_c_ssrs_values'] = missing_values_sum / 6

    return df, ['c_ssrs_idea_score', 'c_ssrs_stb_score', 'ratio_of_missing_c_ssrs_values']


def calculate_c_ssrs_scores_intake(df, rolling_negative=True):
    if rolling_negative:
        c_ssrs_cols = list(c_ssrs_life_values_map.keys())
        df = c_ssrs_roll_negative(df, c_ssrs_cols)

        c_ssrs_cols = list(c_ssrs_2weeks_values_map.keys()) + ['c_ssrs_6_3month']
        df = c_ssrs_roll_negative(df, c_ssrs_cols)

    columns_names = []

    for time in ['life', '2weeks', 'recent']:
        for severity in ['stb', 'idea']:
            columns_names.append(f'c_ssrs_intake_{time}_{severity}')
            df[f'c_ssrs_intake_{time}_{severity}'] = \
                calculate_intake_c_ssrs_individual_score(df, severity=severity, time=time)

    return df, columns_names


def calculate_c_ssrs_scores_clinician(df, rolling_negative=True):
    columns_names = []
    for single_score in C_ssrs_clinician.values():
        score_name = single_score['name']
        columns_names.append(score_name)
        df[score_name] = calculate_clinician_c_ssrs_individual_score(df, single_score, rolling_negative)

    return df, columns_names


# others

def compute_swan_scores(df, impute=True):
    """
    questionnaires['swan_m']['columns']
    """
    missing_values = df[swan_m].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_swan_values'] = missing_values_sum / len(swan_m)

    if impute:
        df = impute_mean_questionnaire_score(df, swan_m)

    for key in swan_factors:
        factor_columns = swan_factors[key]

        df[key] = df[factor_columns].sum(axis=1)

    df['swan_score'] = df[swan_m].sum(axis=1)
    df['swan_sum'] = df[swan_m].sum(axis=1)

    params = list(swan_factors.keys()) + ['ratio_of_missing_swan_values', 'swan_score', 'swan_sum']

    return df, params


def compute_ders_score(df, skipna=False):
    ders_reverse_columns = [f"{i}_reverse" for i in DERS_reverse_items]
    ders_aligned_columns = [i for i in DERS if i not in DERS_reverse_items]
    df[ders_reverse_columns] = 6 - df[DERS_reverse_items]

    df['DERS_sum'] = df[ders_aligned_columns + ders_reverse_columns].sum(axis=1, skipna=skipna)
    df['DERS_score'] = df[ders_aligned_columns + ders_reverse_columns].sum(axis=1, skipna=skipna)

    missing_values = df[DERS].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_DERS_values'] = missing_values_sum / len(DERS)
    df.loc[df[f'ratio_of_missing_DERS_values'] >= 0.99, ['DERS_score', 'DERS_sum']] = np.nan

    for key in DERS_factors.keys():
        df[key] = df[DERS_factors[key]].sum(axis=1, skipna=skipna)

        missing_values = df[DERS_factors[key]].isnull()
        missing_values_sum = missing_values.sum(axis=1)
        df[f'ratio_of_missing_{key}_values'] = missing_values_sum / len(DERS_factors[key])
        df.loc[df[f'ratio_of_missing_{key}_values'] >= 0.99, key] = np.nan

    df = df.drop(ders_reverse_columns, axis=1)
    params = list(DERS_factors.keys()) + ['DERS_score', 'DERS_sum', 'ratio_of_missing_DERS_values']

    return df, params


def compute_wai_score(df, skipna=False):
    wai_reverse_columns = [f"{i}_reverse" for i in wai_reversed_items]
    df[wai_reverse_columns] = 8 - df[wai_reversed_items]

    missing_values = df[wai].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_wai_values'] = missing_values_sum / len(wai)

    for key in wai_factors.keys():
        df[key] = df[wai_factors[key]].sum(axis=1, skipna=skipna)

        missing_values = df[wai_factors[key]].isnull()
        missing_values_sum = missing_values.sum(axis=1)
        df[f'ratio_of_missing_{key}_values'] = missing_values_sum / len(wai_factors[key])
        df.loc[df[f'ratio_of_missing_{key}_values'] >= 0.99, key] = np.nan

    df = df.drop(wai_reverse_columns, axis=1)
    params = list(wai_factors.keys()) + ['ratio_of_missing_wai_values']

    return df, params


def compute_ecr_score(df, skipna=False):
    erc_rc_reverse_columns = [f"{i}_reverse" for i in erc_rc_reversed_items]
    df[erc_rc_reverse_columns] = 8 - df[erc_rc_reversed_items]

    missing_values = df[erc_rc].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_erc_rc_values'] = missing_values_sum / len(erc_rc)

    for key in erc_rc_factors.keys():
        df[key] = df[erc_rc_factors[key]].sum(axis=1, skipna=skipna)

        missing_values = df[erc_rc_factors[key]].isnull()
        missing_values_sum = missing_values.sum(axis=1)
        df[f'ratio_of_missing_{key}_values'] = missing_values_sum / len(erc_rc_factors[key])
        df.loc[df[f'ratio_of_missing_{key}_values'] >= 0.99, key] = np.nan

    df = df.drop(erc_rc_reverse_columns, axis=1)
    params = list(erc_rc_factors.keys()) + ['ratio_of_missing_erc_rc_values']

    return df, params


def compute_dass_score(df, skipna=False):

    for key in dass_factors.keys():
        df[key] = df[dass_factors[key]].sum(axis=1, skipna=skipna)

        missing_values = df[dass_factors[key]].isnull()
        missing_values_sum = missing_values.sum(axis=1)
        df[f'ratio_of_missing_{key}_values'] = missing_values_sum / len(dass_factors[key])
        df.loc[df[f'ratio_of_missing_{key}_values'] >= 0.99, key] = np.nan

    params = list(dass_factors.keys()) + ['ratio_of_missing_erc_rc_values']

    return df, params
