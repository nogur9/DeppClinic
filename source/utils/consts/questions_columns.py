basic_info_columns = ['gender', 'redcap_event_name', 'age_child_pre']

c_ssrs_intake = [
    'c_ssrs_1_life',
    'c_ssrs_2_life',
    'c_ssrs_3_life',
    'c_ssrs_4_life',
    'c_ssrs_5_life',
    'c_ssrs_6_life',
    'c_ssrs_1_2weeks',
    'c_ssrs_2_2weeks',
    'c_ssrs_3_2weeks',
    'c_ssrs_4_2weeks',
    'c_ssrs_5_2weeks',
    'c_ssrs_6_2weeks',
    'c_ssrs_6_3month',
    'c_ssrs_7_intake',
    'c_ssrs_8_intake'
]

c_ssrs = [
    'c_ssrs_1',
    'c_ssrs_2',
    'c_ssrs_3',
    'c_ssrs_4',
    'c_ssrs_5',
    'c_ssrs_6',
    'c_ssrs_last_visit_6',
    'c_ssrs_7',
    'c_ssrs_8',
]

c_ssrs_clin = [  # 'c_ssrs_t_time_clin',  # what's that?#
    #'c_ssrs_t_2weeks_1_clin',
    'c_ssrs_t_2weeks_2_clin',
    'c_ssrs_t_2weeks_3_clin',
    'c_ssrs_t_2weeks_4_clin',
    'c_ssrs_t_2weeks_5_clin',
    'c_ssrs_t_last_1_clin',
    'c_ssrs_t_last_2_clin',
    'c_ssrs_t_last_3_clin',
    'c_ssrs_t_last_4_clin',
    'c_ssrs_t_last_5_clin',
    'c_ssrs_t_life_1_clin',
    'c_ssrs_t_life_2_clin',
    'c_ssrs_t_life_3_clin',
    'c_ssrs_t_life_4_clin',
    'c_ssrs_t_life_5_clin',
    'c_ssrs_t_6_clin',
    'c_ssrs_t_7_clin',
    'c_ssrs_t_8_clin',
    'c_ssrs_t_9_clin',
    'c_ssrs_t_10_clin',
    'c_ssrs_t_6_clin_2',
    'c_ssrs_t_7_clin_2',
    'c_ssrs_t_8_clin_2',
    'c_ssrs_t_9_clin_2',
    'c_ssrs_t_10_clin_2',
    'c_ssrs_t_11_2weeks_clin',
    'c_ssrs_t_12_2weeks_clin',
    'c_ssrs_t_13_2weeks_clin',
    'c_ssrs_t_14_2weeks_clin',
    'c_ssrs_t_15_2weeks_clin',
    'c_ssrs_t_16_2weeks_clin',
    'suicidal_behavior_last_11_clin',
    'suicidal_behavior_last_12_clin',
    'suicidal_behavior_last_13_clin',
    'suicidal_behavior_last_14_clin',
    'suicidal_behavior_last_15_clin',
    'suicidal_behavior_last_16_clin',
    'suicidal_behavior_last_17_clin',
    'suicidal_behavior_last_11_clin_1',
    'suicidal_behavior_last_12_clin_1',
    'suicidal_behavior_last_13_clin_1',
    'suicidal_behavior_last_18_clin',
    'suicidal_behavior_last_19_clin',
    'c_ssrs_t_11_life_clin',
    'c_ssrs_t_12_life_clin',
    'c_ssrs_t_13_life_clin',
    'c_ssrs_t_14_life_clin',
    'c_ssrs_t_15_life_clin',
    'c_ssrs_t_16_life_clin',
    'c_ssrs_t_17_life_clin',
    'c_ssrs_t_11_life_clin_1',
    'c_ssrs_t_12_life_clin_1',
    'c_ssrs_t_13_life_clin_1',
    'c_ssrs_t_18_life_clin',
    'c_ssrs_t_19_life_clin'
]

