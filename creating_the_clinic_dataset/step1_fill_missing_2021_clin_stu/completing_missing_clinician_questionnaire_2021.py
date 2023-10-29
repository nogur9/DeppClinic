import pandas as pd
import numpy as np
import re
import psycopg2



def fill_id(df):
    """
    This function takes a DataFrame as input, and fills out the empty 'id' values by matching them to the 'record_id' which isn't empty.

    Parameters:
        df (pandas DataFrame): The DataFrame to be cleaned.

    Returns:
        pandas DataFrame : The cleaned DataFrame.
    """
    df = df.copy()
    id_map = df.dropna(subset=['id']).groupby('record_id')['id'].first()
    id_map = {key: id_map[key] for key in id_map.keys()}
    df['id'] = df['record_id'].apply(lambda x: id_map[x])
    return df


def IsClinician(row):
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
        
        
def should_remove_from_stu_columns(string):
      
    terms = ['wai_t', 'maris_y_scars', 'er','sdrs','cdrs','medhis','diet',
         'inclusion','exclusion','week', 'three_mon','six_mon','twelve_mon','c_ssrs_f', 'cssrs_f',
            'wai_immirisk', 'marisyscars']
    
    for term in terms:
        if string.startswith(term):
            return True
    col_names = ['opening_clinicians_complete', 'opening_therapist_battery_timestamp', 'time',
                'parents_safety_plan', 'safety_plan', 'safety_plan_changed', 'opening_therapist_battery_complete',
                'suicide_form_timestamp', 'suiciform_time', 'suicide_form_complete', 'cgi_i']


    imputation_data_mini_columns = ['mini_kid_sum_timestamp', 'mini_class', 'mini_date', 'mini_interviewer',
                                    'mini_date_interview', 'mini_medication___1', 'mini_medication___2',
                                    'mini_medication___3', 'mini_medication___4', 'mini_medication___5',
                                    'mini_medicine_other', 'mini_start_time', 'mini_end_time', 'mini_total_time',
                                    'depres___1', 'depres___2', 'depres___3', 'suicide___1', 'suicide___2',
                                    'suicide_risk', 'dysthemia___1', 'manic___1', 'manic___2', 'hypomania___1',
                                    'hypomania___2', 'bipolar_i___1', 'bipolar_i___2', 'bipolar_ii___1',
                                    'bipolar_ii___2', 'bipolar_unclassified___1', 'bipolar_unclassified___2',
                                    'panic___1', 'panic___2', 'agoraphobia___1', 'separation_anxiety___1',
                                    'social_anxiety___1', 'social_anxiety___2', 'social_anxiety___3', 'phobia___1',
                                    'ocd___1', 'ptsd___1', 'alcohol_depend___1', 'alcohol_use___1', 'drug_depend___1',
                                    'drug_use___1', 'tourette___1', 'motor_tics___1', 'vocal_tics___1',
                                    'transient_tics___1', 'adhd_mix___1', 'adhd_attention___1', 'adhd_hyper___1',
                                    'conduct___1', 'odd___1', 'psychotic___1', 'psychotic___2', 'affect_psychotic___1',
                                    'affect_psychotic___2', 'anorexia___1', 'bulimia___1', 'anorexia_bulmus___1',
                                    'gad___1', 'adjustment___1', 'organic', 'development___1', 'main_dianose',
                                    'mini_kid_sum_complete']

    if string in  col_names + imputation_data_mini_columns:
            return True

    return False


def upload_to_old_data_column_names_map(conn_str, questionnaire, old_2_redcap_map):

    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()

    cur.execute("""UPDATE  auxiliary_questionnaires_data.questionnaires_columns_names
    SET old_data_column_names_map = '{0}'
    WHERE questionnaire_name = {1};""".format(repr(old_2_redcap_map).replace("'", "\""), questionnaire))

    # Make the changes to the database persistent
    conn.commit()

    # Close cursor and communication with the database
    cur.close()
    conn.close()


def upload_to_imputation_data_to_old_data_map(conn_str, questionnaire, imputation_2_old_map):
    conn = psycopg2.connect(conn_str, questionnaire)
    cur = conn.cursor()

    cur.execute("""UPDATE  auxiliary_questionnaires_data.old_data_questionnaires_columns_names
    SET imputation_data_to_old_data_map = '{0}'
    WHERE questionnaire_name = {1};""".format(repr(imputation_2_old_map).replace("'", "\""), questionnaire))

    # Make the changes to the database persistent
    conn.commit()

    # Close cursor and communication with the database
    cur.close()
    conn.close()

