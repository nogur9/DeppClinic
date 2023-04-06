import pandas as pd
import numpy as np


sci_af_ac_agg_map = {
  'sci_af_ca_Factor1': ['sci_af_ca_5',
  'sci_af_ca_6',
  'sci_af_ca_13',
  'sci_af_ca_15',
  'sci_af_ca_16',
  'sci_af_ca_19',
  'sci_af_ca_20',
  'sci_af_ca_22',
  'sci_af_ca_24',
  'sci_af_ca_25'],
 'sci_af_ca_Factor2': ['sci_af_ca_1',
  'sci_af_ca_2',
  'sci_af_ca_3',
  'sci_af_ca_7',
  'sci_af_ca_8',
  'sci_af_ca_9',
  'sci_af_ca_10',
  'sci_af_ca_11',
  'sci_af_ca_14',
  'sci_af_ca_17',
  'sci_af_ca_26'],
 'sci_af_ca_Factor3': ['sci_af_ca_4',
  'sci_af_ca_12',
  'sci_af_ca_18',
  'sci_af_ca_21',
  'sci_af_ca_23',
  'sci_af_ca_27',
  'sci_af_ca_28'],
 'sci_af_ca_Factor4': ['sci_af_ca_29',
  'sci_af_ca_30',
  'sci_af_ca_31',
  'sci_af_ca_32',
  'sci_af_ca_33',
  'sci_af_ca_34',
  'sci_af_ca_40'],
 'sci_af_ca_Factor5': ['sci_af_ca_35',
  'sci_af_ca_36',
  'sci_af_ca_37',
  'sci_af_ca_38',
  'sci_af_ca_39']}

def get_max_index(df, questions_values_map):
    questions_values = df[questions_values_map.keys()] * questions_values_map.values()
    max_value = questions_values.max(axis=1)
    return max_value
    

def sci_af_ac_aggregation(df):
    
    for key in sci_af_ac_agg_map.keys():
        df[key] = df[sci_af_ac_agg_map[key]].sum(axis=1)
    
    params = ['sci_af_ca_Factor1', 'sci_af_ca_Factor2',
             'sci_af_ca_Factor3', 'sci_af_ca_Factor4', 
             'sci_af_ca_Factor5']
    return df, params



def c_ssrs_aggregation(df, severity):
    
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


    
def c_ssrs_intake_aggregation(df, severity = 'stb', time = 'life'):
    
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