c_ssrs_stu = [
    'c_ssrs_t_2weeks_1_stu',
    'c_ssrs_t_2weeks_2_stu',
    'c_ssrs_t_2weeks_3_stu',
    'c_ssrs_t_2weeks_4_stu',
    'c_ssrs_t_2weeks_5_stu',
    'c_ssrs_t_last_1_stu',
    'c_ssrs_t_last_2_stu',
    'c_ssrs_t_last_3_stu',
    'c_ssrs_t_last_4_stu',
    'c_ssrs_t_last_5_stu',
    'c_ssrs_t_life_1_stu',
    'c_ssrs_t_life_2_stu',
    'c_ssrs_t_life_3_stu',
    'c_ssrs_t_life_4_stu',
    'c_ssrs_t_life_5_stu',
    'c_ssrs_t_6_stu',
    'c_ssrs_t_7_stu',
    'c_ssrs_t_8_stu',
    'c_ssrs_t_9_stu',
    'c_ssrs_t_10_stu',
    'c_ssrs_t_6_stu_2',
    'c_ssrs_t_7_stu_2',
    'c_ssrs_t_8_stu_2',
    'c_ssrs_t_9_stu_2',
    'c_ssrs_t_10_stu_2',
    'c_ssrs_t_11_2weeks_stu',
    'c_ssrs_t_12_2weeks_stu',
    'c_ssrs_t_13_2weeks_stu',
    'c_ssrs_t_14_2weeks_stu',
    'c_ssrs_t_15_2weeks_stu',
    'c_ssrs_t_16_2weeks_stu',
    'suicidal_behavior_last_11_stu',
    'suicidal_behavior_last_12_stu',
    'suicidal_behavior_last_13_stu',
    'suicidal_behavior_last_14_stu',
    'suicidal_behavior_last_15_stu',
    'suicidal_behavior_last_16_stu',
    'suicidal_behavior_last_17_stu',
    'suicidal_behavior_last_11_stu_1',
    'suicidal_behavior_last_12_stu_1',
    'suicidal_behavior_last_13_stu_1',
    'suicidal_behavior_last_18_stu',
    'suicidal_behavior_last_19_stu',
    'c_ssrs_t_11_life_stu',
    'c_ssrs_t_12_life_stu',
    'c_ssrs_t_13_life_stu',
    'c_ssrs_t_14_life_stu',
    'c_ssrs_t_15_life_stu',
    'c_ssrs_t_16_life_stu',
    'c_ssrs_t_17_life_stu',
    'c_ssrs_t_11_life_stu_1',
    'c_ssrs_t_12_life_stu_1',
    'c_ssrs_t_13_life_stu_1',
    'c_ssrs_t_18_life_stu',
    'c_ssrs_t_19_life_stu']

mfq = [
    'mfq_1',
    'mfq_2',
    'mfq_5',
    'mfq_7',
    'mfq_8',
    'mfq_14',
    'mfq_21',
    'mfq_23',
    'mfq_24',
    'mfq_27',
    'mfq_28',
    'mfq_30',
    'mfq_31']

additional_mfq = [
    'mfq_34',
    'mfq_35',
    'mfq_36',
    'mfq_37'
]

siq = [
    'siq_1',
    'siq_2',
    'siq_3',
    'siq_4',
    'siq_5',
    'siq_6',
    'siq_7',
    'siq_8',
    'siq_9',
    'siq_10',
    'siq_11',
    'siq_12',
    'siq_13',
    'siq_14',
    'siq_15'
]

sdq = [
    'sdq_1',
    'sdq_2',
    'sdq_3',
    'sdq_4',
    'sdq_5',
    'sdq_6',
    'sdq_7',
    'sdq_8',
    'sdq_9',
    'sdq_10',
    'sdq_11',
    'sdq_12',
    'sdq_13',
    'sdq_14',
    'sdq_15',
    'sdq_16',
    'sdq_17',
    'sdq_18',
    'sdq_19',
    'sdq_20',
    'sdq_21',
    'sdq_22',
    'sdq_23',
    'sdq_24',
    'sdq_25'
]

scared = [
    'scared_1',
    'scared_2',
    'scared_3',
    'scared_4',
    'scared_5',
    'scared_6',
    'scared_7',
    'scared_8',
    'scared_9',
    'scared_10',
    'scared_11',
    'scared_12',
    'scared_13',
    'scared_14',
    'scared_15',
    'scared_16',
    'scared_17',
    'scared_18',
    'scared_19',
    'scared_20',
    'scared_21',
    'scared_22',
    'scared_23',
    'scared_24',
    'scared_25',
    'scared_26',
    'scared_27',
    'scared_28',
    'scared_29',
    'scared_30',
    'scared_31',
    'scared_32',
    'scared_33',
    'scared_34',
    'scared_35',
    'scared_36',
    'scared_37',
    'scared_38',
    'scared_39',
    'scared_40',
    'scared_41'
]

