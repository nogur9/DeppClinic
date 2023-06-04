from utils.consts.subsets_of_questionnaires import sci_af_ac_factors, C_ssrs_clinician, sci_af_ca_new_questions
from utils.consts.subsets_of_questionnaires import sdq_reverse, sdq_normal, c_ssrs_life_values_map, c_ssrs_2weeks_values_map
from utils.consts.questions_columns import mfq, siq, scared, SAS, ATHENS, c_ssrs, sci_af_ca, scs_clin, sci_mother

# util functions
from utils.utils import impute_from_column


def get_max_index(df, questions_values_map):
    questions_values = df[questions_values_map.keys()] * questions_values_map.values()
    max_value = questions_values.max(axis=1)
    return max_value


# compute scores
def compute_sdq_score(df, skipna = False):
    sdq_reverse_columns = [f"{i}_reverse" for i in sdq_reverse]

    df[sdq_reverse_columns] = 2 - df[sdq_reverse]
    sdq_columns = sdq_normal + sdq_reverse_columns
    df['sdq_score'] = df[sdq_columns].sum(axis=1, skipna=skipna)

    missing_values = df[sdq_columns].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_sdq_values'] = missing_values_sum / len(sdq_columns)

    df = df.drop(sdq_reverse_columns, axis=1)


    return df, ['sdq_score', 'ratio_of_missing_sdq_values']


def compute_mfq_score(df, skipna = False):
    """
    SPSS code, I think it's wrong therefore it's doing sum of our mfq columns

    ****QUALTRICS****
    **MFQ_SUM**

    COMPUTE MFQ_SUM=SUM(MFQ_1,MFQ_2,MFQ_3,MFQ_4,MFQ_5,MFQ_6,MFQ_7,MFQ_8,MFQ_9,MFQ_10,MFQ_11,MFQ_12,MFQ_13,MFQ_14,MFQ_15,MFQ_16,
        MFQ_17,MFQ_18,MFQ_19,MFQ_20,MFQ_21,MFQ_22,MFQ_23,MFQ_24,MFQ_25,MFQ_26,MFQ_27,MFQ_28,MFQ_29,MFQ_30,MFQ_31,MFQ_32,MFQ_33).
    EXECUTE.

    ****REDCAP****
    **MFQ_SUM (SHORT VER.)**

    COMPUTE MFQ_SUM=SUM(MFQ_1,MFQ_2,MFQ_5,MFQ_7,MFQ_8,MFQ_14,MFQ_21,MFQ_23,MFQ_24,MFQ_27,MFQ_28,MFQ_30,MFQ_31).
    EXECUTE.
    """
    df['mfq_score'] = df[mfq].sum(axis=1, skipna=skipna)

    missing_values = df[mfq].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_mfq_values'] = missing_values_sum / len(mfq)

    return df, ['mfq_score', 'ratio_of_missing_mfq_values']


def compute_siq_score(df):
    """
    spss code:

    COMPUTE SIQ_SUM=SUM(SIQ_1,SIQ_2,SIQ_3,SIQ_4,SIQ_5,SIQ_6,SIQ_7,SIQ_8,SIQ_9,SIQ_10,SIQ_11,SIQ_12,SIQ_13,SIQ_14,SIQ_15).
    EXECUTE.

    """
    df['siq_score'] = df[siq].sum(axis=1, skipna=False)

    missing_values = df[siq].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_siq_values'] = missing_values_sum / len(siq)

    return df, ['siq_score', 'ratio_of_missing_siq_values']


def compute_scared_score(df, skipna = False):
    """
    COMPUTE SCARED_SUM=SUM(SCARED_1,SCARED_2,SCARED_3,SCARED_4,SCARED_5,SCARED_6,SCARED_7,SCARED_8,SCARED_9,SCARED_10,
        SCARED_11,SCARED_12,SCARED_13,SCARED_14,SCARED_15,SCARED_16,SCARED_17,SCARED_18,SCARED_19,SCARED_20,SCARED_21,SCARED_22,
        SCARED_23,SCARED_24,SCARED_25,SCARED_26,SCARED_27,SCARED_28,SCARED_29,SCARED_30,SCARED_31,SCARED_32,SCARED_33,SCARED_34,
        SCARED_35,SCARED_36,SCARED_37,SCARED_38,SCARED_39,SCARED_40,SCARED_41).
    EXECUTE.
    """

    df['scared_score'] = df[scared].sum(axis=1, skipna=skipna)

    missing_values = df[scared].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_scared_values'] = missing_values_sum / len(scared)

    return df, ['scared_score', 'ratio_of_missing_scared_values']


