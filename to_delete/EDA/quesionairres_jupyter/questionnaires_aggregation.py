import pandas as pd
import numpy as np


def get_max_index(df, questions_values_map):
    questions_values = df[questions_values_map.keys()] * questions_values_map.values()

    max_value = questions_values.max(axis=1)
    return max_value
    

def c_ssrs_aggregation(df, severity = 'stb'):
    
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