ATHENS = [
    'athens_1',
    'athens_2',
    'athens_3',
    'athens_4',
    'athens_5',
    'athens_6',
    'athens_7',
    'athens_8'
]

SAS = [
    'sas_1',
    'sas_2',
    'sas_3',
    'sas_4',
    'sas_5',
    'sas_6',
    'sas_7',
    'sas_8',
    'sas_9',
    'sas_10',
    'sas_11',
    'sas_12',
    'sas_13',
    'sas_14',
    'sas_15',
    'sas_16',
    'sas_17',
    'sas_18',
    'sas_19',
    'sas_20',
    'sas_21',
    'sas_22',
    'sas_23'
]

sci_af_ca = [
    'sci_af_ca_1',
    'sci_af_ca_2',
    'sci_af_ca_3',
    'sci_af_ca_4',
    'sci_af_ca_5',
    'sci_af_ca_6',
    'sci_af_ca_7',
    'sci_af_ca_8',
    'sci_af_ca_9',
    'sci_af_ca_10',
    'sci_af_ca_11',
    'sci_af_ca_12',
    'sci_af_ca_13',
    'sci_af_ca_14',
    'sci_af_ca_15',
    'sci_af_ca_16',
    'sci_af_ca_17',
    'sci_af_ca_18',
    'sci_af_ca_19',
    'sci_af_ca_20',
    'sci_af_ca_21',
    'sci_af_ca_22',
    'sci_af_ca_23',
    'sci_af_ca_24',
    'sci_af_ca_25',
    'sci_af_ca_26',
    'sci_af_ca_27',
    'sci_af_ca_28',
    'sci_af_ca_29',
    'sci_af_ca_30',
    'sci_af_ca_31',
    'sci_af_ca_32',
    'sci_af_ca_33',
    'sci_af_ca_34',
    'sci_af_ca_35',
    'sci_af_ca_36',
    'sci_af_ca_37',
    'sci_af_ca_38',
    'sci_af_ca_39',
    'sci_af_ca_40'
]

scs_clin = [
    'sci_c_1_1_clin',
    'scs_2_1_clin',
    'scs_2_2_clin',
    'scs_2_3_clin',
    'scs_2_4_clin',
    'sci_c_3_1_clin',
    'sci_c_3_2_clin',
    'sci_c_3_3_clin',
    'sci_c_3_4_clin',
    'sci_c_4_1_clin',
    'sci_c_4_2_clin',
    'sci_c_4_3_clin',
    'sci_c_4_4_clin',
    'sci_c_5_1_clin',
    'sci_c_5_2_clin'
]

scs_stu = [
    'sci_c_1_1_stu',
    'scs_2_1_stu',
    'scs_2_2_stu',
    'scs_2_3_stu',
    'scs_2_4_stu',
    'sci_c_3_1_stu',
    'sci_c_3_2_stu',
    'sci_c_3_3_stu',
    'sci_c_3_4_stu',
    'sci_c_4_1_stu',
    'sci_c_4_2_stu',
    'sci_c_4_3_stu',
    'sci_c_4_4_stu',
    'sci_c_5_1_stu',
    'sci_c_5_2_stu'
]

sci_mother = [
    'sci_p_1_m',
    'sci_p_2_m',
    'sci_p_3_m',
    'sci_p_4_m',
    'sci_p_5_m',
    'sci_p_6_m',
    'sci_p_7_m',
    'sci_p_8_m',
    'sci_p_9_m',
    'sci_p_10_m',
    'sci_p_11_m',
    'sci_p_12_m',
    'sci_p_13_m',
    'sci_p_14_m',
    'sci_p_15_m'
]

sci_father = [
    'sci_p_1_f',
    'sci_p_2_f',
    'sci_p_3_f',
    'sci_p_4_f',
    'sci_p_5_f',
    'sci_p_6_f',
    'sci_p_7_f',
    'sci_p_8_f',
    'sci_p_9_f',
    'sci_p_10_f',
    'sci_p_11_f',
    'sci_p_12_f',
    'sci_p_13_f',
    'sci_p_14_f',
    'sci_p_15_f'
]

