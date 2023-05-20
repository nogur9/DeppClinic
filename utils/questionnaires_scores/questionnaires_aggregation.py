from utils.consts.subsets_of_questionnaires import sci_af_ac_factors
from utils.consts.subsets_of_questionnaires import sdq_reverse, sdq_normal
from utils.consts.questions_columns import mfq, siq

# util functions


def get_max_index(df, questions_values_map):
    questions_values = df[questions_values_map.keys()] * questions_values_map.values()
    max_value = questions_values.max(axis=1)
    return max_value


# compute scores
def compute_sdq_score(df):
    sdq_reverse_columns = [f"{i}_reverse" for i in sdq_reverse]

    df[sdq_reverse_columns] = 2 - df[sdq_reverse]
    df['sdq_score'] = df[sdq_normal + sdq_reverse_columns].sum(axis=1, skipna=False)
    df = df.drop(sdq_reverse_columns, axis=1)
    return df

def compute_mfq_score(df):
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
    df['mfq_score'] = df[mfq].sum(axis=1, skipna=False)
    return df

def compute_siq_score(df):
    """
    spss code:

    COMPUTE SIQ_SUM=SUM(SIQ_1,SIQ_2,SIQ_3,SIQ_4,SIQ_5,SIQ_6,SIQ_7,SIQ_8,SIQ_9,SIQ_10,SIQ_11,SIQ_12,SIQ_13,SIQ_14,SIQ_15).
    EXECUTE.

    """
    df['siq_score'] = df[siq].sum(axis=1, skipna=False)

def compute_sci_af_ac_score(df):

    for key in sci_af_ac_factors.keys():
        df[key] = df[sci_af_ac_factors[key]].sum(axis=1, skipna=False)

    params = ['sci_af_ca_Factor1', 'sci_af_ca_Factor2',
             'sci_af_ca_Factor3', 'sci_af_ca_Factor4',
             'sci_af_ca_Factor5']
    return df, params


def compute_c_ssrs_score(df, severity):
    
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
        
    agg_score = get_max_index(df, c_ssrs_values_map)
    
    return agg_score


def compute_c_ssrs_intake_score(df, severity ='stb', time ='life'):
    
    c_ssrs_life_values_map = {
    'c_ssrs_1_life': 1,
    'c_ssrs_2_life': 2,
    'c_ssrs_3_life': 3,
    'c_ssrs_4_life': 4,
    'c_ssrs_5_life': 5,
    'c_ssrs_6_life': 6}
    
    c_ssrs_2weeks_values_map = {
    'c_ssrs_1_2weeks':1,
    'c_ssrs_2_2weeks':2,
    'c_ssrs_3_2weeks':3,
    'c_ssrs_4_2weeks':4,
    'c_ssrs_5_2weeks':5,
    'c_ssrs_6_2weeks':6}
    
    
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
        
    agg_score = get_max_index(df, c_ssrs_values_map)
    
    return agg_score



    
# def c_ssrs_clin_aggregation(df, severity = 'stb', time = 'life'):
    

    
#     c_ssrs_2weeks_values_map = {
#         'c_ssrs_t_2weeks_1_clin':
#         'c_ssrs_t_2weeks_2_clin':
#         'c_ssrs_t_2weeks_3_clin':
#         'c_ssrs_t_2weeks_4_clin':
#         'c_ssrs_t_2weeks_5_clin':
#         }

    
#     c_ssrs_life_values_map = {
#         'c_ssrs_t_last_1_clin':
#         'c_ssrs_t_last_2_clin':
#         'c_ssrs_t_last_3_clin':
#         'c_ssrs_t_last_4_clin':
#         'c_ssrs_t_last_5_clin':
#         }
    
    
    
#     c_ssrs_life_values_map = {
#         'c_ssrs_t_life_1_clin':
#         'c_ssrs_t_life_2_clin':
#         'c_ssrs_t_life_3_clin':
#         'c_ssrs_t_life_4_clin':
#         'c_ssrs_t_life_5_clin':
#         }


#     c_ssrs_life_values_map = {
#         'c_ssrs_t_6_clin':
#         'c_ssrs_t_7_clin':
#         'c_ssrs_t_8_clin':
#         'c_ssrs_t_9_clin':
#         'c_ssrs_t_10_clin':
#         'c_ssrs_t_6_clin_2':
#         'c_ssrs_t_7_clin_2':
#         'c_ssrs_t_8_clin_2':
#         'c_ssrs_t_9_clin_2':
#         'c_ssrs_t_10_clin_2':
#         }

#     c_ssrs_life_values_map = {
#         'c_ssrs_t_11_2weeks_clin':
#         'c_ssrs_t_12_2weeks_clin':
#         'c_ssrs_t_13_2weeks_clin':
#         'c_ssrs_t_14_2weeks_clin':
#         'c_ssrs_t_15_2weeks_clin':
#         'c_ssrs_t_16_2weeks_clin':
#         }

        
#     c_ssrs_life_values_map = {
#         'suicidal_behavior_last_11_clin':
#         'suicidal_behavior_last_12_clin':
#         'suicidal_behavior_last_13_clin':
#         'suicidal_behavior_last_14_clin':
#         'suicidal_behavior_last_15_clin':
#         'suicidal_behavior_last_16_clin':
#         'suicidal_behavior_last_17_clin':
#         'suicidal_behavior_last_11_clin_1':
#         'suicidal_behavior_last_12_clin_1':
#         'suicidal_behavior_last_13_clin_1':
#         'suicidal_behavior_last_18_clin':
#         'suicidal_behavior_last_19_clin':
#         }

        
#     c_ssrs_life_values_map = {
#         'c_ssrs_t_11_life_clin':
#         'c_ssrs_t_12_life_clin':
#         'c_ssrs_t_13_life_clin':
#         'c_ssrs_t_14_life_clin':
#         'c_ssrs_t_15_life_clin':
#         'c_ssrs_t_16_life_clin':
#         'c_ssrs_t_17_life_clin':
#         'c_ssrs_t_11_life_clin_1':
#         'c_ssrs_t_12_life_clin_1':
#         'c_ssrs_t_13_life_clin_1':
#         'c_ssrs_t_18_life_clin':
#         'c_ssrs_t_19_life_clin':
#         }
    
#     if time == 'life':
#         c_ssrs_values_map = c_ssrs_life_values_map
    
#     elif time == '2weeks':
#         c_ssrs_values_map = c_ssrs_2weeks_values_map
        
#     elif time == 'recent':
#         c_ssrs_values_map = c_ssrs_2weeks_values_map
#         c_ssrs_values_map['c_ssrs_6_3month'] = 6
#     else:
#         raise ValueError
        
#     if severity == 'idea':
#         stb_questions = [i for i in c_ssrs_values_map.keys() if c_ssrs_values_map[i] > 5]
#         for question in stb_questions:
#             c_ssrs_values_map.pop(question)
        
#     agg_score = get_max_index(df, c_ssrs_values_map)
    
#     return agg_score



