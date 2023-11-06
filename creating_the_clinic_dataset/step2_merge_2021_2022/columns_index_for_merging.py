import pandas as pd

# c_ssrs_t_2weeks_1_clin - removed from columns_to_apply_default_merge_solution
# df = pd.read_csv('all_columns_list.csv').rename({'0': 'name'},axis=1)

df = pd.read_csv(r'C:\Users\nogur\Documents\DeppClinic\Data\helper_docs\intersection_columns_list.csv').rename({'0': 'name'},axis=1)
df_redundant = pd.read_csv(r'C:\Users\nogur\Documents\DeppClinic\Data\helper_docs\columns_to_apply_default_merge_solution.csv')

binary_1_2 = ['opening_psychothe', 'opening_medicine', 'chameleon_follow_stu', 'treatment_end_stu', 'chameleon_behavior_stu', 'chameleon_attempt_stu', 'chameleon_nssi_stu', 'chameleon_suicide_er_stu', 'chameleon_psychiatric_stu']

weird_text_columns = ['opening_psychothe_3', 'complaint_other', 'diagnosis_other', 'opening_medicine_3', 'treatment_end_2_stu', 'treatment_end_stu', 'emergency_stu',
'treatment_end_stu']



columns_dict = {
    'diagnosis_binary': df[(df['name'].str.startswith('diagnosis')) & (df['name'].str.contains(r'\d', regex=True))]['name'],
    'complaint_binary': df[(df['name'].str.startswith('complaint')) & (df['name'].str.contains(r'\d', regex=True))]['name'],
    'timestamp': df[df['name'].str.contains('timestamp')]['name'],
    'date': df[(df['name'].str.contains('date')) & (df['name'] != 'visit_date_stu')]['name'],
   
    'chameleon_all': ['chameleon_timestamp', 'chameleon_follow_stu', 'treatment_end_stu', 'treatment_end_2_stu', 'visit_date_stu', 'chameleon_ideation_stu', 'chameleon_behavior_stu', 'chameleon_attempt_stu', 'chameleon_nssi_stu', 'chameleon_suicide_er_stu', 'chameleon_suicide_er_date_stu', 'chameleon_suicide_er_date_2_stu', 'chameleon_suicide_er_date_3_stu', 'chameleon_psychiatric_stu', 'chameleon_psychiatric_date_stu', 'chameleon_psychiatric_date_2_stu', 'chameleon_psychiatric_date_3_stu', 'emergency_stu', 'chameleon_psychotherapy_stu', 'chameleon_psychotherapy_2_stu___1', 'chameleon_psychotherapy_2_stu___2', 'chameleon_psychotherapy_2_stu___3', 'chameleon_psychotherapy_2_stu___4', 'chameleon_psychotherapy_2_stu___5', 'chameleon_psychotherapy_2_stu___6', 'chameleon_psychotherapy_2_stu___7', 'chameleon_psychotherapy_other_stu', 'chameleon_medicine_stu', 'chameleon_medicine_2_stu___1', 'chameleon_medicine_2_stu___2', 'chameleon_medicine_2_stu___3', 'chameleon_medicine_2_stu___4', 'chameleon_medicine_2_stu___5', 'chameleon_medicine_other_stu', 'chameleon_notes_stu'],

    'chameleon_binary_0_1': ['chameleon_psychotherapy_2_stu___1', 'chameleon_psychotherapy_2_stu___2', 'chameleon_psychotherapy_2_stu___3', 'chameleon_psychotherapy_2_stu___4', 'chameleon_psychotherapy_2_stu___6', 'chameleon_psychotherapy_2_stu___7', 'chameleon_medicine_2_stu___1', 'chameleon_medicine_2_stu___2', 'chameleon_medicine_2_stu___4', 'chameleon_medicine_2_stu___5'],

    'chameleon_binary_1_2': ['chameleon_follow_stu', 'treatment_end_stu', 'chameleon_behavior_stu', 'chameleon_attempt_stu', 'chameleon_nssi_stu', 'chameleon_suicide_er_stu', 'chameleon_psychiatric_stu'],

    'chameleon_others':['chameleon_timestamp', 'treatment_end_2_stu', 'visit_date_stu', 'chameleon_suicide_er_date_stu', 'chameleon_suicide_er_date_2_stu', 'chameleon_suicide_er_date_3_stu', 'chameleon_psychiatric_date_stu', 'chameleon_psychiatric_date_2_stu', 'chameleon_psychiatric_date_3_stu', 'chameleon_psychotherapy_other_stu', 'chameleon_medicine_other_stu', 'chameleon_notes_stu'],

    'opening_psychothe_binary_0_1': ['opening_psychothe_2___1', 'opening_psychothe_2___2', 'opening_psychothe_2___3', 'opening_psychothe_2___4', 'opening_psychothe_2___5', 'opening_psychothe_2___6', 'opening_psychothe_2___7'],
    
    'opening_psychothe_binary_1_2': ['opening_psychothe'],
   
    'opening_medicine_binary_0_1': ['opening_medicine_2___1', 'opening_medicine_2___2', 'opening_medicine_2___3', 'opening_medicine_2___4', 'opening_medicine_2___5'],
    
    'opening_medicine_binary_1_2': ['opening_medicine'],

    'with_who_m': ['with_who_m___1', 'with_who_m___2', 'with_who_m___3', 'with_who_m___4', 'with_who_m___5', 'with_who_m___6', 'with_who_m___7'],
    
    'with_who_f': ['with_who_f___1', 'with_who_f___2', 'with_who_f___3', 'with_who_f___4', 'with_who_f___5', 'with_who_f___6', 'with_who_f___7'],

    
    'groups': ['group___1', 'group___2', 'group___3'],
    'record_id': ['record_id'],
    'age_child_pre': ['age_child_pre'],
    'duplicated_cols': list(df_redundant['column_name']),
    'visit_date_stu': ['visit_date_stu']
}

merging_functions_by_columns_set = {
    'visit_date_stu': max,

    'diagnosis_binary': max,
    'complaint_binary': max,
    'timestamp': min,
    'date': min,
    'groups': max,
    'age_child_pre': max,
    'record_id': 'take 2021',
    'chameleon_binary_0_1': max,
    'chameleon_binary_1_2': min, 
    'opening_psychothe_binary_0_1': max,
    'opening_psychothe_binary_1_2': min,
    'opening_medicine_binary_0_1': max, 
    'opening_medicine_binary_1_2': min,
    'with_who_m': max,
    'with_who_f': max,
    
    'duplicated_cols': 'take 2022',
        
}