ARI_S = ['ari_s_1', 'ari_s_2', 'ari_s_3', 'ari_s_4', 'ari_s_5', 'ari_s_6', 'ari_s_7']

ARI_P_m = ['ari_p_1_m', 'ari_p_2_m', 'ari_p_3_m', 'ari_p_4_m', 'ari_p_5_m', 'ari_p_6_m']

ARI_P_f = ['ari_p_1_f', 'ari_p_2_f', 'ari_p_3_f', 'ari_p_4_f', 'ari_p_5_f', 'ari_p_6_f']

MAST = ['mast_1',
         'mast_5',
         'mast_6',
         'mast_13',
         'mast_18',
         'mast_19',
         'mast_25',
         'mast_28',
         'mast_2',
         'mast_9',
         'mast_14',
         'mast_15',
         'mast_16',
         'mast_21',
         'mast_30',
         'mast_8',
         'mast_17',
         'mast_22',
         'mast_23',
         'mast_26',
         'mast_27',
         'mast_29',
         'mast_3',
         'mast_4',
         'mast_7',
         'mast_10',
         'mast_11',
         'mast_12',
         'mast_20',
         'mast_24']

maris_sci_sf = ['maris_sci_sf_1', 'maris_sci_sf_2', 'maris_sci_sf_3', 'maris_sci_sf_4',
                'maris_sci_sf_5', 'maris_sci_sf_6', 'maris_sci_sf_7', 'maris_sci_sf_8',
                'maris_sci_sf_9']

maris_soq_sf = ['maris_soq_sf_1', 'maris_soq_sf_2', 'maris_soq_sf_3', 'maris_soq_sf_4',
                'maris_soq_sf_5', 'maris_soq_sf_6', 'maris_soq_sf_7', 'maris_soq_sf_8']

demographics_f = ['parents_born_f',
                  'parents_born_2_f',
                  'born_child_f',
                  'born_child_2_f',
                  'parent_religion_f',
                  'parent_religion_other_f',
                  'parents_economy_f',
                  'parents_education_f',
                  'parents_education_other_f',
                  'parents_work_f',
                  'paresnts_work_2_f',
                  'together_live_f']

demographics_m = [
    'parents_born_m',
    'parents_born_2_m',
    'born_child_m',
    'born_child_2_m',
    'parent_religion_m',
    'parent_religion_other_m',
    'parents_economy_m',
    'parents_education_m',
    'parents_education_other_m',
    'parents_work_m',
    'paresnts_work_2_m',
    'together_live_m',
]

swan_m = [
    "swan_1_m",
    "swan_2_m",
    "swan_3_m",
    "swan_4_m",
    "swan_5_m",
    "swan_6_m",
    "swan_7_m",
    "swan_8_m",
    "swan_9_m",
    "swan_10_m",
    "swan_11_m",
    "swan_12_m",
    "swan_13_m",
    "swan_14_m",
    "swan_15_m",
    "swan_16_m",
    "swan_17_m",
    "swan_18_m"
]

swan_f = [
    "s-wan_1_f",
    "swan_2_f",
    "swan_3_f",
    "swan_4_f",
    "swan_5_f",
    "swan_6_f",
    "swan_7_f",
    "swan_8_f",
    "swan_9_f",
    "swan_10_f",
    "swan_11_f",
    "swan_12_f",
    "swan_13_f",
    "swan_14_f",
    "swan_15_f",
    "swan_16_f",
    "swan_17_f",
    "swan_18_f"
]

dass_m = [
    'dass_1_m',
    'dass_2_m',
    'dass_3_m',
    'dass_4_m',
    'dass_5_m',
    'dass_6_m',
    'dass_7_m',
    'dass_8_m',
    'dass_9_m',
    'dass_10_m',
    'dass_11_m',
    'dass_12_m',
    'dass_13_m',
    'dass_14_m',
    'dass_15_m',
    'dass_16_m',
    'dass_17_m',
    'dass_18_m',
    'dass_19_m',
    'dass_20_m',
    'dass_21_m'
]

dass_f = [
    'dass_1_f',
    'dass_2_f',
    'dass_3_f',
    'dass_4_f',
    'dass_5_f',
    'dass_6_f',
    'dass_7_f',
    'dass_8_f',
    'dass_9_f',
    'dass_10_f',
    'dass_11_f',
    'dass_12_f',
    'dass_13_f',
    'dass_14_f',
    'dass_15_f',
    'dass_16_f',
    'dass_17_f',
    'dass_18_f',
    'dass_19_f',
    'dass_20_f',
    'dass_21_f'
]