def compute_sas_score(df, skipna = False):
    """

    RECODE SAS_1,SAS_2,SAS_3,SAS_4,SAS_5,SAS_6,SAS_7,SAS_8,SAS_9,SAS_10,SAS_11,SAS_12,SAS_13,SAS_14,SAS_15,SAS_16,SAS_17,
        SAS_18,SAS_19,SAS_20,SAS_21,SAS_22,SAS_23 (1=1) (2=2) (3=3) (4=4) (5=5) (6=6).
    EXECUTE.

    COMPUTE SAS_MEAN=MEAN(SAS_1,SAS_2,SAS_3,SAS_4,SAS_5,SAS_6,SAS_7,SAS_8,SAS_9,SAS_10,
        SAS_11,SAS_12,SAS_13,SAS_14,SAS_15,SAS_16,SAS_17,SAS_18,SAS_19,SAS_20,SAS_21,SAS_22,
        SAS_23).
    EXECUTE.


    """
    df['sas_score'] = df[SAS].mean(axis=1, skipna=skipna)

    missing_values = df[SAS].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_sas_values'] = missing_values_sum / len(SAS)

    return df, ['sas_score', 'ratio_of_missing_sas_values']


def compute_athens_score(df, skipna = False):
    """

    COMPUTE
    ATHENS_SUM=SUM(athens_1,athens_2,athens_3,athens_4,athens_5,athens_6,athens_7,athens_8).
    EXECUTE.

    """
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


def compute_scs_clin_score(df, skipna = False):

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


# C_SSRS questionnaire


def calculate_c_ssrs_individual_score(df, severity):
    
    c_ssrs_values_map = {
    'c_ssrs_1': 1,
    'c_ssrs_2': 2,
    'c_ssrs_3': 3,
    'c_ssrs_4': 4,
    'c_ssrs_5': 5,
    'c_ssrs_6': 6,
    'c_ssrs_last_visit_6': 6
    }
    
    if severity == 'idea':
        stb_questions = [i for i in c_ssrs_values_map.keys() if c_ssrs_values_map[i] > 5]
        for question in stb_questions:
            c_ssrs_values_map.pop(question)
    elif severity == 'stb':
        pass
    else:
        raise ValueError

    agg_score = get_max_index(df, c_ssrs_values_map)
    
    return agg_score


def c_ssrs_roll_negative(df, c_ssrs_columns):

    # Check if the first 2 items are 0 and the last 4 items are missing (NaN)

    c_ssrs_columns = list(c_ssrs_columns)
    negative_columns_condition = (df[c_ssrs_columns[0]] == 0) & (df[c_ssrs_columns[1]] == 0)
    redundant_columns_condition = df[c_ssrs_columns[2:]].isna().all(axis=1)
    redundant_columns = c_ssrs_columns[2:]

    mask = negative_columns_condition & redundant_columns_condition

    # Impute the last 4 items with 0 where the conditions are met
    df.loc[mask, redundant_columns] = 0

    return df


def calculate_c_ssrs_scores(df, prefix='', impute_question_6=True, rolling_negative=True):
    if impute_question_6:
        df = impute_from_column(df, impute_to='c_ssrs_6', impute_from='c_ssrs_last_visit_6')

    if rolling_negative:
        df = c_ssrs_roll_negative(df, c_ssrs)

    df[f'c_ssrs_idea_score'] = calculate_c_ssrs_individual_score(df, severity='idea')
    df[f'c_ssrs_stb_score'] = calculate_c_ssrs_individual_score(df, severity='stb')

    missing_values = df[c_ssrs[:6]].isnull()
    missing_values_sum = missing_values.sum(axis=1)
    df['ratio_of_missing_c_ssrs_values'] = missing_values_sum / 6

    return df, ['c_ssrs_idea_score', 'c_ssrs_stb_score', 'ratio_of_missing_c_ssrs_values']


def calculate_intake_c_ssrs_individual_score(df, severity ='stb', time ='life'):
    
    if time == 'life':
        c_ssrs_values_map = c_ssrs_life_values_map
    
    elif time == '2weeks':
        c_ssrs_values_map = c_ssrs_2weeks_values_map
        
    elif time == 'recent':
        c_ssrs_values_map = c_ssrs_2weeks_values_map
        c_ssrs_values_map['c_ssrs_6_3month'] = 6
    else:
        raise ValueError
        
    if severity == 'idea':
        stb_questions = [i for i in c_ssrs_values_map.keys() if c_ssrs_values_map[i] > 5]
        for question in stb_questions:
            c_ssrs_values_map.pop(question)
    elif severity == 'stb':
        pass
    else:
        raise ValueError

    agg_score = get_max_index(df, c_ssrs_values_map)
    
    return agg_score


def calculate_c_ssrs_scores_intake(df, rolling_negative=True):

    if rolling_negative:
        c_ssrs_cols = list(c_ssrs_life_values_map.keys())
        df = c_ssrs_roll_negative(df, c_ssrs_cols)

        c_ssrs_cols = list(c_ssrs_2weeks_values_map.keys()) + ['c_ssrs_6_3month']
        df = c_ssrs_roll_negative(df,  c_ssrs_cols)

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


def calculate_clinician_c_ssrs_individual_score(df, score_info, rolling_negative):

    if score_info['agg_method'] == 'max':
        if rolling_negative:
            df = c_ssrs_roll_negative(df, score_info['columns'])

        c_ssrs_values_map = {value: (idx + 1) for idx, value in enumerate(score_info['columns'])}
        score = get_max_index(df, c_ssrs_values_map)

    elif score_info['agg_method'] == 'no':
        score = df[score_info['columns']]
    else:
        raise ValueError

    return score


