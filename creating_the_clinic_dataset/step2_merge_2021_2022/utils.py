import numpy as np
import pandas as pd

def mark_inattentive_participants(df, year, inattentive_participants_index = 'pre-created'):
    df = df.copy()
    df['id & redcup'] = df['id'].astype(str) + '_' + df['redcap_event_name'].astype(str)
    df['inattentive_child'] = 0
    df['inattentive_mother'] = 0
    df['inattentive_father'] = 0
    
  
    if inattentive_participants_index == 'pre-created':
        index = pd.read_csv('inattentive_participants_index.csv')
        index['id & redcup'] = index['id'].astype(str) + '_' + index['redcap_event_name'].astype(str)
    
    
    for year in [2021, 2022]:
        index = index[index['year']==year]
        
        for participant in ['child', 'mother', 'father']:
            tmp_index = index[index['participant'] == participant]
            df.loc[df['id & redcup'].isin(tmp_index['id & redcup']), f'inattentive_{participant}'] = 1
        
    df = df.drop('id & redcup', axis=1)

    return df
    
def fix_wrong_record_id(df, year=2022):
    """
    This function takes a DataFrame as input, and applies the following cleaning steps:
    1. Replaces 'id' with 'A6735' when 'record_id' == 85.
    2. Removes the rows where 'record_id' == 550.

    Parameters:
        df (pandas DataFrame): The DataFrame to be cleaned.

    Returns:
        pandas DataFrame : The cleaned DataFrame.
    """
    df = df.copy()
    if year==2022:
        df.loc[df['record_id'] == 85, 'id'] = 'A6735'
        df = df[df['record_id'] != 550]
    
    elif year==2021:
        # df_2021[(df_2021['id'] == 'N4125') & (df_2021['redcap_event_name'] == 'intake_arm_1')]
        df = df[~((df['id'] == 'N4125') & (df['redcap_event_name'] == 'intake_arm_1') & (df['record_id'] == 328))]


    return df


def fill_id(df):
    """
    This function takes a DataFrame as input, and fills out the empty 'id' values by matching them to the 'record_id' which isn't empty.

    Parameters:
        df (pandas DataFrame): The DataFrame to be cleaned.

    Returns:
        pandas DataFrame : The cleaned DataFrame.
    """
    df=df.copy()
    id_map = df.dropna(subset=['id']).groupby('record_id')['id'].first()
    id_map = {key: id_map[key] for key in id_map.keys()}
    df['id'] = df['record_id'].apply(lambda x: id_map[x])
    return df


def format_datetime_columns(df):
    df = df.copy()
    timestamps = [col for col in df.columns if 'timestamp' in col]
    dates = [col for col in df.columns if 'date' in col]
    
    for col in timestamps + dates:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    return df

def delete_redundant_columns(df_2021, df_2022):
    df_2021 = df_2021.copy()
    df_2022 = df_2022.copy()

    completion_cols_2022 = [col for col in df_2022.columns if col.endswith('complete')]
    completion_cols_2021 = [col for col in df_2021.columns if col.endswith('complete')]
    cols_unique_to_2021 = [col for col in df_2021.columns if (col not in df_2022.columns) and (col not in completion_cols_2021)]

    df_2021 = df_2021.drop(completion_cols_2021, axis=1)
    df_2021 = df_2021.drop(cols_unique_to_2021, axis=1)
    df_2021 = df_2021.drop(['iat_done_no'], axis=1)
    
    df_2022 = df_2022.drop(completion_cols_2022, axis=1)
    df_2022 = df_2022.drop(['iat_done_no'], axis=1)
    return df_2021, df_2022

def delete_negative_age(df):
    df.loc[df['age_child_pre'] < 2, 'age_child_pre'] = np.float64(np.nan)
    return df
    

def fix_age(df):
    index = pd.read_csv('invalid_age.csv')
    for id_num in index['id']:
        correct_age = index[index['id'] == id_num]['age_child'].iloc[0]
        df.loc[df['id'] == id_num, 'age_child_pre'] = correct_age
  
    return df

def fill_missing_age(df):
    index = pd.read_csv('missing_age.csv')
    for id_num in index['id']:
        correct_age = index[index['id'] == id_num]['age_child_pre'].iloc[0]
        if not np.isnan(correct_age):
            df.loc[df['id'] == id_num, 'age_child_pre'] = correct_age
    return df
    
def remove_test_id(df):
    df = df[~df['id'].str.lower().str.contains('test')]
    return df