ecr_f = [
    'ecr_1_f',
    'ecr_2_f',
    'ecr_3_f',
    'ecr_4_f',
    'ecr_5_f',
    'ecr_6_f',
    'ecr_7_f',
    'ecr_8_f',
    'ecr_9_f',
    'ecr_10_f',
    'ecr_11_f',
    'ecr_12_f',
    'ecr_13_f',
    'ecr_14_f',
    'ecr_15_f',
    'ecr_16_f',
    'ecr_17_f',
    'ecr_18_f',
    'ecr_19_f',
    'ecr_20_f',
    'ecr_21_f',
    'ecr_22_f',
    'ecr_23_f',
    'ecr_24_f',
    'ecr_25_f',
    'ecr_26_f',
    'ecr_27_f',
    'ecr_28_f',
    'ecr_29_f',
    'ecr_30_f',
    'ecr_31_f',
    'ecr_32_f',
    'ecr_33_f',
    'ecr_34_f',
    'ecr_35_f',
    'ecr_36_f']

ecr_m = [
    'ecr_1_m',
    'ecr_2_m',
    'ecr_3_m',
    'ecr_4_m',
    'ecr_5_m',
    'ecr_6_m',
    'ecr_7_m',
    'ecr_8_m',
    'ecr_9_m',
    'ecr_10_m',
    'ecr_11_m',
    'ecr_12_m',
    'ecr_13_m',
    'ecr_14_m',
    'ecr_15_m',
    'ecr_16_m',
    'ecr_17_m',
    'ecr_18_m',
    'ecr_19_m',
    'ecr_20_m',
    'ecr_21_m',
    'ecr_22_m',
    'ecr_23_m',
    'ecr_24_m',
    'ecr_25_m',
    'ecr_26_m',
    'ecr_27_m',
    'ecr_28_m',
    'ecr_29_m',
    'ecr_30_m',
    'ecr_31_m',
    'ecr_32_m',
    'ecr_33_m',
    'ecr_34_m',
    'ecr_35_m',
    'ecr_36_m']

trq_sf_maris_clin = [
    'trq_sf_maris_1_clin',
    'trq_sf_maris_2_clin',
    'trq_sf_maris_3_clin',
    'trq_sf_maris_4_clin',
    'trq_sf_maris_5_clin',
    'trq_sf_maris_6_clin',
    'trq_sf_maris_7_clin',
    'trq_sf_maris_8_clin',
    'trq_sf_maris_9_clin',
    'trq_sf_maris_10_clin',
    'trq_sf_maris_11_clin',
    'trq_sf_maris_12_clin',
    'trq_sf_maris_13_clin',
    'trq_sf_maris_14_clin'
]

screening_form = [
    'screen_1',
    'screen_2',
    'screen_3',
    'screen_10',
    'screen_11',
    'screen_12',
    'screen_13',
    'screen_14',
    'screen_15',
    'screen_16',
    'screen_17',
    'screen_18',
    'screen_23',
    'screen_24',
    'screen_25',
    'screen_26',
    'screen_27',
    'screen_28',
    'screen_29',
    'screen_30',
    'screen_31',
    'screen_32',
    'screen_33',
    'screen_35',
    'screen_35_1',
    'screen_36',
    'screen_36_1',
    'screen_37',
    'screen_37_1',
    'screen_38',
    'screen_38_1',
    'screen_39',
    'screen_39_1'
]

c_ssrs_fu_maya = [
    'c_ssrs_fu_thought_1_clin',
    'c_ssrs_fu_thought_2_clin',
    'c_ssrs_fu_thought_3_clin',
    'c_ssrs_fu_thought_4_clin',
    'c_ssrs_fu_thought_5_clin',
    'c_ssrs_fu_intensity_clin',
    'c_ssrs_fu_frequ_clin',
    'c_ssrs_fu_lengh_clin',
    'c_ssrs_fu_control_clin',
    'c_ssrs_fu_deter_clin',
    'c_ssrs_fu_reason_clin',
    'c_ssrs_fu_attemp_clin',
    'c_ssrs_fu_attemp_2_3_clin',
    'c_ssrs_fu_attemp_3_clin',
    'c_ssrs_fu_attemp_4_clin',
    'c_ssrs_fu_attemp_4_2_clin',
    'c_ssrs_fu_attemp_4_3_clin',
    'c_ssrs_fu_attemp_5_clin',
    'c_ssrs_fu_attemp_5_2_clin',
    'c_ssrs_fu_attemp_5_3_clin',
    'c_ssrs_fu_attemp_6_clin',
    'c_ssrs_fu_attemp_6_2_clin',
    'c_ssrs_fu_attemp_7_clin',
    'c_ssrs_fu_attemp_8_clin',
    'c_ssrs_fu_done_clin',
    'c_ssrs_fu_done_2_clin'
]

