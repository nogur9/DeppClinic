import pandas as pd
import numpy as np
import re



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


def IsClinician (row):
    """
    Determine if data in row belongs to either student or clinician.
    default - student
    step a: check 'who' column,
    1 = clinician
    2 = student
    
    if 'who' empty, do step b: check 'opening_therapist_battery_timestamp' column:
    if column not empty. determine it's clinician
    """
    
    questionnaire_operator = 'student'
    
    #step a
    if row['who'] == 1:
        questionnaire_operator = 'clinician'
        return questionnaire_operator
    
    elif row['who'] == 2:
        questionnaire_operator = 'student'
        return questionnaire_operator
    
    elif pd.isnull(row['opening_therapist_battery_timestamp']):
        questionnaire_operator = 'student'
        return questionnaire_operator
    else:
        questionnaire_operator = 'clinician'
        return questionnaire_operator
    
    
def map_additional_column_name_to_2021_student_column_name(column_name, target_columns_names):
    if column_name == 'cgi_s':
        return 'cgi_s_base_stu', True
    
    elif column_name in target_columns_names:
        #print('original column - ', column_name in target_columns_names)
        success = column_name in target_columns_names
        if not success:
            print(column_name)
        return column_name, success
    elif bool(re.search(r'___\d+$', column_name)):
        suffix = re.search(r'___\d+$', column_name)[0]
        new_column_name = column_name.replace(suffix, f'_stu{suffix}')
        # validate
        #print('before number suffix - ', new_column_name in target_columns_names)
        success = new_column_name in target_columns_names
        if not success:
            print(column_name)
        return new_column_name, success
    else:
        if f'{column_name}_stu' in target_columns_names:
            new_column_name = f'{column_name}_stu'
            # validate
            #print('suffix clin', new_column_name in target_columns_names)
            success = new_column_name in target_columns_names
            if not success:
                print(column_name)
            return new_column_name, success
        else:
            
            words = column_name.split('_')
            words = words[:-1] + ['stu'] + words[-1:]
            new_column_name = '_'.join(words)
            # validate 
            #print('before last word -', new_column_name in target_columns_names)
            success = new_column_name in target_columns_names
            if not success:
                
                print(column_name)
            return new_column_name, success
        
def map_additional_column_name_to_2021_clinician_column_name(column_name, target_columns_names):
    if column_name in target_columns_names:
        #print('original column - ', column_name in target_columns_names)
        success = column_name in target_columns_names
        if not success:
            print(column_name)
        return column_name, success
    elif bool(re.search(r'__\d+$', column_name)):
        suffix = re.search(r'___\d+$', column_name)[0]
        new_column_name = column_name.replace(suffix, f'_clin{suffix}')
        # validate
        #print('before number suffix - ', new_column_name in target_columns_names)
        success = new_column_name in target_columns_names
        if not success:
            print(column_name)
        return new_column_name, success
    else:
        if f'{column_name}_clin' in target_columns_names:
            new_column_name = f'{column_name}_clin'
            # validate
            #print('suffix clin', new_column_name in target_columns_names)
            success = new_column_name in target_columns_names
            if not success:
                print(column_name)
            return new_column_name, success
        else:
            
            words = column_name.split('_')
            words = words[:-1] + ['clin'] + words[-1:]
            new_column_name = '_'.join(words)
            # validate 
            #print('before last word -', new_column_name in target_columns_names)
            success = new_column_name in target_columns_names
            if not success:
                print(column_name)
            return new_column_name, success
        
        
def remove_from_stu_columns(string):
      
    terms = ['wai_t', 'maris_y_scars', 'er','sdrs','cdrs','medhis','diet',
         'inclusion','exclusion','week', 'three_mon','six_mon','twelve_mon','c_ssrs_f', 'cssrs_f',
            'wai_immirisk', 'marisyscars']
    
    for term in terms:
        if string.startswith(term):
            return True
    col_names = ['opening_clinicians_complete', 'opening_therapist_battery_timestamp', 'time',
                'parents_safety_plan', 'safety_plan', 'safety_plan_changed', 'opening_therapist_battery_complete',
                'suicide_form_timestamp', 'suiciform_time', 'suicide_form_complete']
    
    for col in col_names:
        if string == col:
            return True 
    return False