DERS = [
    'ders_1', 'ders_2', 'ders_3', 'ders_4', 'ders_5', 'ders_6', 'ders_7', 'ders_8', 'ders_9', 'ders_10',
    'ders_11', 'ders_12', 'ders_13', 'ders_14', 'ders_15', 'ders_16', 'ders_17', 'ders_18', 'ders_19',
    'ders_20', 'ders_21', 'ders_22', 'ders_23', 'ders_24', 'ders_25', 'ders_26', 'ders_27', 'ders_28',
    'ders_29', 'ders_30', 'ders_31', 'ders_32', 'ders_33','ders_34', 'ders_35', 'ders_36'
]

wai = ['wai_1', 'wai_2', 'wai_3', 'wai_4',
       'wai_5', 'wai_6', 'wai_7', 'wai_8',
       'wai_9', 'wai_10', 'wai_11', 'wai_12']

erc_rc = [
    'erc_rc_1', 'erc_rc_2', 'erc_rc_3',
    'erc_rc_4', 'erc_rc_5', 'erc_rc_6',
    'erc_rc_7', 'erc_rc_8', 'erc_rc_9',
    'erc_rc_10', 'erc_rc_11', 'erc_rc_12']

bulling = [
    'cyberbulling_1',
    'cyberbulling_2',
    'cyberbulling_3',
    'cyberbulling_4',
    'cyberbulling_5',
    'cyberbulling_6',
    'cyberbulling_7',
    'cyberbulling_8',
    'cyberbulling_9',
    'cyberbulling_10',
    'cyberbulling_11',
    'bullied_1',
    'bullied_2',
    'bullied_3',
    'bullied_4'
]

opening = [
    'complaint___1',
    'complaint___2',
    'complaint___3',
    'complaint___4',
    'complaint___5',
    'complaint___6',
    'complaint_other',
    'diagnosis___1',
    'diagnosis___2',
    'diagnosis___3',
    'diagnosis___4',
    'diagnosis___5',
    'diagnosis___6',
    'diagnosis___7',
    'diagnosis___8',
    'diagnosis___9',
    'diagnosis___10',
    'diagnosis___11',
    'diagnosis___12',
    'diagnosis___13',
    'diagnosis___14',
    'diagnosis_other',
    'opening_psychothe',
    'opening_psychothe_2___1',
    'opening_psychothe_2___2',
    'opening_psychothe_2___3',
    'opening_psychothe_2___4',
    'opening_psychothe_2___5',
    'opening_psychothe_2___6',
    'opening_psychothe_2___7',
    'opening_psychothe_3',
    'opening_medicine',
    'opening_medicine_2___1',
    'opening_medicine_2___2',
    'opening_medicine_2___3',
    'opening_medicine_2___4',
    'opening_medicine_2___5',
    'opening_medicine_3'
]

chameleon_all = ['chameleon_follow_stu',
             'treatment_end_stu',
             'treatment_end_2_stu',
             'visit_date_stu',
             'chameleon_ideation_stu',
             'chameleon_behavior_stu',
             'chameleon_attempt_stu',
             'chameleon_nssi_stu',
             'chameleon_suicide_er_stu',
             'chameleon_suicide_er_date_stu',
             'chameleon_suicide_er_date_2_stu',
             'chameleon_suicide_er_date_3_stu',
             'chameleon_psychiatric_stu',
             'chameleon_psychiatric_date_stu',
             'chameleon_psychiatric_date_2_stu',
             'chameleon_psychiatric_date_3_stu',
             'emergency_stu',
             'chameleon_psychotherapy_stu',
             'chameleon_psychotherapy_2_stu___1',
             'chameleon_psychotherapy_2_stu___2',
             'chameleon_psychotherapy_2_stu___3',
             'chameleon_psychotherapy_2_stu___4',
             'chameleon_psychotherapy_2_stu___5',
             'chameleon_psychotherapy_2_stu___6',
             'chameleon_psychotherapy_2_stu___7',
             'chameleon_psychotherapy_other_stu',
             'chameleon_medicine_stu',
             'chameleon_medicine_2_stu___1',
             'chameleon_medicine_2_stu___2',
             'chameleon_medicine_2_stu___3',
             'chameleon_medicine_2_stu___4',
             'chameleon_medicine_2_stu___5',
             'chameleon_medicine_other_stu',
             'chameleon_notes_stu'
]

chameleon = ['chameleon_follow_stu',
             'treatment_end_stu',
             'chameleon_ideation_stu',
             'chameleon_behavior_stu',
             'chameleon_attempt_stu',
             'chameleon_nssi_stu',
             'chameleon_suicide_er_stu',
             'chameleon_psychiatric_stu',
             'emergency_stu',
             'chameleon_psychotherapy_stu',
             'chameleon_psychotherapy_2_stu___1',
             'chameleon_psychotherapy_2_stu___2',
             'chameleon_psychotherapy_2_stu___3',
             'chameleon_psychotherapy_2_stu___4',
             'chameleon_psychotherapy_2_stu___5',
             'chameleon_psychotherapy_2_stu___6',
             'chameleon_psychotherapy_2_stu___7',
             'chameleon_medicine_stu',
             'chameleon_medicine_2_stu___1',
             'chameleon_medicine_2_stu___2',
             'chameleon_medicine_2_stu___3',
             'chameleon_medicine_2_stu___4',
             'chameleon_medicine_2_stu___5',
]

cgi = ['cgi_s_clin']

piu_cyberbulling = ['piu_1', 'piu_2', 'piu_3', 'piu_4', 'piu_5', 'piu_6',
                    'cyberbulling_1', 'cyberbulling_2',	'cyberbulling_3', 'cyberbulling_4',
                    'cyberbulling_5', 'cyberbulling_6', 'cyberbulling_7', 'cyberbulling_8',
                    'cyberbulling_9', 'cyberbulling_10', 'cyberbulling_11',
                    'bullied_1', 'bullied_2', 'bullied_3', 'bullied_4']

erq_ca = ['erq_ca_1', 'erq_ca_2', 'erq_ca_3', 'erq_ca_4', 'erq_ca_5',
          'erq_ca_6', 'erq_ca_7', 'erq_ca_8', 'erq_ca_9', 'erq_ca_10']

cts = ['cts_c_1', 'cts_c_2', 'cts_c_3', 'cts_c_4', 'cts_c_4_1']

dshi_pre = ['dshi_pre_1', 'dshi_pre_2', 'dshi_pre_3', 'dshi_pre_4', 'dshi_pre_5', 'dshi_pre_6']

dshi_post = ['dshi_post_1', 'dshi_post_2', 'dshi_post_3', 'dshi_post_4', 'dshi_post_5', 'dshi_post_6']

inq = ['inq_1', 'inq_2', 'inq_3', 'inq_4', 'inq_5', 'inq_6', 'inq_7', 'inq_8',
       'inq_9', 'inq_10', 'inq_11', 'inq_12', 'inq_13', 'inq_14', 'inq_15']


all_of_the_questionnaires = c_ssrs_intake + c_ssrs + \
                            c_ssrs_clin + \
                            mfq + \
                            additional_mfq + \
                            siq + \
                            sdq + \
                            scared + \
                            ATHENS + \
                            SAS + \
                            sci_af_ca + \
                            scs_clin + \
                            sci_mother + \
                            ARI_S + \
                            ARI_P_m + \
                            MAST + \
                            maris_sci_sf + \
                            maris_soq_sf + \
                            demographics_m + \
                            swan_m + \
                            dass_m + \
                            ecr_m + \
                            trq_sf_maris_clin + \
                            screening_form + \
                            DERS + \
                            wai + \
                            erc_rc + \
                            bulling + \
                            opening + \
                            chameleon + \
                            cgi + \
                            piu_cyberbulling + \
                            erq_ca + \
                            cts + \
                            dshi_pre + \
                            dshi_post + \
                            inq

