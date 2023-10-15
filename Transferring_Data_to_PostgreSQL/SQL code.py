CREATE SCHEMA auxiliary_questionnaires_data

CREATE TABLE auxiliary_questionnaires_data.questionnaires_columns_names (
  questionnaire_name text NOT NULL,
  column_names text[], -- this is an array column
  old_data_column_names jsonb -- this is a jsonb column
  imputation_data_column_names jsonb -- this is a jsonb column
  reverse_questions text[] -- this is an array column

);


-- Inserting Questionnaires values:

INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('c_ssrs_intake',
	ARRAY['cssrs_intake_timestamp',
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
    'c_ssrs_8_intake']
);

INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('c_ssrs',
	ARRAY['cssrs_timestamp',
	'c_ssrs_1',
    'c_ssrs_2',
    'c_ssrs_3',
    'c_ssrs_4',
    'c_ssrs_5',
    'c_ssrs_6',
    'c_ssrs_last_visit_6',
    'c_ssrs_7',
    'c_ssrs_8']
);

INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('c_ssrs_clin',
	ARRAY[
	'cssrs_t_clin_timestamp',
	'c_ssrs_t_time_clin',
    'c_ssrs_t_2weeks_1_clin',
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
);

INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('c_ssrs_stu',
	ARRAY[
'cssrs_t_stu_timestamp',
    'c_ssrs_t_time_stu',
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
);


INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('mfq',
	ARRAY[
	'mfq_short_timestamp',
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
    'mfq_31',
	'mfq_34',
    'mfq_35',
    'mfq_36',
    'mfq_37'
	]
);



INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('siq',
	ARRAY[
	'siq_timestamp',
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
);

INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('sdq',
	ARRAY[
	'sdq_timestamp',
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
    'sdq_25'	]
);


INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('scared',
	ARRAY[
	'scared_timestamp',
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
    'scared_41']
);


INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ATHENS',
	ARRAY[
    'athens_1',
    'athens_2',
    'athens_3',
    'athens_4',
    'athens_5',
    'athens_6',
    'athens_7',
    'athens_8'
	]
);


INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('SAS',
	ARRAY[
	'sas_timestamp',
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
);


INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('sci_af_ca',
	ARRAY[
	'sciafca_timestamp',
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
);


INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('scs_clin',
	ARRAY[
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
);


INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('scs_stu',
	ARRAY[
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
);


INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('sci_mother',
	ARRAY[
	'scip_m_timestamp',
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
);



INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('sci_father',
	ARRAY[
	'scip_f_timestamp',
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
);







INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('mast',
	ARRAY[
		'immirisk_adolescents_mast_athens_timestamp',
		'age',
		'mast_1',
		'mast_2',
		'mast_3',
		'mast_4',
		'mast_5',
		'mast_6',
		'mast_7',
		'mast_8',
		'mast_9',
		'mast_10',
		'mast_11',
		'mast_12',
		'mast_13',
		'mast_14',
		'mast_15',
		'mast_16',
		'mast_17',
		'mast_18',
		'mast_19',
		'mast_20',
		'mast_21',
		'mast_22',
		'mast_23',
		'mast_24',
		'mast_25',
		'mast_26',
		'mast_27',
		'mast_28',
		'mast_29',
		'mast_30'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('maris_sci_sf',
	ARRAY[
		'marisscisf_timestamp',
		'age_child'
		'maris_sci_sf_1',
		'maris_sci_sf_2',
		'maris_sci_sf_3',
		'maris_sci_sf_4',
		'maris_sci_sf_5',
		'maris_sci_sf_6',
		'maris_sci_sf_7',
		'maris_sci_sf_8',
        'maris_sci_sf_9'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('maris_soq_sf',
	ARRAY[
		'marissoqsf_timestamp',
		'maris_soq_sf_1',
		'maris_soq_sf_2',
		'maris_soq_sf_3',
		'maris_soq_sf_4',
        'maris_soq_sf_5',
		'maris_soq_sf_6',
		'maris_soq_sf_7',
		'maris_soq_sf_8'
	]
);



INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ARI_P',
	ARRAY[
		'arippps_m_timestamp',
		'ari_p_1',
		'ari_p_2',
		'ari_p_3',
		'ari_p_4',
		'ari_p_5',
		'ari_p_6',
		'ari_p_7_m',
		'pps_1_m',
		'pps_2_m'

	]
);


INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ARI_S',
	ARRAY[
		'aris_timestamp',
		'ari_s_1',
		'ari_s_2',
		'ari_s_3',
		'ari_s_4',
		'ari_s_5',
		'ari_s_6',
		'ari_s_7'
	]
);



INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('demographics_f',
	ARRAY[
		'demographic_parents_f_timestamp',
		'parents_who_f',
		'parent_who_other_f',
		'parents_age_f',
		'parents_born_f',
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
		'together_live_f',
		'with_who_f___1',
		'with_who_f___2',
		'with_who_f___3',
		'with_who_f___4',
		'with_who_f___5',
		'with_who_f___6',
		'with_who_f___7',
		'with_who_other_f'
	]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('demographics_m',
	ARRAY[
		'demographic_parents_m_timestamp',
		'parents_who_m',
		'parent_who_other_m',
		'parents_age_m',
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
		'with_who_m___1',
		'with_who_m___2',
		'with_who_m___3',
		'with_who_m___4',
		'with_who_m___5',
		'with_who_m___6',
		'with_who_m___7',
		'with_who_other_m']
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('swan_m',
	ARRAY[
	'swan_m_timestamp',
    'swan_1_m',
    'swan_2_m',
    'swan_3_m',
    'swan_4_m',
    'swan_5_m',
    'swan_6_m',
    'swan_7_m',
    'swan_8_m',
    'swan_9_m',
    'swan_10_m',
    'swan_11_m',
    'swan_12_m',
    'swan_13_m',
    'swan_14_m',
    'swan_15_m',
    'swan_16_m',
    'swan_17_m',
    'swan_18_m'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('swan_f',
	ARRAY[
	'swan_f_timestamp',
	'swan_1_f',
    'swan_2_f',
    'swan_3_f',
    'swan_4_f',
    'swan_5_f',
    'swan_6_f',
    'swan_7_f',
    'swan_8_f',
    'swan_9_f',
    'swan_10_f',
    'swan_11_f',
    'swan_12_f',
    'swan_13_f',
    'swan_14_f',
    'swan_15_f',
    'swan_16_f',
    'swan_17_f',
    'swan_18_f'
	]
);



INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('dass_f',
	ARRAY[
		'dass_f_timestamp',
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
);



INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ecr_f',
	ARRAY[
		'ecr_f_timestamp',
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
		'ecr_36_f'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('trq_sf_maris_clin',
	ARRAY[
		'trqsfmarisclin_timestamp',
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
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('screening_form',
	ARRAY[
		'screening_form_timestamp',
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
);



INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('c_ssrs_fu_maya',
	ARRAY[
		'cssrs_fw_maya_timestamp',
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
);



INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('opening',
	ARRAY[
		'opening_timestamp',
		'id',
		'er_num',
		'complaint___1',
		'complaint___2',
		'complaint___3',
		'complaint___4',
		'complaint___5',
		'complaint___6',
		'complaint_other',
		'complaint_date',
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
		'opening_medicine_3',
		'group___1',
		'group___2',
		'group___3',
		'consent',
		'consent_no'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('covid19',
	ARRAY[
		'covid19_timestamp',
		'covid_1___1',
		'covid_1___2',
		'covid_1___3',
		'covid_1___4',
		'covid_2',
		'covid_3___1',
		'covid_3___2',
		'covid_3___3',
		'covid_3___4',
		'covid_3___5',
		'covid_3___6',
		'covid_3___7',
		'covid_3___8',
		'covid_4',
		'covid_5',
		'covid_6',
		'covid_7',
		'covid_8'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('opening_child_pre',
	ARRAY[
		'opening_child_pre_timestamp',
		'age_child_pre',
		'gender'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('erc_rc',
	ARRAY[
		'ecrrc_timestamp',
		'erc_rc_1',
		'erc_rc_2',
		'erc_rc_3',
		'erc_rc_4',
		'erc_rc_5',
		'erc_rc_6',
		'erc_rc_7',
		'erc_rc_8',
		'erc_rc_9',
		'erc_rc_10',
		'erc_rc_11',
		'erc_rc_12'
	]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('piu_cyberbulling',
	ARRAY[
		'piu_cyberbulling_timestamp',
		'piu_1',
		'piu_2',
		'piu_3',
		'piu_4',
		'piu_5',
		'piu_6',
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
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('erq_ca',
	ARRAY[

		'erqca_timestamp',
		'erq_ca_1',
		'erq_ca_2',
		'erq_ca_3',
		'erq_ca_4',
		'erq_ca_5',
		'erq_ca_6',
		'erq_ca_7',
		'erq_ca_8',
		'erq_ca_9',
		'erq_ca_10'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ders',
	ARRAY[
		'ders_timestamp'
		'ders_1',
		'ders_2',
		'ders_3',
		'ders_4',
		'ders_5',
		'ders_6',
		'ders_7',
		'ders_8',
		'ders_9',
		'ders_10',
		'ders_11',
		'ders_12',
		'ders_13',
		'ders_14',
		'ders_15',
		'ders_16',
		'ders_17',
		'ders_18',
		'ders_19',
		'ders_20',
		'ders_21',
		'ders_22',
		'ders_23',
		'ders_24',
		'ders_25',
		'ders_26',
		'ders_27',
		'ders_28',
		'ders_29',
		'ders_30',
		'ders_31',
		'ders_32',
		'ders_33',
		'ders_34',
		'ders_35',
		'ders_36'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('wai',
	ARRAY[
		'wai_timestamp',
		'wai_1'
		'wai_2',
		'wai_3',
		'wai_4',
		'wai_5',
		'wai_6',
		'wai_7',
		'wai_8',
		'wai_9',
		'wai_10',
		'wai_11',
		'wai_12'
	]
);







INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('cshq_m',
	ARRAY[
		'cshq_m_timestamp',
		'age_cshq_m',
		'bedtime_1_m',
		'bedtime_2_m',
		'bedtime_3_m',
		'dtime_4_m',
		'dtime_5_m',
		'bedtime_6_m',
		'bedtime_7_m',
		'bedtime_8_m',
		'bedtime_9_m',
		'bedtime_10_m',
		'duration_1_m',
		'duration_2_m',
		'duration_3_m',
		'duration_4_m',
		'duration_5_m',
		'duration_6_m',
		'duration_7_m',
		'duration_8_m',
		'duration_9_m',
		'duration_10_m',
		'duration_11_m',
		'duration_12_m',
		'duration_13_m',
		'duration_14_m',
		'duration_15_m',
		'night_wake_1_m',
		'night_wake_2_m',
		'night_wake_3_m',
		'day_wake_1_m',
		'day_wake_2_m',
		'day_wake_3_m',
		'day_wake_4_m',
		'day_wake_5_m',
		'day_wake_6_m',
		'sleepiness_1_m',
		'sleepiness_2_m',
		'daytime_sleepiness_3_m'

	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('sdq_parents_m',
	ARRAY[
		'sdq_parents_m_timestamp',
		'sdq_1_parents_m',
		'sdq_2_parents_m',
		'sdq_3_parents_m',
		'sdq_4_parents_m',
		'sdq_5_parents_m',
		'sdq_6_parents_m',
		'sdq_7_parents_m',
		'sdq_8_parents_m',
		'sdq_9_parents_m',
		'sdq_10_parents_m',
		'sdq_11_parents_m',
		'sdq_12_parents_m',
		'sdq_13_parents_m',
		'sdq_14_parents_m',
		'sdq_15_parents_m',
		'sdq_16_parents_m',
		'sdq_17_parents_m',
		'sdq_18_parents_m',
		'sdq_19_parents_m',
		'sdq_20_parents_m',
		'sdq_21_parents_m',
		'sdq_22_parents_m',
		'sdq_23_parents_m',
		'sdq_24_parents_m',
		'sdq_25_parents_m',
		'sdq_26_parents_m',
		'sdq_27_parents_m',
		'sdq_28_parents_m',
		'sdq_29_parents_1_m',
		'sdq_29_parents_2_m',
		'sdq_29_parents_3_m',
		'sdq_29_parents_4_m',
		'sdq_30_parents_m'
	]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('dass_m',
	ARRAY[
		'dass_m_timestamp',
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
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ders_p_m',
	ARRAY[
		'ders_p_m_timestamp',
		'ders_1_p_m',
		'ders_2_p_m',
		'ders_3_p_m',
		'ders_4_p_m',
		'ders_5_p_m',
		'ders_6_p_m',
		'ders_7_p_m',
		'ders_8_p_m',
		'ders_9_p_m',
		'ders_10_p_m',
		'ders_11_p_m',
		'ders_12_p_m',
		'ders_13_p_m',
		'ders_14_p_m',
		'ders_15_p_m',
		'ders_16_p_m',
		'ders_17_p_m',
		'ders_18_p_m',
		'ders_19_p_m',
		'ders_20_p_m',
		'ders_21_p_m',
		'ders_22_p_m',
		'ders_23_p_m',
		'ders_24_p_m',
		'ders_25_p_m',
		'ders_26_p_m',
		'ders_27_p_m',
		'ders_28_p_m',
		'ders_29_p_m',
		'ders_30_p_m',
		'ders_31_p_m',
		'ders_32_p_m',
		'ders_33_p_m',
		'ders_34_p_m',
		'ders_35_p_m',
		'ders_36_p_m'
	]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ecr_m',
	ARRAY[
	'ecr_m_timestamp',
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
		'ecr_36_m'

	]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('cshq_f',
	ARRAY[
		'cshq_f_timestamp',
		'age_cshq_f',
		'bedtime_1_f',
		'bedtime_2_f',
		'bedtime_3_f',
		'bedtime_4_f',
		'bedtime_5_f',
		'bedtime_6_f',
		'bedtime_7_f',
		'bedtime_8_f',
		'bedtime_9_f',
		'bedtime_10_f',
		'duration_1_f',
		'duration_2_f',
		'duration_3_f',
		'duration_4_f',
		'duration_5_f',
		'duration_6_f',
		'duration_7_f',
		'duration_8_f',
		'duration_9_f',
		'duration_10_f',
		'duration_11_f',
		'duration_12_f',
		'duration_13_f',
		'duration_14_f',
		'duration_15_f',
		'night_wake_1_f',
		'night_wake_2_f',
		'night_wake_3_f',
		'day_wake_1_f',
		'day_wake_2_f',
		'day_wake_3_f',
		'day_wake_4_f',
		'day_wake_5_f',
		'day_wake_6_f',
		'sleepiness_1_f',
		'sleepiness_2_f',
		'daytime_sleepiness_3_f'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('erq_f',
	ARRAY[
		'erq_f_timestamp',
		'erq_1_f',
		'erq_2_f',
		'erq_3_f',
		'erq_4_f',
		'erq_5_f',
		'erq_6_f',
		'erq_7_f',
		'erq_8_f',
		'erq_9_f',
		'erq_10_f'
	]
);







INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ARI_P_F',
	ARRAY[
		'arippps_f_timestamp',
		'ari_p_1_f',
		'ari_p_2_f',
		'ari_p_3_f',
		'ari_p_4_f',
		'ari_p_5_f',
		'ari_p_6_f',
		'ari_p_7_f',
		'pps_1_f',
		'pps_2_f'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('opening_clinicians_timestamp',
	ARRAY[
		'opening_clinicians_timestamp',
		'who_clin',
		'who_other_clin',
		'name_clin'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('wai_immirisk_clin',
	ARRAY[
		'wai_immirisk_clin_timestamp',
		'wai_t_immi_1_clin',
		'wai_t_immi_2_clin',
		'wai_t_immi_3_clin',
		'wai_t_immi_4_clin',
		'wai_t_immi_5_clin',
		'wai_t_immi_6_clin',
		'wai_t_immi_7_clin',
		'wai_t_immi_8_clin',
		'wai_t_immi_9_clin',
		'wai_t_immi_10_clin',
		'wai_t_immi_11_clin',
		'wai_t_immi_12_clin'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('remote_clin',
	ARRAY[
		'remote_clin_timestamp',
		'remote_1_clin'
	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('er_questionnaire_clin',
	ARRAY[
		'er_questionnaire_clin_timestamp',
		'er_id',
		'er_name_clin',
		'er_date_of_birth_clin',
		'er_id_clin',
		'er_arrival_clin',
		'er_reason_clin',
		'er_attemp_time_clin',
		'er_planned_clin',
		'er_regret_clin',
		'er_cut_first_clin',
		'er_thoughts_clin',
		'er_worst_thoughts_clin',
		'er_thoughts_now_clin',
		'er_medicine_clin',
		'er_medicine_what_clin',
		'er_medicine_mg_clin'

	]
);




INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('suicide_form_clin',
	ARRAY[
		'suicide_form_clin_timestamp',
		'suiciform_time_clin',
		'medhis_1_clin',
		'medhis_1_1_clin',
		'medhis_2_clin',
		'medhis_2_1_clin',
		'medhis_3_clin',
		'medhis_3_1_clin',
		'medhis_4_clin',
		'medhis_4_1_clin',
		'medhis_5_clin',
		'medhis_5_1_clin',
		'medhis_6_clin',
		'medhis_6_1_clin',
		'medhis_7_clin',
		'medhis_7_1_clin',
		'medhis_8_clin',
		'medhis_8_1_clin',
		'medhis_9_clin',
		'medhis_9_1_clin',
		'medhis_10_clin',
		'medhis_10_1_clin',
		'medhis_11_clin',
		'medhis_11_1_clin',
		'medhis_12_clin',
		'medhis_12_1_clin',
		'medhis_13_clin',
		'medhis_13_1_clin',
		'medhis_details_clin',
		'diet_1_clin',
		'diet_1_1_clin',
		'diet_2_clin',
		'diet_2_1_clin',
		'diet_3_clin',
		'diet_3_1_clin',
		'diet_4_clin',
		'diet_4_1_clin',
		'diet_5_clin',
		'diet_5_1_clin',
		'medhis_clin',
		'inclusion_1_clin',
		'inclusion_2_clin',
		'exclusion_1_clin',
		'exclusion_2_clin',
		'exclusion_3_clin',
		'exclusion_4_clin',
		'exclusion_5_clin',
		'exclusion_6_clin',
		'week_1_clin',
		'week_1_1_clin',
		'week_2_clin',
		'week_2_1_clin',
		'week_3_clin',
		'week_medic_clin',
		'three_mon_1_clin',
		'three_mon_1_1_clin',
		'three_mon_2_clin',
		'three_mon_2_1_clin',
		'three_mon_3_clin',
		'three_mon_medic_clin',
		'six_mon_1_clin',
		'six_mon_1_1_clin',
		'six_mon_2_clin',
		'six_mon_2_1_clin',
		'six_mon_3_clin',
		'six_mon_medic_clin',
		'twelve_mon_1_clin',
		'twelve_mon_1_1_clin',
		'twelve_mon_2_clin',
		'twelve_mon_2_1_clin',
		'twelve_mon_3_clin',
		'twelve_mon_medic_clin'
]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('mini_kid_sum_clin',
	ARRAY[
		'mini_kid_sum_clin_timestamp',
		'mini_class_clin',
		'mini_date_clin',
		'mini_interviewer_clin',
		'mini_date_interview_clin',
		'mini_medication_clin___1',
		'mini_medication_clin___2',
		'mini_medication_clin___3',
		'mini_medication_clin___4',
		'mini_medication_clin___5',
		'mini_medicine_other_clin',
		'mini_start_time_clin',
		'mini_end_time_clin',
		'mini_total_time_clin',
		'depres_clin___1',
		'depres_clin___2',
		'depres_clin___3',
		'suicide_clin___1',
		'suicide_clin___2',
		'suicide_risk_clin',
		'dysthemia_clin___1',
		'manic_clin___1',
		'manic_clin___2',
		'hypomania_clin___1',
		'hypomania_clin___2',
		'bipolar_i_clin___1',
		'bipolar_i_clin___2',
		'bipolar_ii_clin___1',
		'bipolar_ii_clin___2',
		'bipolar_unclassified_clin___1',
		'bipolar_unclassified_clin___2',
		'panic_clin___1',
		'panic_clin___2',
		'agoraphobia_clin___1',
		'separation_anxiety_clin___1',
		'social_anxiety_clin___1',
		'social_anxiety_clin___2',
		'social_anxiety_clin___3',
		'phobia_clin___1',
		'ocd_clin___1',
		'ptsd_clin___1',
		'alcohol_depend_clin___1',
		'alcohol_use_clin___1',
		'drug_depend_clin___1',
		'drug_use_clin___1',
		'tourette_clin___1',
		'motor_tics_clin___1',
		'vocal_tics_clin___1',
		'transient_tics_clin___1',
		'adhd_mix_clin___1',
		'adhd_attention_clin___1',
		'adhd_hyper_clin___1',
		'conduct_clin___1',
		'odd_clin___1',
		'psychotic_clin___1',
		'psychotic_clin___2',
		'affect_psychotic_clin___1',
		'affect_psychotic_clin___2',
		'anorexia_clin___1',
		'bulimia_clin___1',
		'anorexia_bulmus_clin___1',
		'gad_clin___1',
		'adjustment_clin___1',
		'organic_clin',
		'development_clin___1',
		'main_dianose_clin'
]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('trq_sf_maris_stu',
	ARRAY[
	'trqsfmaris_stu_timestamp',
		'trq_sf_maris_1_stu',
		'trq_sf_maris_2_stu',
		'trq_sf_maris_3_stu',
		'trq_sf_maris_4_stu',
		'trq_sf_maris_5_stu',
		'trq_sf_maris_6_stu',
		'trq_sf_maris_7_stu',
		'trq_sf_maris_8_stu',
		'trq_sf_maris_9_stu',
		'trq_sf_maris_10_stu',
		'trq_sf_maris_11_stu',
		'trq_sf_maris_12_stu',
		'trq_sf_maris_13_stu',
		'trq_sf_maris_14_stu'
]
);







INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('mini_kid_sum_stu',
	ARRAY[
		'mini_kid_sum_stu_timestamp',
		'mini_class_stu',
        'mini_date_stu',
		'mini_interviewer_stu',
		'mini_date_interview_stu',
		'mini_medication_stu___1',
		'mini_medication_stu___2',
		'mini_medication_stu___3',
		'mini_medication_stu___4',
		'mini_medication_stu___5',
		'mini_medicine_other_stu',
		'mini_start_time_stu',
		'mini_end_time_stu',
		'mini_total_time_stu',
		'depres_stu___1',
		'depres_stu___2',
		'depres_stu___3',
		'suicide_stu___1',
		'suicide_stu___2',
		'suicide_risk_stu',
		'dysthemia_stu___1',
		'manic_stu___1',
		'manic_stu___2',
		'hypomania_stu___1',
		'hypomania_stu___2',
		'bipolar_i_stu___1',
		'bipolar_i_stu___2',
		'bipolar_ii_stu___1',
		'bipolar_ii_stu___2',
		'bipolar_unclassified_stu___1',
		'bipolar_unclassified_stu___2',
		'panic_stu___1',
		'panic_stu___2',
		'agoraphobia_stu___1',
		'separation_anxiety_stu___1',
		'social_anxiety_stu___1',
		'social_anxiety_stu___2',
		'social_anxiety_stu___3',
		'phobia_stu___1',
		'ocd_stu___1',
		'ptsd_stu___1',
		'alcohol_depend_stu___1',
		'alcohol_use_stu___1',
		'drug_depend_stu___1',
		'drug_use_stu___1',
		'tourette_stu___1',
		'motor_tics_stu___1',
		'vocal_tics_stu___1',
		'transient_tics_stu___1',
		'adhd_mix_stu___1',
		'adhd_attention_stu___1',
		'adhd_hyper_stu___1',
		'conduct_stu___1',
		'odd_stu___1',
		'psychotic_stu___1',
		'psychotic_stu___2',
		'affect_psychotic_stu___1',
		'affect_psychotic_stu___2',
		'anorexia_stu___1',
		'bulimia_stu___1',
		'anorexia_bulmus_stu___1',
		'gad_stu___1',
		'adjustment_stu___1',
		'organic_stu',
		'development_stu___1',
		'main_dianose_stu'

]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('chameleon',
	ARRAY[
	'chameleon_timestamp',
		'chameleon_follow_stu',
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
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('erq_m',
	ARRAY[
		'erq_m_timestamp',
		'erq_1_m',
		'erq_2_m',
		'erq_3_m',
		'erq_4_m',
		'erq_5_m',
		'erq_6_m',
		'erq_7_m',
		'erq_8_m',
		'erq_9_m',
		'erq_10_m'

]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('cts_m',
	ARRAY[
		'cts_m_timestamp',
		'cts_p_1_m',
		'cts_p_2_m',
		'cts_p_3_m',
		'cts_p_4_m',
		'cts_p_4_1_m'
]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('moas_m',
	ARRAY[
'moas_m_timestamp',
		'moas_0_m',
		'moas_1_m',
		'moas_2_m',
		'moas_3_m',
		'moas_4_m',
		'moas_5_m',
		'moas_6_m',
		'moas_7_m',
		'moas_8_m',
		'moas_9_m',
		'moas_10_m',
		'moas_11_m',
		'moas_12_m',
		'moas_13_m',
		'moas_14_m',
		'moas_15_m',
		'moas_16_m',
		'moas_17_m',
		'moas_18_m',
		'moas_19_m',
		'moas_20_m'
]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ending_parent_m',
	ARRAY[
		'ending_parent_m_timestamp',
		'therapy_child_2_m',
		'ending_childparent_m'
]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('opening_parents_f',
	ARRAY[
		'opening_parents_f_timestamp',
		'who_fills_out_f',
		'who_fills_out_2_f'
]
);







INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('sdq_parents_f',
	ARRAY[
		'sdq_parents_f_timestamp',
		'sdq_1_parents_f',
		'sdq_2_parents_f',
		'sdq_3_parents_f',
		'sdq_4_parents_f',
		'sdq_5_parents_f',
		'sdq_6_parents_f',
		'sdq_7_parents_f',
		'sdq_8_parents_f',
		'sdq_9_parents_f',
		'sdq_10_parents_f',
		'sdq_11_parents_f',
		'sdq_12_parents_f',
		'sdq_13_parents_f',
		'sdq_14_parents_f',
		'sdq_15_parents_f',
		'sdq_16_parents_f',
		'sdq_17_parents_f',
		'sdq_18_parents_f',
		'sdq_19_parents_f',
		'sdq_20_parents_f',
		'sdq_21_parents_f',
		'sdq_22_parents_f',
		'sdq_23_parents_f',
		'sdq_24_parents_f',
		'sdq_25_parents_f',
		'sdq_26_parents_f',
		'sdq_27_parents_f',
		'sdq_28_parents_f',
		'sdq_29_parents_1_f',
		'sdq_29_parents_2_f',
		'sdq_29_parents_3_f',
		'sdq_29_parents_4_f',
		'sdq_30_parents_f'
]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ders_p_f',
	ARRAY[
	'ders_p_f_timestamp',
		'ders_1_p_f',
		'ders_2_p_f',
		'ders_3_p_f',
		'ders_4_p_f',
		'ders_5_p_f',
		'ders_6_p_f',
		'ders_7_p_f',
		'ders_8_p_f',
		'ders_9_p_f',
		'ders_10_p_f',
		'ders_11_p_f',
		'ders_12_p_f',
		'ders_13_p_f',
		'ders_14_p_f',
		'ders_15_p_f',
		'ders_16_p_f',
		'ders_17_p_f',
		'ders_18_p_f',
		'ders_19_p_f',
		'ders_20_p_f',
		'ders_21_p_f',
		'ders_22_p_f',
		'ders_23_p_f',
		'ders_24_p_f',
		'ders_25_p_f',
		'ders_26_p_f',
		'ders_27_p_f',
		'ders_28_p_f',
		'ders_29_p_f',
		'ders_30_p_f',
		'ders_31_p_f',
		'ders_32_p_f',
		'ders_33_p_f',
		'ders_34_p_f',
		'ders_35_p_f',
		'ders_36_p_f'
	]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('cdrsr_clin',
	ARRAY[
'cdrsr_clin_timestamp',
		'cdrs_impaired_schoolwork_clin',
		'cdrs_difficulty_having_fun_clin',
		'sdrs_social_withdrawal_clin',
		'cdrs_sleep_disturbance_clin',
		'cdrs_sleep_disturbance_2_clin',
		'cdrs_appetite_disturbance_clin',
		'cdrs_appetite_disturbance_2_clin',
		'cdrs_excessive_fatigue_clin',
		'cdrs_physical_complaints_clin',
		'sdrs_irritability_clin',
		'cdrs_excessive_guilt_clin',
		'cdrs_low_self_esteem_clin',
		'cdrs_depressed_feelings_clin',
		'cdrs_morbid_ideation_clin',
		'cdrs_suicidal_ideation_clin',
		'cdrs_excessive_weeping_clin',
		'cdrs_depressed_facial_affect_clin',
		'cdrs_listless_speech_clin',
		'cdrs_hypoactivity_clin',
		'cdrs_sum_clin'
	]
);







INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ffq',
	ARRAY[
		'ffq_sum_timestamp',
		'ffq_sum'
	]
);







INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('opening_students',
	ARRAY[
		'opening_students_timestamp',
		'who_stu',
		'who_other_stu',
		'name_stu'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('cgi_s_stu',
	ARRAY[
		'cgi_s_base_stu',
		'cgi_s_stu_complete'
	]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('remote_stu',
	ARRAY[
		'remote_stu_timestamp',
		'remote_1_stu'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('cps_stu',
	ARRAY[
		'cps_stu_timestamp',
		'cps_1_stu',
		'cps_2_stu'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('cps_clin',
	ARRAY[
		'cps_clin_timestamp',
		'cps_1_clin',
		'cps_2_clin'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('cgi_s_clin',
	ARRAY[
		'cgi_s_clin_timestamp',
		'cgi_s_base_clin'
	]
);









INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('opening_therapist_battery',
	ARRAY[
		'opening_therapist_battery_timestamp',
		'time_clin',
		'parents_safety_plan_clin',
		'safety_plan_clin',
		'safety_plan_changed_clin',
		'cgi_s_clin',
		'cgi_i_clin',
		'wai_t_1_clin',
		'wai_t_2_clin',
		'wai_t_3_clin',
		'wai_t_4_clin',
		'wai_t_5_clin',
		'wai_t_6_clin',
		'wai_t_7_clin',
		'wai_t_8_clin',
		'wai_t_9_clin',
		'wai_t_10_clin',
		'wai_t_11_clin',
		'wai_t_12_clin'
	]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('maris_y_scars_clin',
	ARRAY[
		'marisyscars_clin_timestamp',
		'maris_y_scars_1_clin',
		'maris_y_scars_2_clin',
		'maris_y_scars_3_clin',
		'maris_y_scars_4_clin',
		'maris_y_scars_5_clin',
		'maris_y_scars_6_clin',
		'maris_y_scars_7_clin',
		'maris_y_scars_8_clin'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ending_parent_f',
	ARRAY[
		'ending_parent_f_timestamp',
		'therapy_child_2_f',
		'ending_childparent_f'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('moas_f',
	ARRAY[
		'moas_f_timestamp',
		'moas_0_f',
		'moas_1_f',
		'moas_2_f',
		'moas_3_f',
		'moas_4_f',
		'moas_5_f',
		'moas_6_f',
		'moas_7_f',
		'moas_8_f',
		'moas_9_f',
		'moas_10_f',
		'moas_11_f',
		'moas_12_f',
		'moas_13_f',
		'moas_14_f',
		'moas_15_f',
		'moas_16_f',
		'moas_17_f',
		'moas_18_f',
		'moas_19_f',
		'moas_20_f'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('cts_f',
	ARRAY[
		'cts_f_timestamp',
		'cts_p_1_f',
		'cts_p_2_f',
		'cts_p_3_f',
		'cts_p_4_f',
		'cts_p_4_1_f'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('cts_c',
	ARRAY[
		'cts_c_timestamp',
		'cts_c_1',
		'cts_c_2',
		'cts_c_3',
		'cts_c_4',
		'cts_c_4_1'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('dshi_pre',
	ARRAY[
		'dshi_pre_timestamp',
		'dshi_pre_1',
		'dshi_pre_2',
		'dshi_pre_3',
		'dshi_pre_4',
		'dshi_pre_5',
		'dshi_pre_6'

	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('dshi_post',
	ARRAY[
		'dshi_post_timestamp',
		'dshi_post_1',
		'dshi_post_2',
		'dshi_post_3',
		'dshi_post_4',
		'dshi_post_5',
		'dshi_post_6'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('inq',
	ARRAY[
'inq_timestamp',
		'inq_1',
		'inq_2',
		'inq_3',
		'inq_4',
		'inq_5',
		'inq_6',
		'inq_7',
		'inq_8',
		'inq_9',
		'inq_10',
		'inq_11',
		'inq_12',
		'inq_13',
		'inq_14',
		'inq_15'
	]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('ending',
	ARRAY[
		'ending_timestamp',
		'therapy_child',
		'ending_child'

	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('opening_parents_m',
	ARRAY[
		'opening_parents_m_timestamp',
		'who_fills_out_m',
		'who_fills_out_2_m'
	]
);






INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('estimation_and_satisfaction',
	ARRAY[
		'estimation_and_satisfaction_timestamp',
		'satis_1',
		'satis_2',
		'satis_3',
		'satis_4'
	]
);





INSERT INTO auxiliary_questionnaires_data.questionnaires_columns_names (questionnaire_name, column_names)
VALUES('intro',
	ARRAY[
		'record_id',
		'redcap_event_name',
		'redcap_survey_identifier'
	]
);

#################### upload redcap data
CREATE SCHEMA redcap_data


CREATE TABLE redcap_data.c_ssrs_intake(
    primary_key VARCHAR (20) PRIMARY KEY,
    cssrs_intake_timestamp VARCHAR (20),
    c_ssrs_1_life VARCHAR (20),
    c_ssrs_2_life VARCHAR (20),
    c_ssrs_3_life VARCHAR (20),
    c_ssrs_4_life VARCHAR (20),
    c_ssrs_5_life VARCHAR (20),
    c_ssrs_6_life VARCHAR (20),
    c_ssrs_1_2weeks VARCHAR (20),
    c_ssrs_2_2weeks VARCHAR (20),
    c_ssrs_3_2weeks VARCHAR (20),
    c_ssrs_4_2weeks VARCHAR (20),
    c_ssrs_5_2weeks VARCHAR (20),
    c_ssrs_6_2weeks VARCHAR (20),
    c_ssrs_6_3month VARCHAR (20),
    c_ssrs_7_intake VARCHAR (20),
    c_ssrs_8_intake VARCHAR (20));


CREATE TABLE redcap_data.c_ssrs(
        primary_key VARCHAR (20) PRIMARY KEY,
        cssrs_timestamp VARCHAR (50),
    c_ssrs_1 VARCHAR (50),
    c_ssrs_2 VARCHAR (50),
    c_ssrs_3 VARCHAR (50),
    c_ssrs_4 VARCHAR (50),
    c_ssrs_5 VARCHAR (50),
    c_ssrs_6 VARCHAR (50),
    c_ssrs_last_visit_6 VARCHAR (50),
    c_ssrs_7 VARCHAR (50),
    c_ssrs_8 VARCHAR (50));




CREATE TABLE redcap_data.c_ssrs_clin(
        primary_key VARCHAR (20) PRIMARY KEY,
        cssrs_t_clin_timestamp VARCHAR (50),
    c_ssrs_t_time_clin VARCHAR (50),
    c_ssrs_t_2weeks_1_clin VARCHAR (50),
    c_ssrs_t_2weeks_2_clin VARCHAR (50),
    c_ssrs_t_2weeks_3_clin VARCHAR (50),
    c_ssrs_t_2weeks_4_clin VARCHAR (50),
    c_ssrs_t_2weeks_5_clin VARCHAR (50),
    c_ssrs_t_last_1_clin VARCHAR (50),
    c_ssrs_t_last_2_clin VARCHAR (50),
    c_ssrs_t_last_3_clin VARCHAR (50),
    c_ssrs_t_last_4_clin VARCHAR (50),
    c_ssrs_t_last_5_clin VARCHAR (50),
    c_ssrs_t_life_1_clin VARCHAR (50),
    c_ssrs_t_life_2_clin VARCHAR (50),
    c_ssrs_t_life_3_clin VARCHAR (50),
    c_ssrs_t_life_4_clin VARCHAR (50),
    c_ssrs_t_life_5_clin VARCHAR (50),
    c_ssrs_t_6_clin VARCHAR (50),
    c_ssrs_t_7_clin VARCHAR (50),
    c_ssrs_t_8_clin VARCHAR (50),
    c_ssrs_t_9_clin VARCHAR (50),
    c_ssrs_t_10_clin VARCHAR (50),
    c_ssrs_t_6_clin_2 VARCHAR (50),
    c_ssrs_t_7_clin_2 VARCHAR (50),
    c_ssrs_t_8_clin_2 VARCHAR (50),
    c_ssrs_t_9_clin_2 VARCHAR (50),
    c_ssrs_t_10_clin_2 VARCHAR (50),
    c_ssrs_t_11_2weeks_clin VARCHAR (50),
    c_ssrs_t_12_2weeks_clin VARCHAR (50),
    c_ssrs_t_13_2weeks_clin VARCHAR (50),
    c_ssrs_t_14_2weeks_clin VARCHAR (50),
    c_ssrs_t_15_2weeks_clin VARCHAR (50),
    c_ssrs_t_16_2weeks_clin VARCHAR (50),
    suicidal_behavior_last_11_clin VARCHAR (50),
    suicidal_behavior_last_12_clin VARCHAR (50),
    suicidal_behavior_last_13_clin VARCHAR (50),
    suicidal_behavior_last_14_clin VARCHAR (50),
    suicidal_behavior_last_15_clin VARCHAR (50),
    suicidal_behavior_last_16_clin VARCHAR (50),
    suicidal_behavior_last_17_clin VARCHAR (50),
    suicidal_behavior_last_11_clin_1 VARCHAR (50),
    suicidal_behavior_last_12_clin_1 VARCHAR (50),
    suicidal_behavior_last_13_clin_1 VARCHAR (50),
    suicidal_behavior_last_18_clin VARCHAR (50),
    suicidal_behavior_last_19_clin VARCHAR (50),
    c_ssrs_t_11_life_clin VARCHAR (50),
    c_ssrs_t_12_life_clin VARCHAR (50),
    c_ssrs_t_13_life_clin VARCHAR (50),
    c_ssrs_t_14_life_clin VARCHAR (50),
    c_ssrs_t_15_life_clin VARCHAR (50),
    c_ssrs_t_16_life_clin VARCHAR (50),
    c_ssrs_t_17_life_clin VARCHAR (50),
    c_ssrs_t_11_life_clin_1 VARCHAR (50),
    c_ssrs_t_12_life_clin_1 VARCHAR (50),
    c_ssrs_t_13_life_clin_1 VARCHAR (50),
    c_ssrs_t_18_life_clin VARCHAR (50),
    c_ssrs_t_19_life_clin VARCHAR (50));



CREATE TABLE redcap_data.c_ssrs_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    cssrs_t_clin_timestamp VARCHAR (50),
c_ssrs_t_time_clin VARCHAR (50),
c_ssrs_t_2weeks_1_clin VARCHAR (50),
c_ssrs_t_2weeks_2_clin VARCHAR (50),
c_ssrs_t_2weeks_3_clin VARCHAR (50),
c_ssrs_t_2weeks_4_clin VARCHAR (50),
c_ssrs_t_2weeks_5_clin VARCHAR (50),
c_ssrs_t_last_1_clin VARCHAR (50),
c_ssrs_t_last_2_clin VARCHAR (50),
c_ssrs_t_last_3_clin VARCHAR (50),
c_ssrs_t_last_4_clin VARCHAR (50),
c_ssrs_t_last_5_clin VARCHAR (50),
c_ssrs_t_life_1_clin VARCHAR (50),
c_ssrs_t_life_2_clin VARCHAR (50),
c_ssrs_t_life_3_clin VARCHAR (50),
c_ssrs_t_life_4_clin VARCHAR (50),
c_ssrs_t_life_5_clin VARCHAR (50),
c_ssrs_t_6_clin VARCHAR (50),
c_ssrs_t_7_clin VARCHAR (50),
c_ssrs_t_8_clin VARCHAR (50),
c_ssrs_t_9_clin VARCHAR (50),
c_ssrs_t_10_clin VARCHAR (50),
c_ssrs_t_6_clin_2 VARCHAR (50),
c_ssrs_t_7_clin_2 VARCHAR (50),
c_ssrs_t_8_clin_2 VARCHAR (50),
c_ssrs_t_9_clin_2 VARCHAR (50),
c_ssrs_t_10_clin_2 VARCHAR (50),
c_ssrs_t_11_2weeks_clin VARCHAR (50),
c_ssrs_t_12_2weeks_clin VARCHAR (50),
c_ssrs_t_13_2weeks_clin VARCHAR (50),
c_ssrs_t_14_2weeks_clin VARCHAR (50),
c_ssrs_t_15_2weeks_clin VARCHAR (50),
c_ssrs_t_16_2weeks_clin VARCHAR (50),
suicidal_behavior_last_11_clin VARCHAR (50),
suicidal_behavior_last_12_clin VARCHAR (50),
suicidal_behavior_last_13_clin VARCHAR (50),
suicidal_behavior_last_14_clin VARCHAR (50),
suicidal_behavior_last_15_clin VARCHAR (50),
suicidal_behavior_last_16_clin VARCHAR (50),
suicidal_behavior_last_17_clin VARCHAR (50),
suicidal_behavior_last_11_clin_1 VARCHAR (50),
suicidal_behavior_last_12_clin_1 VARCHAR (50),
suicidal_behavior_last_13_clin_1 VARCHAR (50),
suicidal_behavior_last_18_clin VARCHAR (50),
suicidal_behavior_last_19_clin VARCHAR (50),
c_ssrs_t_11_life_clin VARCHAR (50),
c_ssrs_t_12_life_clin VARCHAR (50),
c_ssrs_t_13_life_clin VARCHAR (50),
c_ssrs_t_14_life_clin VARCHAR (50),
c_ssrs_t_15_life_clin VARCHAR (50),
c_ssrs_t_16_life_clin VARCHAR (50),
c_ssrs_t_17_life_clin VARCHAR (50),
c_ssrs_t_11_life_clin_1 VARCHAR (50),
c_ssrs_t_12_life_clin_1 VARCHAR (50),
c_ssrs_t_13_life_clin_1 VARCHAR (50),
c_ssrs_t_18_life_clin VARCHAR (50),
c_ssrs_t_19_life_clin VARCHAR (50));




CREATE TABLE redcap_data.c_ssrs_stu(
    primary_key VARCHAR (20) PRIMARY KEY,
    cssrs_t_stu_timestamp VARCHAR (50),
c_ssrs_t_time_stu VARCHAR (50),
c_ssrs_t_2weeks_1_stu VARCHAR (50),
c_ssrs_t_2weeks_2_stu VARCHAR (50),
c_ssrs_t_2weeks_3_stu VARCHAR (50),
c_ssrs_t_2weeks_4_stu VARCHAR (50),
c_ssrs_t_2weeks_5_stu VARCHAR (50),
c_ssrs_t_last_1_stu VARCHAR (50),
c_ssrs_t_last_2_stu VARCHAR (50),
c_ssrs_t_last_3_stu VARCHAR (50),
c_ssrs_t_last_4_stu VARCHAR (50),
c_ssrs_t_last_5_stu VARCHAR (50),
c_ssrs_t_life_1_stu VARCHAR (50),
c_ssrs_t_life_2_stu VARCHAR (50),
c_ssrs_t_life_3_stu VARCHAR (50),
c_ssrs_t_life_4_stu VARCHAR (50),
c_ssrs_t_life_5_stu VARCHAR (50),
c_ssrs_t_6_stu VARCHAR (50),
c_ssrs_t_7_stu VARCHAR (50),
c_ssrs_t_8_stu VARCHAR (50),
c_ssrs_t_9_stu VARCHAR (50),
c_ssrs_t_10_stu VARCHAR (50),
c_ssrs_t_6_stu_2 VARCHAR (50),
c_ssrs_t_7_stu_2 VARCHAR (50),
c_ssrs_t_8_stu_2 VARCHAR (50),
c_ssrs_t_9_stu_2 VARCHAR (50),
c_ssrs_t_10_stu_2 VARCHAR (50),
c_ssrs_t_11_2weeks_stu VARCHAR (50),
c_ssrs_t_12_2weeks_stu VARCHAR (50),
c_ssrs_t_13_2weeks_stu VARCHAR (50),
c_ssrs_t_14_2weeks_stu VARCHAR (50),
c_ssrs_t_15_2weeks_stu VARCHAR (50),
c_ssrs_t_16_2weeks_stu VARCHAR (50),
suicidal_behavior_last_11_stu VARCHAR (50),
suicidal_behavior_last_12_stu VARCHAR (50),
suicidal_behavior_last_13_stu VARCHAR (50),
suicidal_behavior_last_14_stu VARCHAR (50),
suicidal_behavior_last_15_stu VARCHAR (50),
suicidal_behavior_last_16_stu VARCHAR (50),
suicidal_behavior_last_17_stu VARCHAR (50),
suicidal_behavior_last_11_stu_1 VARCHAR (50),
suicidal_behavior_last_12_stu_1 VARCHAR (50),
suicidal_behavior_last_13_stu_1 VARCHAR (50),
suicidal_behavior_last_18_stu VARCHAR (50),
suicidal_behavior_last_19_stu VARCHAR (50),
c_ssrs_t_11_life_stu VARCHAR (50),
c_ssrs_t_12_life_stu VARCHAR (50),
c_ssrs_t_13_life_stu VARCHAR (50),
c_ssrs_t_14_life_stu VARCHAR (50),
c_ssrs_t_15_life_stu VARCHAR (50),
c_ssrs_t_16_life_stu VARCHAR (50),
c_ssrs_t_17_life_stu VARCHAR (50),
c_ssrs_t_11_life_stu_1 VARCHAR (50),
c_ssrs_t_12_life_stu_1 VARCHAR (50),
c_ssrs_t_13_life_stu_1 VARCHAR (50),
c_ssrs_t_18_life_stu VARCHAR (50),
c_ssrs_t_19_life_stu VARCHAR (50));




CREATE TABLE redcap_data.mfq(
    primary_key VARCHAR (20) PRIMARY KEY,
    mfq_short_timestamp VARCHAR (50),
mfq_1 VARCHAR (50),
mfq_2 VARCHAR (50),
mfq_5 VARCHAR (50),
mfq_7 VARCHAR (50),
mfq_8 VARCHAR (50),
mfq_14 VARCHAR (50),
mfq_21 VARCHAR (50),
mfq_23 VARCHAR (50),
mfq_24 VARCHAR (50),
mfq_27 VARCHAR (50),
mfq_28 VARCHAR (50),
mfq_30 VARCHAR (50),
mfq_31 VARCHAR (50),
mfq_34 VARCHAR (50),
mfq_35 VARCHAR (50),
mfq_36 VARCHAR (50),
mfq_37 VARCHAR (50));




CREATE TABLE redcap_data.siq(
    primary_key VARCHAR (20) PRIMARY KEY,
    siq_timestamp VARCHAR (50),
siq_1 VARCHAR (50),
siq_2 VARCHAR (50),
siq_3 VARCHAR (50),
siq_4 VARCHAR (50),
siq_5 VARCHAR (50),
siq_6 VARCHAR (50),
siq_7 VARCHAR (50),
siq_8 VARCHAR (50),
siq_9 VARCHAR (50),
siq_10 VARCHAR (50),
siq_11 VARCHAR (50),
siq_12 VARCHAR (50),
siq_13 VARCHAR (50),
siq_14 VARCHAR (50),
siq_15 VARCHAR (50));




CREATE TABLE redcap_data.sdq(
    primary_key VARCHAR (20) PRIMARY KEY,
    sdq_timestamp VARCHAR (50),
sdq_1 VARCHAR (50),
sdq_2 VARCHAR (50),
sdq_3 VARCHAR (50),
sdq_4 VARCHAR (50),
sdq_5 VARCHAR (50),
sdq_6 VARCHAR (50),
sdq_7 VARCHAR (50),
sdq_8 VARCHAR (50),
sdq_9 VARCHAR (50),
sdq_10 VARCHAR (50),
sdq_11 VARCHAR (50),
sdq_12 VARCHAR (50),
sdq_13 VARCHAR (50),
sdq_14 VARCHAR (50),
sdq_15 VARCHAR (50),
sdq_16 VARCHAR (50),
sdq_17 VARCHAR (50),
sdq_18 VARCHAR (50),
sdq_19 VARCHAR (50),
sdq_20 VARCHAR (50),
sdq_21 VARCHAR (50),
sdq_22 VARCHAR (50),
sdq_23 VARCHAR (50),
sdq_24 VARCHAR (50),
sdq_25 VARCHAR (50));




CREATE TABLE redcap_data.scared(
    primary_key VARCHAR (20) PRIMARY KEY,
    scared_timestamp VARCHAR (50),
scared_1 VARCHAR (50),
scared_2 VARCHAR (50),
scared_3 VARCHAR (50),
scared_4 VARCHAR (50),
scared_5 VARCHAR (50),
scared_6 VARCHAR (50),
scared_7 VARCHAR (50),
scared_8 VARCHAR (50),
scared_9 VARCHAR (50),
scared_10 VARCHAR (50),
scared_11 VARCHAR (50),
scared_12 VARCHAR (50),
scared_13 VARCHAR (50),
scared_14 VARCHAR (50),
scared_15 VARCHAR (50),
scared_16 VARCHAR (50),
scared_17 VARCHAR (50),
scared_18 VARCHAR (50),
scared_19 VARCHAR (50),
scared_20 VARCHAR (50),
scared_21 VARCHAR (50),
scared_22 VARCHAR (50),
scared_23 VARCHAR (50),
scared_24 VARCHAR (50),
scared_25 VARCHAR (50),
scared_26 VARCHAR (50),
scared_27 VARCHAR (50),
scared_28 VARCHAR (50),
scared_29 VARCHAR (50),
scared_30 VARCHAR (50),
scared_31 VARCHAR (50),
scared_32 VARCHAR (50),
scared_33 VARCHAR (50),
scared_34 VARCHAR (50),
scared_35 VARCHAR (50),
scared_36 VARCHAR (50),
scared_37 VARCHAR (50),
scared_38 VARCHAR (50),
scared_39 VARCHAR (50),
scared_40 VARCHAR (50),
scared_41 VARCHAR (50));




CREATE TABLE redcap_data.ATHENS(
    primary_key VARCHAR (20) PRIMARY KEY,
    athens_1 VARCHAR (50),
athens_2 VARCHAR (50),
athens_3 VARCHAR (50),
athens_4 VARCHAR (50),
athens_5 VARCHAR (50),
athens_6 VARCHAR (50),
athens_7 VARCHAR (50),
athens_8 VARCHAR (50));




CREATE TABLE redcap_data.SAS(
    primary_key VARCHAR (20) PRIMARY KEY,
    sas_timestamp VARCHAR (50),
sas_1 VARCHAR (50),
sas_2 VARCHAR (50),
sas_3 VARCHAR (50),
sas_4 VARCHAR (50),
sas_5 VARCHAR (50),
sas_6 VARCHAR (50),
sas_7 VARCHAR (50),
sas_8 VARCHAR (50),
sas_9 VARCHAR (50),
sas_10 VARCHAR (50),
sas_11 VARCHAR (50),
sas_12 VARCHAR (50),
sas_13 VARCHAR (50),
sas_14 VARCHAR (50),
sas_15 VARCHAR (50),
sas_16 VARCHAR (50),
sas_17 VARCHAR (50),
sas_18 VARCHAR (50),
sas_19 VARCHAR (50),
sas_20 VARCHAR (50),
sas_21 VARCHAR (50),
sas_22 VARCHAR (50),
sas_23 VARCHAR (50));




CREATE TABLE redcap_data.sci_af_ca(
    primary_key VARCHAR (20) PRIMARY KEY,
    sciafca_timestamp VARCHAR (50),
sci_af_ca_1 VARCHAR (50),
sci_af_ca_2 VARCHAR (50),
sci_af_ca_3 VARCHAR (50),
sci_af_ca_4 VARCHAR (50),
sci_af_ca_5 VARCHAR (50),
sci_af_ca_6 VARCHAR (50),
sci_af_ca_7 VARCHAR (50),
sci_af_ca_8 VARCHAR (50),
sci_af_ca_9 VARCHAR (50),
sci_af_ca_10 VARCHAR (50),
sci_af_ca_11 VARCHAR (50),
sci_af_ca_12 VARCHAR (50),
sci_af_ca_13 VARCHAR (50),
sci_af_ca_14 VARCHAR (50),
sci_af_ca_15 VARCHAR (50),
sci_af_ca_16 VARCHAR (50),
sci_af_ca_17 VARCHAR (50),
sci_af_ca_18 VARCHAR (50),
sci_af_ca_19 VARCHAR (50),
sci_af_ca_20 VARCHAR (50),
sci_af_ca_21 VARCHAR (50),
sci_af_ca_22 VARCHAR (50),
sci_af_ca_23 VARCHAR (50),
sci_af_ca_24 VARCHAR (50),
sci_af_ca_25 VARCHAR (50),
sci_af_ca_26 VARCHAR (50),
sci_af_ca_27 VARCHAR (50),
sci_af_ca_28 VARCHAR (50),
sci_af_ca_29 VARCHAR (50),
sci_af_ca_30 VARCHAR (50),
sci_af_ca_31 VARCHAR (50),
sci_af_ca_32 VARCHAR (50),
sci_af_ca_33 VARCHAR (50),
sci_af_ca_34 VARCHAR (50),
sci_af_ca_35 VARCHAR (50),
sci_af_ca_36 VARCHAR (50),
sci_af_ca_37 VARCHAR (50),
sci_af_ca_38 VARCHAR (50),
sci_af_ca_39 VARCHAR (50),
sci_af_ca_40 VARCHAR (50));




CREATE TABLE redcap_data.scs_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    sci_c_1_1_clin VARCHAR (50),
scs_2_1_clin VARCHAR (50),
scs_2_2_clin VARCHAR (50),
scs_2_3_clin VARCHAR (50),
scs_2_4_clin VARCHAR (50),
sci_c_3_1_clin VARCHAR (50),
sci_c_3_2_clin VARCHAR (50),
sci_c_3_3_clin VARCHAR (50),
sci_c_3_4_clin VARCHAR (50),
sci_c_4_1_clin VARCHAR (50),
sci_c_4_2_clin VARCHAR (50),
sci_c_4_3_clin VARCHAR (50),
sci_c_4_4_clin VARCHAR (50),
sci_c_5_1_clin VARCHAR (50),
sci_c_5_2_clin VARCHAR (50));




CREATE TABLE redcap_data.scs_stu(
    primary_key VARCHAR (20) PRIMARY KEY,
    sci_c_1_1_stu VARCHAR (50),
scs_2_1_stu VARCHAR (50),
scs_2_2_stu VARCHAR (50),
scs_2_3_stu VARCHAR (50),
scs_2_4_stu VARCHAR (50),
sci_c_3_1_stu VARCHAR (50),
sci_c_3_2_stu VARCHAR (50),
sci_c_3_3_stu VARCHAR (50),
sci_c_3_4_stu VARCHAR (50),
sci_c_4_1_stu VARCHAR (50),
sci_c_4_2_stu VARCHAR (50),
sci_c_4_3_stu VARCHAR (50),
sci_c_4_4_stu VARCHAR (50),
sci_c_5_1_stu VARCHAR (50),
sci_c_5_2_stu VARCHAR (50));




CREATE TABLE redcap_data.sci_mother(
    primary_key VARCHAR (20) PRIMARY KEY,
    scip_m_timestamp VARCHAR (50),
sci_p_1_m VARCHAR (50),
sci_p_2_m VARCHAR (50),
sci_p_3_m VARCHAR (50),
sci_p_4_m VARCHAR (50),
sci_p_5_m VARCHAR (50),
sci_p_6_m VARCHAR (50),
sci_p_7_m VARCHAR (50),
sci_p_8_m VARCHAR (50),
sci_p_9_m VARCHAR (50),
sci_p_10_m VARCHAR (50),
sci_p_11_m VARCHAR (50),
sci_p_12_m VARCHAR (50),
sci_p_13_m VARCHAR (50),
sci_p_14_m VARCHAR (50),
sci_p_15_m VARCHAR (50));




CREATE TABLE redcap_data.sci_father(
    primary_key VARCHAR (20) PRIMARY KEY,
    scip_f_timestamp VARCHAR (50),
sci_p_1_f VARCHAR (50),
sci_p_2_f VARCHAR (50),
sci_p_3_f VARCHAR (50),
sci_p_4_f VARCHAR (50),
sci_p_5_f VARCHAR (50),
sci_p_6_f VARCHAR (50),
sci_p_7_f VARCHAR (50),
sci_p_8_f VARCHAR (50),
sci_p_9_f VARCHAR (50),
sci_p_10_f VARCHAR (50),
sci_p_11_f VARCHAR (50),
sci_p_12_f VARCHAR (50),
sci_p_13_f VARCHAR (50),
sci_p_14_f VARCHAR (50),
sci_p_15_f VARCHAR (50));




CREATE TABLE redcap_data.ARI_P(
    primary_key VARCHAR (20) PRIMARY KEY,
    arippps_m_timestamp VARCHAR (50),
ari_p_1 VARCHAR (50),
ari_p_2 VARCHAR (50),
ari_p_3 VARCHAR (50),
ari_p_4 VARCHAR (50),
ari_p_5 VARCHAR (50),
ari_p_6 VARCHAR (50),
ari_p_7_m VARCHAR (50),
pps_1_m VARCHAR (50),
pps_2_m VARCHAR (50));




CREATE TABLE redcap_data.mast(
    primary_key VARCHAR (20) PRIMARY KEY,
    immirisk_adolescents_mast_athens_timestamp VARCHAR (50),
age VARCHAR (50),
mast_1 VARCHAR (50),
mast_2 VARCHAR (50),
mast_3 VARCHAR (50),
mast_4 VARCHAR (50),
mast_5 VARCHAR (50),
mast_6 VARCHAR (50),
mast_7 VARCHAR (50),
mast_8 VARCHAR (50),
mast_9 VARCHAR (50),
mast_10 VARCHAR (50),
mast_11 VARCHAR (50),
mast_12 VARCHAR (50),
mast_13 VARCHAR (50),
mast_14 VARCHAR (50),
mast_15 VARCHAR (50),
mast_16 VARCHAR (50),
mast_17 VARCHAR (50),
mast_18 VARCHAR (50),
mast_19 VARCHAR (50),
mast_20 VARCHAR (50),
mast_21 VARCHAR (50),
mast_22 VARCHAR (50),
mast_23 VARCHAR (50),
mast_24 VARCHAR (50),
mast_25 VARCHAR (50),
mast_26 VARCHAR (50),
mast_27 VARCHAR (50),
mast_28 VARCHAR (50),
mast_29 VARCHAR (50),
mast_30 VARCHAR (50));




CREATE TABLE redcap_data.maris_sci_sf(
    primary_key VARCHAR (20) PRIMARY KEY,
    marisscisf_timestamp VARCHAR (50),
age_childmaris_sci_sf_1 VARCHAR (50),
maris_sci_sf_2 VARCHAR (50),
maris_sci_sf_3 VARCHAR (50),
maris_sci_sf_4 VARCHAR (50),
maris_sci_sf_5 VARCHAR (50),
maris_sci_sf_6 VARCHAR (50),
maris_sci_sf_7 VARCHAR (50),
maris_sci_sf_8 VARCHAR (50),
maris_sci_sf_9 VARCHAR (50));




CREATE TABLE redcap_data.maris_soq_sf(
    primary_key VARCHAR (20) PRIMARY KEY,
    marissoqsf_timestamp VARCHAR (50),
maris_soq_sf_1 VARCHAR (50),
maris_soq_sf_2 VARCHAR (50),
maris_soq_sf_3 VARCHAR (50),
maris_soq_sf_4 VARCHAR (50),
maris_soq_sf_5 VARCHAR (50),
maris_soq_sf_6 VARCHAR (50),
maris_soq_sf_7 VARCHAR (50),
maris_soq_sf_8 VARCHAR (50));




CREATE TABLE redcap_data.swan_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    swan_m_timestamp VARCHAR (50),
swan_1_m VARCHAR (50),
swan_2_m VARCHAR (50),
swan_3_m VARCHAR (50),
swan_4_m VARCHAR (50),
swan_5_m VARCHAR (50),
swan_6_m VARCHAR (50),
swan_7_m VARCHAR (50),
swan_8_m VARCHAR (50),
swan_9_m VARCHAR (50),
swan_10_m VARCHAR (50),
swan_11_m VARCHAR (50),
swan_12_m VARCHAR (50),
swan_13_m VARCHAR (50),
swan_14_m VARCHAR (50),
swan_15_m VARCHAR (50),
swan_16_m VARCHAR (50),
swan_17_m VARCHAR (50),
swan_18_m VARCHAR (50));


CREATE TABLE redcap_data.dass_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    dass_f_timestamp VARCHAR (50),
dass_1_f VARCHAR (50),
dass_2_f VARCHAR (50),
dass_3_f VARCHAR (50),
dass_4_f VARCHAR (50),
dass_5_f VARCHAR (50),
dass_6_f VARCHAR (50),
dass_7_f VARCHAR (50),
dass_8_f VARCHAR (50),
dass_9_f VARCHAR (50),
dass_10_f VARCHAR (50),
dass_11_f VARCHAR (50),
dass_12_f VARCHAR (50),
dass_13_f VARCHAR (50),
dass_14_f VARCHAR (50),
dass_15_f VARCHAR (50),
dass_16_f VARCHAR (50),
dass_17_f VARCHAR (50),
dass_18_f VARCHAR (50),
dass_19_f VARCHAR (50),
dass_20_f VARCHAR (50),
dass_21_f VARCHAR (50));




CREATE TABLE redcap_data.ecr_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    ecr_f_timestamp VARCHAR (50),
ecr_1_f VARCHAR (50),
ecr_2_f VARCHAR (50),
ecr_3_f VARCHAR (50),
ecr_4_f VARCHAR (50),
ecr_5_f VARCHAR (50),
ecr_6_f VARCHAR (50),
ecr_7_f VARCHAR (50),
ecr_8_f VARCHAR (50),
ecr_9_f VARCHAR (50),
ecr_10_f VARCHAR (50),
ecr_11_f VARCHAR (50),
ecr_12_f VARCHAR (50),
ecr_13_f VARCHAR (50),
ecr_14_f VARCHAR (50),
ecr_15_f VARCHAR (50),
ecr_16_f VARCHAR (50),
ecr_17_f VARCHAR (50),
ecr_18_f VARCHAR (50),
ecr_19_f VARCHAR (50),
ecr_20_f VARCHAR (50),
ecr_21_f VARCHAR (50),
ecr_22_f VARCHAR (50),
ecr_23_f VARCHAR (50),
ecr_24_f VARCHAR (50),
ecr_25_f VARCHAR (50),
ecr_26_f VARCHAR (50),
ecr_27_f VARCHAR (50),
ecr_28_f VARCHAR (50),
ecr_29_f VARCHAR (50),
ecr_30_f VARCHAR (50),
ecr_31_f VARCHAR (50),
ecr_32_f VARCHAR (50),
ecr_33_f VARCHAR (50),
ecr_34_f VARCHAR (50),
ecr_35_f VARCHAR (50),
ecr_36_f VARCHAR (50));




CREATE TABLE redcap_data.trq_sf_maris_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    trqsfmarisclin_timestamp VARCHAR (50),
trq_sf_maris_1_clin VARCHAR (50),
trq_sf_maris_2_clin VARCHAR (50),
trq_sf_maris_3_clin VARCHAR (50),
trq_sf_maris_4_clin VARCHAR (50),
trq_sf_maris_5_clin VARCHAR (50),
trq_sf_maris_6_clin VARCHAR (50),
trq_sf_maris_7_clin VARCHAR (50),
trq_sf_maris_8_clin VARCHAR (50),
trq_sf_maris_9_clin VARCHAR (50),
trq_sf_maris_10_clin VARCHAR (50),
trq_sf_maris_11_clin VARCHAR (50),
trq_sf_maris_12_clin VARCHAR (50),
trq_sf_maris_13_clin VARCHAR (50),
trq_sf_maris_14_clin VARCHAR (50));




CREATE TABLE redcap_data.screening_form(
    primary_key VARCHAR (20) PRIMARY KEY,
    screening_form_timestamp VARCHAR (50),
screen_1 VARCHAR (50),
screen_2 VARCHAR (50),
screen_3 VARCHAR (50),
screen_10 VARCHAR (50),
screen_11 VARCHAR (50),
screen_12 VARCHAR (50),
screen_13 VARCHAR (50),
screen_14 VARCHAR (50),
screen_15 VARCHAR (50),
screen_16 VARCHAR (50),
screen_17 VARCHAR (50),
screen_18 VARCHAR (50),
screen_23 VARCHAR (50),
screen_24 VARCHAR (50),
screen_25 VARCHAR (50),
screen_26 VARCHAR (50),
screen_27 VARCHAR (50),
screen_28 VARCHAR (50),
screen_29 VARCHAR (50),
screen_30 VARCHAR (50),
screen_31 VARCHAR (50),
screen_32 VARCHAR (50),
screen_33 VARCHAR (50),
screen_35 VARCHAR (50),
screen_35_1 VARCHAR (50),
screen_36 VARCHAR (50),
screen_36_1 VARCHAR (50),
screen_37 VARCHAR (50),
screen_37_1 VARCHAR (50),
screen_38 VARCHAR (50),
screen_38_1 VARCHAR (50),
screen_39 VARCHAR (50),
screen_39_1 VARCHAR (50));




CREATE TABLE redcap_data.c_ssrs_fu_maya(
    primary_key VARCHAR (20) PRIMARY KEY,
    cssrs_fw_maya_timestamp VARCHAR (50),
c_ssrs_fu_thought_1_clin VARCHAR (50),
c_ssrs_fu_thought_2_clin VARCHAR (50),
c_ssrs_fu_thought_3_clin VARCHAR (50),
c_ssrs_fu_thought_4_clin VARCHAR (50),
c_ssrs_fu_thought_5_clin VARCHAR (50),
c_ssrs_fu_intensity_clin VARCHAR (50),
c_ssrs_fu_frequ_clin VARCHAR (50),
c_ssrs_fu_lengh_clin VARCHAR (50),
c_ssrs_fu_control_clin VARCHAR (50),
c_ssrs_fu_deter_clin VARCHAR (50),
c_ssrs_fu_reason_clin VARCHAR (50),
c_ssrs_fu_attemp_clin VARCHAR (50),
c_ssrs_fu_attemp_2_3_clin VARCHAR (50),
c_ssrs_fu_attemp_3_clin VARCHAR (50),
c_ssrs_fu_attemp_4_clin VARCHAR (50),
c_ssrs_fu_attemp_4_2_clin VARCHAR (50),
c_ssrs_fu_attemp_4_3_clin VARCHAR (50),
c_ssrs_fu_attemp_5_clin VARCHAR (50),
c_ssrs_fu_attemp_5_2_clin VARCHAR (50),
c_ssrs_fu_attemp_5_3_clin VARCHAR (50),
c_ssrs_fu_attemp_6_clin VARCHAR (50),
c_ssrs_fu_attemp_6_2_clin VARCHAR (50),
c_ssrs_fu_attemp_7_clin VARCHAR (50),
c_ssrs_fu_attemp_8_clin VARCHAR (50),
c_ssrs_fu_done_clin VARCHAR (50),
c_ssrs_fu_done_2_clin VARCHAR (50));


CREATE TABLE redcap_data.ARI_S(
    primary_key VARCHAR (20) PRIMARY KEY,
    aris_timestamp VARCHAR (50),
ari_s_1 VARCHAR (50),
ari_s_2 VARCHAR (50),
ari_s_3 VARCHAR (50),
ari_s_4 VARCHAR (50),
ari_s_5 VARCHAR (50),
ari_s_6 VARCHAR (50),
ari_s_7 VARCHAR (50));




CREATE TABLE redcap_data.opening(
    primary_key VARCHAR (20) PRIMARY KEY,
    opening_timestamp VARCHAR (50),
id VARCHAR (50),
er_num VARCHAR (50),
complaint___1 VARCHAR (50),
complaint___2 VARCHAR (50),
complaint___3 VARCHAR (50),
complaint___4 VARCHAR (50),
complaint___5 VARCHAR (50),
complaint___6 VARCHAR (50),
complaint_other VARCHAR (50),
complaint_date VARCHAR (50),
diagnosis___1 VARCHAR (50),
diagnosis___2 VARCHAR (50),
diagnosis___3 VARCHAR (50),
diagnosis___4 VARCHAR (50),
diagnosis___5 VARCHAR (50),
diagnosis___6 VARCHAR (50),
diagnosis___7 VARCHAR (50),
diagnosis___8 VARCHAR (50),
diagnosis___9 VARCHAR (50),
diagnosis___10 VARCHAR (50),
diagnosis___11 VARCHAR (50),
diagnosis___12 VARCHAR (50),
diagnosis___13 VARCHAR (50),
diagnosis___14 VARCHAR (50),
diagnosis_other VARCHAR (50),
opening_psychothe VARCHAR (50),
opening_psychothe_2___1 VARCHAR (50),
opening_psychothe_2___2 VARCHAR (50),
opening_psychothe_2___3 VARCHAR (50),
opening_psychothe_2___4 VARCHAR (50),
opening_psychothe_2___5 VARCHAR (50),
opening_psychothe_2___6 VARCHAR (50),
opening_psychothe_2___7 VARCHAR (50),
opening_psychothe_3 VARCHAR (50),
opening_medicine VARCHAR (50),
opening_medicine_2___1 VARCHAR (50),
opening_medicine_2___2 VARCHAR (50),
opening_medicine_2___3 VARCHAR (50),
opening_medicine_2___4 VARCHAR (50),
opening_medicine_2___5 VARCHAR (50),
opening_medicine_3 VARCHAR (50),
group___1 VARCHAR (50),
group___2 VARCHAR (50),
group___3 VARCHAR (50),
consent VARCHAR (50),
consent_no VARCHAR (50));




CREATE TABLE redcap_data.covid19(
    primary_key VARCHAR (20) PRIMARY KEY,
    covid19_timestamp VARCHAR (50),
covid_1___1 VARCHAR (50),
covid_1___2 VARCHAR (50),
covid_1___3 VARCHAR (50),
covid_1___4 VARCHAR (50),
covid_2 VARCHAR (50),
covid_3___1 VARCHAR (50),
covid_3___2 VARCHAR (50),
covid_3___3 VARCHAR (50),
covid_3___4 VARCHAR (50),
covid_3___5 VARCHAR (50),
covid_3___6 VARCHAR (50),
covid_3___7 VARCHAR (50),
covid_3___8 VARCHAR (50),
covid_4 VARCHAR (50),
covid_5 VARCHAR (50),
covid_6 VARCHAR (50),
covid_7 VARCHAR (50),
covid_8 VARCHAR (50));




CREATE TABLE redcap_data.opening_child_pre(
    primary_key VARCHAR (20) PRIMARY KEY,
    opening_child_pre_timestamp VARCHAR (50),
age_child_pre VARCHAR (50),
gender VARCHAR (50));




CREATE TABLE redcap_data.erc_rc(
    primary_key VARCHAR (20) PRIMARY KEY,
    ecrrc_timestamp VARCHAR (50),
erc_rc_1 VARCHAR (50),
erc_rc_2 VARCHAR (50),
erc_rc_3 VARCHAR (50),
erc_rc_4 VARCHAR (50),
erc_rc_5 VARCHAR (50),
erc_rc_6 VARCHAR (50),
erc_rc_7 VARCHAR (50),
erc_rc_8 VARCHAR (50),
erc_rc_9 VARCHAR (50),
erc_rc_10 VARCHAR (50),
erc_rc_11 VARCHAR (50),
erc_rc_12 VARCHAR (50));




CREATE TABLE redcap_data.piu_cyberbulling(
    primary_key VARCHAR (20) PRIMARY KEY,
    piu_cyberbulling_timestamp VARCHAR (50),
piu_1 VARCHAR (50),
piu_2 VARCHAR (50),
piu_3 VARCHAR (50),
piu_4 VARCHAR (50),
piu_5 VARCHAR (50),
piu_6 VARCHAR (50),
cyberbulling_1 VARCHAR (50),
cyberbulling_2 VARCHAR (50),
cyberbulling_3 VARCHAR (50),
cyberbulling_4 VARCHAR (50),
cyberbulling_5 VARCHAR (50),
cyberbulling_6 VARCHAR (50),
cyberbulling_7 VARCHAR (50),
cyberbulling_8 VARCHAR (50),
cyberbulling_9 VARCHAR (50),
cyberbulling_10 VARCHAR (50),
cyberbulling_11 VARCHAR (50),
bullied_1 VARCHAR (50),
bullied_2 VARCHAR (50),
bullied_3 VARCHAR (50),
bullied_4 VARCHAR (50));




CREATE TABLE redcap_data.erq_ca(
    primary_key VARCHAR (20) PRIMARY KEY,
    erqca_timestamp VARCHAR (50),
erq_ca_1 VARCHAR (50),
erq_ca_2 VARCHAR (50),
erq_ca_3 VARCHAR (50),
erq_ca_4 VARCHAR (50),
erq_ca_5 VARCHAR (50),
erq_ca_6 VARCHAR (50),
erq_ca_7 VARCHAR (50),
erq_ca_8 VARCHAR (50),
erq_ca_9 VARCHAR (50),
erq_ca_10 VARCHAR (50));




CREATE TABLE redcap_data.ders(
    primary_key VARCHAR (20) PRIMARY KEY,
    ders_timestampders_1 VARCHAR (50),
ders_2 VARCHAR (50),
ders_3 VARCHAR (50),
ders_4 VARCHAR (50),
ders_5 VARCHAR (50),
ders_6 VARCHAR (50),
ders_7 VARCHAR (50),
ders_8 VARCHAR (50),
ders_9 VARCHAR (50),
ders_10 VARCHAR (50),
ders_11 VARCHAR (50),
ders_12 VARCHAR (50),
ders_13 VARCHAR (50),
ders_14 VARCHAR (50),
ders_15 VARCHAR (50),
ders_16 VARCHAR (50),
ders_17 VARCHAR (50),
ders_18 VARCHAR (50),
ders_19 VARCHAR (50),
ders_20 VARCHAR (50),
ders_21 VARCHAR (50),
ders_22 VARCHAR (50),
ders_23 VARCHAR (50),
ders_24 VARCHAR (50),
ders_25 VARCHAR (50),
ders_26 VARCHAR (50),
ders_27 VARCHAR (50),
ders_28 VARCHAR (50),
ders_29 VARCHAR (50),
ders_30 VARCHAR (50),
ders_31 VARCHAR (50),
ders_32 VARCHAR (50),
ders_33 VARCHAR (50),
ders_34 VARCHAR (50),
ders_35 VARCHAR (50),
ders_36 VARCHAR (50));




CREATE TABLE redcap_data.wai(
    primary_key VARCHAR (20) PRIMARY KEY,
    wai_timestamp VARCHAR (50),
wai_1wai_2 VARCHAR (50),
wai_3 VARCHAR (50),
wai_4 VARCHAR (50),
wai_5 VARCHAR (50),
wai_6 VARCHAR (50),
wai_7 VARCHAR (50),
wai_8 VARCHAR (50),
wai_9 VARCHAR (50),
wai_10 VARCHAR (50),
wai_11 VARCHAR (50),
wai_12 VARCHAR (50));




CREATE TABLE redcap_data.cshq_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    cshq_m_timestamp VARCHAR (50),
age_cshq_m VARCHAR (50),
bedtime_1_m VARCHAR (50),
bedtime_2_m VARCHAR (50),
bedtime_3_m VARCHAR (50),
dtime_4_m VARCHAR (50),
dtime_5_m VARCHAR (50),
bedtime_6_m VARCHAR (50),
bedtime_7_m VARCHAR (50),
bedtime_8_m VARCHAR (50),
bedtime_9_m VARCHAR (50),
bedtime_10_m VARCHAR (50),
duration_1_m VARCHAR (50),
duration_2_m VARCHAR (50),
duration_3_m VARCHAR (50),
duration_4_m VARCHAR (50),
duration_5_m VARCHAR (50),
duration_6_m VARCHAR (50),
duration_7_m VARCHAR (50),
duration_8_m VARCHAR (50),
duration_9_m VARCHAR (50),
duration_10_m VARCHAR (50),
duration_11_m VARCHAR (50),
duration_12_m VARCHAR (50),
duration_13_m VARCHAR (50),
duration_14_m VARCHAR (50),
duration_15_m VARCHAR (50),
night_wake_1_m VARCHAR (50),
night_wake_2_m VARCHAR (50),
night_wake_3_m VARCHAR (50),
day_wake_1_m VARCHAR (50),
day_wake_2_m VARCHAR (50),
day_wake_3_m VARCHAR (50),
day_wake_4_m VARCHAR (50),
day_wake_5_m VARCHAR (50),
day_wake_6_m VARCHAR (50),
sleepiness_1_m VARCHAR (50),
sleepiness_2_m VARCHAR (50),
daytime_sleepiness_3_m VARCHAR (50));




CREATE TABLE redcap_data.sdq_parents_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    sdq_parents_m_timestamp VARCHAR (50),
sdq_1_parents_m VARCHAR (50),
sdq_2_parents_m VARCHAR (50),
sdq_3_parents_m VARCHAR (50),
sdq_4_parents_m VARCHAR (50),
sdq_5_parents_m VARCHAR (50),
sdq_6_parents_m VARCHAR (50),
sdq_7_parents_m VARCHAR (50),
sdq_8_parents_m VARCHAR (50),
sdq_9_parents_m VARCHAR (50),
sdq_10_parents_m VARCHAR (50),
sdq_11_parents_m VARCHAR (50),
sdq_12_parents_m VARCHAR (50),
sdq_13_parents_m VARCHAR (50),
sdq_14_parents_m VARCHAR (50),
sdq_15_parents_m VARCHAR (50),
sdq_16_parents_m VARCHAR (50),
sdq_17_parents_m VARCHAR (50),
sdq_18_parents_m VARCHAR (50),
sdq_19_parents_m VARCHAR (50),
sdq_20_parents_m VARCHAR (50),
sdq_21_parents_m VARCHAR (50),
sdq_22_parents_m VARCHAR (50),
sdq_23_parents_m VARCHAR (50),
sdq_24_parents_m VARCHAR (50),
sdq_25_parents_m VARCHAR (50),
sdq_26_parents_m VARCHAR (50),
sdq_27_parents_m VARCHAR (50),
sdq_28_parents_m VARCHAR (50),
sdq_29_parents_1_m VARCHAR (50),
sdq_29_parents_2_m VARCHAR (50),
sdq_29_parents_3_m VARCHAR (50),
sdq_29_parents_4_m VARCHAR (50),
sdq_30_parents_m VARCHAR (50));




CREATE TABLE redcap_data.ders_p_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    ders_p_m_timestamp VARCHAR (50),
ders_1_p_m VARCHAR (50),
ders_2_p_m VARCHAR (50),
ders_3_p_m VARCHAR (50),
ders_4_p_m VARCHAR (50),
ders_5_p_m VARCHAR (50),
ders_6_p_m VARCHAR (50),
ders_7_p_m VARCHAR (50),
ders_8_p_m VARCHAR (50),
ders_9_p_m VARCHAR (50),
ders_10_p_m VARCHAR (50),
ders_11_p_m VARCHAR (50),
ders_12_p_m VARCHAR (50),
ders_13_p_m VARCHAR (50),
ders_14_p_m VARCHAR (50),
ders_15_p_m VARCHAR (50),
ders_16_p_m VARCHAR (50),
ders_17_p_m VARCHAR (50),
ders_18_p_m VARCHAR (50),
ders_19_p_m VARCHAR (50),
ders_20_p_m VARCHAR (50),
ders_21_p_m VARCHAR (50),
ders_22_p_m VARCHAR (50),
ders_23_p_m VARCHAR (50),
ders_24_p_m VARCHAR (50),
ders_25_p_m VARCHAR (50),
ders_26_p_m VARCHAR (50),
ders_27_p_m VARCHAR (50),
ders_28_p_m VARCHAR (50),
ders_29_p_m VARCHAR (50),
ders_30_p_m VARCHAR (50),
ders_31_p_m VARCHAR (50),
ders_32_p_m VARCHAR (50),
ders_33_p_m VARCHAR (50),
ders_34_p_m VARCHAR (50),
ders_35_p_m VARCHAR (50),
ders_36_p_m VARCHAR (50));




CREATE TABLE redcap_data.ecr_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    ecr_m_timestamp VARCHAR (50),
ecr_1_m VARCHAR (50),
ecr_2_m VARCHAR (50),
ecr_3_m VARCHAR (50),
ecr_4_m VARCHAR (50),
ecr_5_m VARCHAR (50),
ecr_6_m VARCHAR (50),
ecr_7_m VARCHAR (50),
ecr_8_m VARCHAR (50),
ecr_9_m VARCHAR (50),
ecr_10_m VARCHAR (50),
ecr_11_m VARCHAR (50),
ecr_12_m VARCHAR (50),
ecr_13_m VARCHAR (50),
ecr_14_m VARCHAR (50),
ecr_15_m VARCHAR (50),
ecr_16_m VARCHAR (50),
ecr_17_m VARCHAR (50),
ecr_18_m VARCHAR (50),
ecr_19_m VARCHAR (50),
ecr_20_m VARCHAR (50),
ecr_21_m VARCHAR (50),
ecr_22_m VARCHAR (50),
ecr_23_m VARCHAR (50),
ecr_24_m VARCHAR (50),
ecr_25_m VARCHAR (50),
ecr_26_m VARCHAR (50),
ecr_27_m VARCHAR (50),
ecr_28_m VARCHAR (50),
ecr_29_m VARCHAR (50),
ecr_30_m VARCHAR (50),
ecr_31_m VARCHAR (50),
ecr_32_m VARCHAR (50),
ecr_33_m VARCHAR (50),
ecr_34_m VARCHAR (50),
ecr_35_m VARCHAR (50),
ecr_36_m VARCHAR (50));




CREATE TABLE redcap_data.cshq_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    cshq_f_timestamp VARCHAR (50),
age_cshq_f VARCHAR (50),
bedtime_1_f VARCHAR (50),
bedtime_2_f VARCHAR (50),
bedtime_3_f VARCHAR (50),
bedtime_4_f VARCHAR (50),
bedtime_5_f VARCHAR (50),
bedtime_6_f VARCHAR (50),
bedtime_7_f VARCHAR (50),
bedtime_8_f VARCHAR (50),
bedtime_9_f VARCHAR (50),
bedtime_10_f VARCHAR (50),
duration_1_f VARCHAR (50),
duration_2_f VARCHAR (50),
duration_3_f VARCHAR (50),
duration_4_f VARCHAR (50),
duration_5_f VARCHAR (50),
duration_6_f VARCHAR (50),
duration_7_f VARCHAR (50),
duration_8_f VARCHAR (50),
duration_9_f VARCHAR (50),
duration_10_f VARCHAR (50),
duration_11_f VARCHAR (50),
duration_12_f VARCHAR (50),
duration_13_f VARCHAR (50),
duration_14_f VARCHAR (50),
duration_15_f VARCHAR (50),
night_wake_1_f VARCHAR (50),
night_wake_2_f VARCHAR (50),
night_wake_3_f VARCHAR (50),
day_wake_1_f VARCHAR (50),
day_wake_2_f VARCHAR (50),
day_wake_3_f VARCHAR (50),
day_wake_4_f VARCHAR (50),
day_wake_5_f VARCHAR (50),
day_wake_6_f VARCHAR (50),
sleepiness_1_f VARCHAR (50),
sleepiness_2_f VARCHAR (50),
daytime_sleepiness_3_f VARCHAR (50));




CREATE TABLE redcap_data.erq_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    erq_f_timestamp VARCHAR (50),
erq_1_f VARCHAR (50),
erq_2_f VARCHAR (50),
erq_3_f VARCHAR (50),
erq_4_f VARCHAR (50),
erq_5_f VARCHAR (50),
erq_6_f VARCHAR (50),
erq_7_f VARCHAR (50),
erq_8_f VARCHAR (50),
erq_9_f VARCHAR (50),
erq_10_f VARCHAR (50));




CREATE TABLE redcap_data.ARI_P_F(
    primary_key VARCHAR (20) PRIMARY KEY,
    arippps_f_timestamp VARCHAR (50),
ari_p_1_f VARCHAR (50),
ari_p_2_f VARCHAR (50),
ari_p_3_f VARCHAR (50),
ari_p_4_f VARCHAR (50),
ari_p_5_f VARCHAR (50),
ari_p_6_f VARCHAR (50),
ari_p_7_f VARCHAR (50),
pps_1_f VARCHAR (50),
pps_2_f VARCHAR (50));




CREATE TABLE redcap_data.wai_immirisk_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    wai_immirisk_clin_timestamp VARCHAR (50),
wai_t_immi_1_clin VARCHAR (50),
wai_t_immi_2_clin VARCHAR (50),
wai_t_immi_3_clin VARCHAR (50),
wai_t_immi_4_clin VARCHAR (50),
wai_t_immi_5_clin VARCHAR (50),
wai_t_immi_6_clin VARCHAR (50),
wai_t_immi_7_clin VARCHAR (50),
wai_t_immi_8_clin VARCHAR (50),
wai_t_immi_9_clin VARCHAR (50),
wai_t_immi_10_clin VARCHAR (50),
wai_t_immi_11_clin VARCHAR (50),
wai_t_immi_12_clin VARCHAR (50));




CREATE TABLE redcap_data.remote_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    remote_clin_timestamp VARCHAR (50),
remote_1_clin VARCHAR (50));




CREATE TABLE redcap_data.er_questionnaire_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    er_questionnaire_clin_timestamp VARCHAR (50),
er_id VARCHAR (50),
er_name_clin VARCHAR (50),
er_date_of_birth_clin VARCHAR (50),
er_id_clin VARCHAR (50),
er_arrival_clin VARCHAR (50),
er_reason_clin VARCHAR (50),
er_attemp_time_clin VARCHAR (50),
er_planned_clin VARCHAR (50),
er_regret_clin VARCHAR (50),
er_cut_first_clin VARCHAR (50),
er_thoughts_clin VARCHAR (50),
er_worst_thoughts_clin VARCHAR (50),
er_thoughts_now_clin VARCHAR (50),
er_medicine_clin VARCHAR (50),
er_medicine_what_clin VARCHAR (50),
er_medicine_mg_clin VARCHAR (50));




CREATE TABLE redcap_data.suicide_form_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    suicide_form_clin_timestamp VARCHAR (50),
suiciform_time_clin VARCHAR (50),
medhis_1_clin VARCHAR (50),
medhis_1_1_clin VARCHAR (50),
medhis_2_clin VARCHAR (50),
medhis_2_1_clin VARCHAR (50),
medhis_3_clin VARCHAR (50),
medhis_3_1_clin VARCHAR (50),
medhis_4_clin VARCHAR (50),
medhis_4_1_clin VARCHAR (50),
medhis_5_clin VARCHAR (50),
medhis_5_1_clin VARCHAR (50),
medhis_6_clin VARCHAR (50),
medhis_6_1_clin VARCHAR (50),
medhis_7_clin VARCHAR (50),
medhis_7_1_clin VARCHAR (50),
medhis_8_clin VARCHAR (50),
medhis_8_1_clin VARCHAR (50),
medhis_9_clin VARCHAR (50),
medhis_9_1_clin VARCHAR (50),
medhis_10_clin VARCHAR (50),
medhis_10_1_clin VARCHAR (50),
medhis_11_clin VARCHAR (50),
medhis_11_1_clin VARCHAR (50),
medhis_12_clin VARCHAR (50),
medhis_12_1_clin VARCHAR (50),
medhis_13_clin VARCHAR (50),
medhis_13_1_clin VARCHAR (50),
medhis_details_clin VARCHAR (50),
diet_1_clin VARCHAR (50),
diet_1_1_clin VARCHAR (50),
diet_2_clin VARCHAR (50),
diet_2_1_clin VARCHAR (50),
diet_3_clin VARCHAR (50),
diet_3_1_clin VARCHAR (50),
diet_4_clin VARCHAR (50),
diet_4_1_clin VARCHAR (50),
diet_5_clin VARCHAR (50),
diet_5_1_clin VARCHAR (50),
medhis_clin VARCHAR (50),
inclusion_1_clin VARCHAR (50),
inclusion_2_clin VARCHAR (50),
exclusion_1_clin VARCHAR (50),
exclusion_2_clin VARCHAR (50),
exclusion_3_clin VARCHAR (50),
exclusion_4_clin VARCHAR (50),
exclusion_5_clin VARCHAR (50),
exclusion_6_clin VARCHAR (50),
week_1_clin VARCHAR (50),
week_1_1_clin VARCHAR (50),
week_2_clin VARCHAR (50),
week_2_1_clin VARCHAR (50),
week_3_clin VARCHAR (50),
week_medic_clin VARCHAR (50),
three_mon_1_clin VARCHAR (50),
three_mon_1_1_clin VARCHAR (50),
three_mon_2_clin VARCHAR (50),
three_mon_2_1_clin VARCHAR (50),
three_mon_3_clin VARCHAR (50),
three_mon_medic_clin VARCHAR (50),
six_mon_1_clin VARCHAR (50),
six_mon_1_1_clin VARCHAR (50),
six_mon_2_clin VARCHAR (50),
six_mon_2_1_clin VARCHAR (50),
six_mon_3_clin VARCHAR (50),
six_mon_medic_clin VARCHAR (50),
twelve_mon_1_clin VARCHAR (50),
twelve_mon_1_1_clin VARCHAR (50),
twelve_mon_2_clin VARCHAR (50),
twelve_mon_2_1_clin VARCHAR (50),
twelve_mon_3_clin VARCHAR (50),
twelve_mon_medic_clin VARCHAR (50));




CREATE TABLE redcap_data.mini_kid_sum_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    mini_kid_sum_clin_timestamp VARCHAR (50),
mini_class_clin VARCHAR (50),
mini_date_clin VARCHAR (50),
mini_interviewer_clin VARCHAR (50),
mini_date_interview_clin VARCHAR (50),
mini_medication_clin___1 VARCHAR (50),
mini_medication_clin___2 VARCHAR (50),
mini_medication_clin___3 VARCHAR (50),
mini_medication_clin___4 VARCHAR (50),
mini_medication_clin___5 VARCHAR (50),
mini_medicine_other_clin VARCHAR (50),
mini_start_time_clin VARCHAR (50),
mini_end_time_clin VARCHAR (50),
mini_total_time_clin VARCHAR (50),
depres_clin___1 VARCHAR (50),
depres_clin___2 VARCHAR (50),
depres_clin___3 VARCHAR (50),
suicide_clin___1 VARCHAR (50),
suicide_clin___2 VARCHAR (50),
suicide_risk_clin VARCHAR (50),
dysthemia_clin___1 VARCHAR (50),
manic_clin___1 VARCHAR (50),
manic_clin___2 VARCHAR (50),
hypomania_clin___1 VARCHAR (50),
hypomania_clin___2 VARCHAR (50),
bipolar_i_clin___1 VARCHAR (50),
bipolar_i_clin___2 VARCHAR (50),
bipolar_ii_clin___1 VARCHAR (50),
bipolar_ii_clin___2 VARCHAR (50),
bipolar_unclassified_clin___1 VARCHAR (50),
bipolar_unclassified_clin___2 VARCHAR (50),
panic_clin___1 VARCHAR (50),
panic_clin___2 VARCHAR (50),
agoraphobia_clin___1 VARCHAR (50),
separation_anxiety_clin___1 VARCHAR (50),
social_anxiety_clin___1 VARCHAR (50),
social_anxiety_clin___2 VARCHAR (50),
social_anxiety_clin___3 VARCHAR (50),
phobia_clin___1 VARCHAR (50),
ocd_clin___1 VARCHAR (50),
ptsd_clin___1 VARCHAR (50),
alcohol_depend_clin___1 VARCHAR (50),
alcohol_use_clin___1 VARCHAR (50),
drug_depend_clin___1 VARCHAR (50),
drug_use_clin___1 VARCHAR (50),
tourette_clin___1 VARCHAR (50),
motor_tics_clin___1 VARCHAR (50),
vocal_tics_clin___1 VARCHAR (50),
transient_tics_clin___1 VARCHAR (50),
adhd_mix_clin___1 VARCHAR (50),
adhd_attention_clin___1 VARCHAR (50),
adhd_hyper_clin___1 VARCHAR (50),
conduct_clin___1 VARCHAR (50),
odd_clin___1 VARCHAR (50),
psychotic_clin___1 VARCHAR (50),
psychotic_clin___2 VARCHAR (50),
affect_psychotic_clin___1 VARCHAR (50),
affect_psychotic_clin___2 VARCHAR (50),
anorexia_clin___1 VARCHAR (50),
bulimia_clin___1 VARCHAR (50),
anorexia_bulmus_clin___1 VARCHAR (50),
gad_clin___1 VARCHAR (50),
adjustment_clin___1 VARCHAR (50),
organic_clin VARCHAR (50),
development_clin___1 VARCHAR (50),
main_dianose_clin VARCHAR (50));




CREATE TABLE redcap_data.trq_sf_maris_stu(
    primary_key VARCHAR (20) PRIMARY KEY,
    trqsfmaris_stu_timestamp VARCHAR (50),
trq_sf_maris_1_stu VARCHAR (50),
trq_sf_maris_2_stu VARCHAR (50),
trq_sf_maris_3_stu VARCHAR (50),
trq_sf_maris_4_stu VARCHAR (50),
trq_sf_maris_5_stu VARCHAR (50),
trq_sf_maris_6_stu VARCHAR (50),
trq_sf_maris_7_stu VARCHAR (50),
trq_sf_maris_8_stu VARCHAR (50),
trq_sf_maris_9_stu VARCHAR (50),
trq_sf_maris_10_stu VARCHAR (50),
trq_sf_maris_11_stu VARCHAR (50),
trq_sf_maris_12_stu VARCHAR (50),
trq_sf_maris_13_stu VARCHAR (50),
trq_sf_maris_14_stu VARCHAR (50));




CREATE TABLE redcap_data.erq_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    erq_m_timestamp VARCHAR (50),
erq_1_m VARCHAR (50),
erq_2_m VARCHAR (50),
erq_3_m VARCHAR (50),
erq_4_m VARCHAR (50),
erq_5_m VARCHAR (50),
erq_6_m VARCHAR (50),
erq_7_m VARCHAR (50),
erq_8_m VARCHAR (50),
erq_9_m VARCHAR (50),
erq_10_m VARCHAR (50));




CREATE TABLE redcap_data.cts_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    cts_m_timestamp VARCHAR (50),
cts_p_1_m VARCHAR (50),
cts_p_2_m VARCHAR (50),
cts_p_3_m VARCHAR (50),
cts_p_4_m VARCHAR (50),
cts_p_4_1_m VARCHAR (50));




CREATE TABLE redcap_data.moas_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    moas_m_timestamp VARCHAR (50),
moas_0_m VARCHAR (50),
moas_1_m VARCHAR (50),
moas_2_m VARCHAR (50),
moas_3_m VARCHAR (50),
moas_4_m VARCHAR (50),
moas_5_m VARCHAR (50),
moas_6_m VARCHAR (50),
moas_7_m VARCHAR (50),
moas_8_m VARCHAR (50),
moas_9_m VARCHAR (50),
moas_10_m VARCHAR (50),
moas_11_m VARCHAR (50),
moas_12_m VARCHAR (50),
moas_13_m VARCHAR (50),
moas_14_m VARCHAR (50),
moas_15_m VARCHAR (50),
moas_16_m VARCHAR (50),
moas_17_m VARCHAR (50),
moas_18_m VARCHAR (50),
moas_19_m VARCHAR (50),
moas_20_m VARCHAR (50));




CREATE TABLE redcap_data.ending_parent_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    ending_parent_m_timestamp VARCHAR (50),
therapy_child_2_m VARCHAR (50),
ending_childparent_m VARCHAR (50));




CREATE TABLE redcap_data.opening_parents_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    opening_parents_f_timestamp VARCHAR (50),
who_fills_out_f VARCHAR (50),
who_fills_out_2_f VARCHAR (50));




CREATE TABLE redcap_data.sdq_parents_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    sdq_parents_f_timestamp VARCHAR (50),
sdq_1_parents_f VARCHAR (50),
sdq_2_parents_f VARCHAR (50),
sdq_3_parents_f VARCHAR (50),
sdq_4_parents_f VARCHAR (50),
sdq_5_parents_f VARCHAR (50),
sdq_6_parents_f VARCHAR (50),
sdq_7_parents_f VARCHAR (50),
sdq_8_parents_f VARCHAR (50),
sdq_9_parents_f VARCHAR (50),
sdq_10_parents_f VARCHAR (50),
sdq_11_parents_f VARCHAR (50),
sdq_12_parents_f VARCHAR (50),
sdq_13_parents_f VARCHAR (50),
sdq_14_parents_f VARCHAR (50),
sdq_15_parents_f VARCHAR (50),
sdq_16_parents_f VARCHAR (50),
sdq_17_parents_f VARCHAR (50),
sdq_18_parents_f VARCHAR (50),
sdq_19_parents_f VARCHAR (50),
sdq_20_parents_f VARCHAR (50),
sdq_21_parents_f VARCHAR (50),
sdq_22_parents_f VARCHAR (50),
sdq_23_parents_f VARCHAR (50),
sdq_24_parents_f VARCHAR (50),
sdq_25_parents_f VARCHAR (50),
sdq_26_parents_f VARCHAR (50),
sdq_27_parents_f VARCHAR (50),
sdq_28_parents_f VARCHAR (50),
sdq_29_parents_1_f VARCHAR (50),
sdq_29_parents_2_f VARCHAR (50),
sdq_29_parents_3_f VARCHAR (50),
sdq_29_parents_4_f VARCHAR (50),
sdq_30_parents_f VARCHAR (50));




CREATE TABLE redcap_data.ders_p_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    ders_p_f_timestamp VARCHAR (50),
ders_1_p_f VARCHAR (50),
ders_2_p_f VARCHAR (50),
ders_3_p_f VARCHAR (50),
ders_4_p_f VARCHAR (50),
ders_5_p_f VARCHAR (50),
ders_6_p_f VARCHAR (50),
ders_7_p_f VARCHAR (50),
ders_8_p_f VARCHAR (50),
ders_9_p_f VARCHAR (50),
ders_10_p_f VARCHAR (50),
ders_11_p_f VARCHAR (50),
ders_12_p_f VARCHAR (50),
ders_13_p_f VARCHAR (50),
ders_14_p_f VARCHAR (50),
ders_15_p_f VARCHAR (50),
ders_16_p_f VARCHAR (50),
ders_17_p_f VARCHAR (50),
ders_18_p_f VARCHAR (50),
ders_19_p_f VARCHAR (50),
ders_20_p_f VARCHAR (50),
ders_21_p_f VARCHAR (50),
ders_22_p_f VARCHAR (50),
ders_23_p_f VARCHAR (50),
ders_24_p_f VARCHAR (50),
ders_25_p_f VARCHAR (50),
ders_26_p_f VARCHAR (50),
ders_27_p_f VARCHAR (50),
ders_28_p_f VARCHAR (50),
ders_29_p_f VARCHAR (50),
ders_30_p_f VARCHAR (50),
ders_31_p_f VARCHAR (50),
ders_32_p_f VARCHAR (50),
ders_33_p_f VARCHAR (50),
ders_34_p_f VARCHAR (50),
ders_35_p_f VARCHAR (50),
ders_36_p_f VARCHAR (50));




CREATE TABLE redcap_data.cdrsr_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    cdrsr_clin_timestamp VARCHAR (50),
cdrs_impaired_schoolwork_clin VARCHAR (50),
cdrs_difficulty_having_fun_clin VARCHAR (50),
sdrs_social_withdrawal_clin VARCHAR (50),
cdrs_sleep_disturbance_clin VARCHAR (50),
cdrs_sleep_disturbance_2_clin VARCHAR (50),
cdrs_appetite_disturbance_clin VARCHAR (50),
cdrs_appetite_disturbance_2_clin VARCHAR (50),
cdrs_excessive_fatigue_clin VARCHAR (50),
cdrs_physical_complaints_clin VARCHAR (50),
sdrs_irritability_clin VARCHAR (50),
cdrs_excessive_guilt_clin VARCHAR (50),
cdrs_low_self_esteem_clin VARCHAR (50),
cdrs_depressed_feelings_clin VARCHAR (50),
cdrs_morbid_ideation_clin VARCHAR (50),
cdrs_suicidal_ideation_clin VARCHAR (50),
cdrs_excessive_weeping_clin VARCHAR (50),
cdrs_depressed_facial_affect_clin VARCHAR (50),
cdrs_listless_speech_clin VARCHAR (50),
cdrs_hypoactivity_clin VARCHAR (50),
cdrs_sum_clin VARCHAR (50));




CREATE TABLE redcap_data.ffq(
    primary_key VARCHAR (20) PRIMARY KEY,
    ffq_sum_timestamp VARCHAR (50),
ffq_sum VARCHAR (50));




CREATE TABLE redcap_data.opening_students(
    primary_key VARCHAR (20) PRIMARY KEY,
    opening_students_timestamp VARCHAR (50),
who_stu VARCHAR (50),
who_other_stu VARCHAR (50),
name_stu VARCHAR (50));




CREATE TABLE redcap_data.cgi_s_stu(
    primary_key VARCHAR (20) PRIMARY KEY,
    cgi_s_base_stu VARCHAR (50),
cgi_s_stu_complete VARCHAR (50));




CREATE TABLE redcap_data.remote_stu(
    primary_key VARCHAR (20) PRIMARY KEY,
    remote_stu_timestamp VARCHAR (50),
remote_1_stu VARCHAR (50));




CREATE TABLE redcap_data.cps_stu(
    primary_key VARCHAR (20) PRIMARY KEY,
    cps_stu_timestamp VARCHAR (50),
cps_1_stu VARCHAR (50),
cps_2_stu VARCHAR (50));




CREATE TABLE redcap_data.cps_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    cps_clin_timestamp VARCHAR (50),
cps_1_clin VARCHAR (50),
cps_2_clin VARCHAR (50));




CREATE TABLE redcap_data.cgi_s_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    cgi_s_clin_timestamp VARCHAR (50),
cgi_s_base_clin VARCHAR (50));




CREATE TABLE redcap_data.opening_therapist_battery(
    primary_key VARCHAR (20) PRIMARY KEY,
    opening_therapist_battery_timestamp VARCHAR (50),
time_clin VARCHAR (50),
parents_safety_plan_clin VARCHAR (50),
safety_plan_clin VARCHAR (50),
safety_plan_changed_clin VARCHAR (50),
cgi_s_clin VARCHAR (50),
cgi_i_clin VARCHAR (50),
wai_t_1_clin VARCHAR (50),
wai_t_2_clin VARCHAR (50),
wai_t_3_clin VARCHAR (50),
wai_t_4_clin VARCHAR (50),
wai_t_5_clin VARCHAR (50),
wai_t_6_clin VARCHAR (50),
wai_t_7_clin VARCHAR (50),
wai_t_8_clin VARCHAR (50),
wai_t_9_clin VARCHAR (50),
wai_t_10_clin VARCHAR (50),
wai_t_11_clin VARCHAR (50),
wai_t_12_clin VARCHAR (50));




CREATE TABLE redcap_data.maris_y_scars_clin(
    primary_key VARCHAR (20) PRIMARY KEY,
    marisyscars_clin_timestamp VARCHAR (50),
maris_y_scars_1_clin VARCHAR (50),
maris_y_scars_2_clin VARCHAR (50),
maris_y_scars_3_clin VARCHAR (50),
maris_y_scars_4_clin VARCHAR (50),
maris_y_scars_5_clin VARCHAR (50),
maris_y_scars_6_clin VARCHAR (50),
maris_y_scars_7_clin VARCHAR (50),
maris_y_scars_8_clin VARCHAR (50));




CREATE TABLE redcap_data.ending_parent_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    ending_parent_f_timestamp VARCHAR (50),
therapy_child_2_f VARCHAR (50),
ending_childparent_f VARCHAR (50));




CREATE TABLE redcap_data.moas_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    moas_f_timestamp VARCHAR (50),
moas_0_f VARCHAR (50),
moas_1_f VARCHAR (50),
moas_2_f VARCHAR (50),
moas_3_f VARCHAR (50),
moas_4_f VARCHAR (50),
moas_5_f VARCHAR (50),
moas_6_f VARCHAR (50),
moas_7_f VARCHAR (50),
moas_8_f VARCHAR (50),
moas_9_f VARCHAR (50),
moas_10_f VARCHAR (50),
moas_11_f VARCHAR (50),
moas_12_f VARCHAR (50),
moas_13_f VARCHAR (50),
moas_14_f VARCHAR (50),
moas_15_f VARCHAR (50),
moas_16_f VARCHAR (50),
moas_17_f VARCHAR (50),
moas_18_f VARCHAR (50),
moas_19_f VARCHAR (50),
moas_20_f VARCHAR (50));




CREATE TABLE redcap_data.cts_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    cts_f_timestamp VARCHAR (50),
cts_p_1_f VARCHAR (50),
cts_p_2_f VARCHAR (50),
cts_p_3_f VARCHAR (50),
cts_p_4_f VARCHAR (50),
cts_p_4_1_f VARCHAR (50));




CREATE TABLE redcap_data.cts_c(
    primary_key VARCHAR (20) PRIMARY KEY,
    cts_c_timestamp VARCHAR (50),
cts_c_1 VARCHAR (50),
cts_c_2 VARCHAR (50),
cts_c_3 VARCHAR (50),
cts_c_4 VARCHAR (50),
cts_c_4_1 VARCHAR (50));




CREATE TABLE redcap_data.dshi_pre(
    primary_key VARCHAR (20) PRIMARY KEY,
    dshi_pre_timestamp VARCHAR (50),
dshi_pre_1 VARCHAR (50),
dshi_pre_2 VARCHAR (50),
dshi_pre_3 VARCHAR (50),
dshi_pre_4 VARCHAR (50),
dshi_pre_5 VARCHAR (50),
dshi_pre_6 VARCHAR (50));




CREATE TABLE redcap_data.dshi_post(
    primary_key VARCHAR (20) PRIMARY KEY,
    dshi_post_timestamp VARCHAR (50),
dshi_post_1 VARCHAR (50),
dshi_post_2 VARCHAR (50),
dshi_post_3 VARCHAR (50),
dshi_post_4 VARCHAR (50),
dshi_post_5 VARCHAR (50),
dshi_post_6 VARCHAR (50));




CREATE TABLE redcap_data.ending(
    primary_key VARCHAR (20) PRIMARY KEY,
    ending_timestamp VARCHAR (50),
therapy_child VARCHAR (50),
ending_child VARCHAR (50));




CREATE TABLE redcap_data.opening_parents_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    opening_parents_m_timestamp VARCHAR (50),
who_fills_out_m VARCHAR (50),
who_fills_out_2_m VARCHAR (50));




CREATE TABLE redcap_data.estimation_and_satisfaction(
    primary_key VARCHAR (20) PRIMARY KEY,
    estimation_and_satisfaction_timestamp VARCHAR (50),
satis_1 VARCHAR (50),
satis_2 VARCHAR (50),
satis_3 VARCHAR (50),
satis_4 VARCHAR (50));




CREATE TABLE redcap_data.intro(
    primary_key VARCHAR (20) PRIMARY KEY,
    record_id VARCHAR (50),
redcap_event_name VARCHAR (50),
redcap_survey_identifier VARCHAR (50));




CREATE TABLE redcap_data.dass_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    dass_m_timestamp VARCHAR (50),
dass_1_m VARCHAR (50),
dass_2_m VARCHAR (50),
dass_3_m VARCHAR (50),
dass_4_m VARCHAR (50),
dass_5_m VARCHAR (50),
dass_6_m VARCHAR (50),
dass_7_m VARCHAR (50),
dass_8_m VARCHAR (50),
dass_9_m VARCHAR (50),
dass_10_m VARCHAR (50),
dass_11_m VARCHAR (50),
dass_12_m VARCHAR (50),
dass_13_m VARCHAR (50),
dass_14_m VARCHAR (50),
dass_15_m VARCHAR (50),
dass_16_m VARCHAR (50),
dass_17_m VARCHAR (50),
dass_18_m VARCHAR (50),
dass_19_m VARCHAR (50),
dass_20_m VARCHAR (50),
dass_21_m VARCHAR (50));




CREATE TABLE redcap_data.opening_clinicians(
    primary_key VARCHAR (20) PRIMARY KEY,
    opening_clinicians_timestamp VARCHAR (50),
who_clin VARCHAR (50),
who_other_clin VARCHAR (50),
name_clin VARCHAR (50));




CREATE TABLE redcap_data.inq(
    primary_key VARCHAR (20) PRIMARY KEY,
    inq_timestamp VARCHAR (50),
inq_1 VARCHAR (50),
inq_2 VARCHAR (50),
inq_3 VARCHAR (50),
inq_4 VARCHAR (50),
inq_5 VARCHAR (50),
inq_6 VARCHAR (50),
inq_7 VARCHAR (50),
inq_8 VARCHAR (50),
inq_9 VARCHAR (50),
inq_10 VARCHAR (50),
inq_11 VARCHAR (50),
inq_12 VARCHAR (50),
inq_13 VARCHAR (50),
inq_14 VARCHAR (50),
inq_15 VARCHAR (50));




CREATE TABLE redcap_data.swan_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    swan_f_timestamp VARCHAR (50),
swan_1_f VARCHAR (50),
swan_2_f VARCHAR (50),
swan_3_f VARCHAR (50),
swan_4_f VARCHAR (50),
swan_5_f VARCHAR (50),
swan_6_f VARCHAR (50),
swan_7_f VARCHAR (50),
swan_8_f VARCHAR (50),
swan_9_f VARCHAR (50),
swan_10_f VARCHAR (50),
swan_11_f VARCHAR (50),
swan_12_f VARCHAR (50),
swan_13_f VARCHAR (50),
swan_14_f VARCHAR (50),
swan_15_f VARCHAR (50),
swan_16_f VARCHAR (50),
swan_17_f VARCHAR (50),
swan_18_f VARCHAR (50));




CREATE TABLE redcap_data.demographics_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    demographic_parents_f_timestamp VARCHAR (50),
parents_who_f VARCHAR (50),
parent_who_other_f VARCHAR (50),
parents_age_f VARCHAR (50),
parents_born_f VARCHAR (50),
parents_born_2_f VARCHAR (50),
born_child_f VARCHAR (50),
born_child_2_f VARCHAR (50),
parent_religion_f VARCHAR (50),
parent_religion_other_f VARCHAR (50),
parents_economy_f VARCHAR (50),
parents_education_f VARCHAR (50),
parents_education_other_f VARCHAR (50),
parents_work_f VARCHAR (50),
paresnts_work_2_f VARCHAR (50),
together_live_f VARCHAR (50),
with_who_f___1 VARCHAR (50),
with_who_f___2 VARCHAR (50),
with_who_f___3 VARCHAR (50),
with_who_f___4 VARCHAR (50),
with_who_f___5 VARCHAR (50),
with_who_f___6 VARCHAR (50),
with_who_f___7 VARCHAR (50),
with_who_other_f VARCHAR (50));

CREATE TABLE redcap_data.demographics_m(
    primary_key VARCHAR (20) PRIMARY KEY,
    demographic_parents_m_timestamp VARCHAR (50),
parents_who_m VARCHAR (50),
parent_who_other_m VARCHAR (50),
parents_age_m VARCHAR (50),
parents_born_m VARCHAR (50),
parents_born_2_m VARCHAR (50),
born_child_m VARCHAR (50),
born_child_2_m VARCHAR (50),
parent_religion_m VARCHAR (50),
parent_religion_other_m VARCHAR (50),
parents_economy_m VARCHAR (50),
parents_education_m VARCHAR (50),
parents_education_other_m VARCHAR (50),
parents_work_m VARCHAR (50),
paresnts_work_2_m VARCHAR (50),
together_live_m VARCHAR (50),
with_who_m___1 VARCHAR (50),
with_who_m___2 VARCHAR (50),
with_who_m___3 VARCHAR (50),
with_who_m___4 VARCHAR (50),
with_who_m___5 VARCHAR (50),
with_who_m___6 VARCHAR (50),
with_who_m___7 VARCHAR (50),
with_who_other_m VARCHAR (50));




CREATE TABLE redcap_data.mini_kid_sum_stu(
    primary_key VARCHAR (20) PRIMARY KEY,
    mini_kid_sum_stu_timestamp VARCHAR (50),
mini_class_stu VARCHAR (50),
mini_date_stu VARCHAR (50),
mini_interviewer_stu VARCHAR (50),
mini_date_interview_stu VARCHAR (50),
mini_medication_stu___1 VARCHAR (50),
mini_medication_stu___2 VARCHAR (50),
mini_medication_stu___3 VARCHAR (50),
mini_medication_stu___4 VARCHAR (50),
mini_medication_stu___5 VARCHAR (50),
mini_medicine_other_stu VARCHAR (50),
mini_start_time_stu VARCHAR (50),
mini_end_time_stu VARCHAR (50),
mini_total_time_stu VARCHAR (50),
depres_stu___1 VARCHAR (50),
depres_stu___2 VARCHAR (50),
depres_stu___3 VARCHAR (50),
suicide_stu___1 VARCHAR (50),
suicide_stu___2 VARCHAR (50),
suicide_risk_stu VARCHAR (50),
dysthemia_stu___1 VARCHAR (50),
manic_stu___1 VARCHAR (50),
manic_stu___2 VARCHAR (50),
hypomania_stu___1 VARCHAR (50),
hypomania_stu___2 VARCHAR (50),
bipolar_i_stu___1 VARCHAR (50),
bipolar_i_stu___2 VARCHAR (50),
bipolar_ii_stu___1 VARCHAR (50),
bipolar_ii_stu___2 VARCHAR (50),
bipolar_unclassified_stu___1 VARCHAR (50),
bipolar_unclassified_stu___2 VARCHAR (50),
panic_stu___1 VARCHAR (50),
panic_stu___2 VARCHAR (50),
agoraphobia_stu___1 VARCHAR (50),
separation_anxiety_stu___1 VARCHAR (50),
social_anxiety_stu___1 VARCHAR (50),
social_anxiety_stu___2 VARCHAR (50),
social_anxiety_stu___3 VARCHAR (50),
phobia_stu___1 VARCHAR (50),
ocd_stu___1 VARCHAR (50),
ptsd_stu___1 VARCHAR (50),
alcohol_depend_stu___1 VARCHAR (50),
alcohol_use_stu___1 VARCHAR (50),
drug_depend_stu___1 VARCHAR (50),
drug_use_stu___1 VARCHAR (50),
tourette_stu___1 VARCHAR (50),
motor_tics_stu___1 VARCHAR (50),
vocal_tics_stu___1 VARCHAR (50),
transient_tics_stu___1 VARCHAR (50),
adhd_mix_stu___1 VARCHAR (50),
adhd_attention_stu___1 VARCHAR (50),
adhd_hyper_stu___1 VARCHAR (50),
conduct_stu___1 VARCHAR (50),
odd_stu___1 VARCHAR (50),
psychotic_stu___1 VARCHAR (50),
psychotic_stu___2 VARCHAR (50),
affect_psychotic_stu___1 VARCHAR (50),
affect_psychotic_stu___2 VARCHAR (50),
anorexia_stu___1 VARCHAR (50),
bulimia_stu___1 VARCHAR (50),
anorexia_bulmus_stu___1 VARCHAR (50),
gad_stu___1 VARCHAR (50),
adjustment_stu___1 VARCHAR (50),
organic_stu VARCHAR (50),
development_stu___1 VARCHAR (50),
main_dianose_stu VARCHAR (50));




CREATE TABLE redcap_data.chameleon(
    primary_key VARCHAR (20) PRIMARY KEY,
    chameleon_timestamp VARCHAR (50),
chameleon_follow_stu VARCHAR (50),
treatment_end_stu VARCHAR (50),
treatment_end_2_stu VARCHAR (50),
visit_date_stu VARCHAR (50),
chameleon_ideation_stu VARCHAR (50),
chameleon_behavior_stu VARCHAR (50),
chameleon_attempt_stu VARCHAR (50),
chameleon_nssi_stu VARCHAR (50),
chameleon_suicide_er_stu VARCHAR (50),
chameleon_suicide_er_date_stu VARCHAR (50),
chameleon_suicide_er_date_2_stu VARCHAR (50),
chameleon_suicide_er_date_3_stu VARCHAR (50),
chameleon_psychiatric_stu VARCHAR (50),
chameleon_psychiatric_date_stu VARCHAR (50),
chameleon_psychiatric_date_2_stu VARCHAR (50),
chameleon_psychiatric_date_3_stu VARCHAR (50),
emergency_stu VARCHAR (50),
chameleon_psychotherapy_stu VARCHAR (50),
chameleon_psychotherapy_2_stu___1 VARCHAR (50),
chameleon_psychotherapy_2_stu___2 VARCHAR (50),
chameleon_psychotherapy_2_stu___3 VARCHAR (50),
chameleon_psychotherapy_2_stu___4 VARCHAR (50),
chameleon_psychotherapy_2_stu___5 VARCHAR (50),
chameleon_psychotherapy_2_stu___6 VARCHAR (50),
chameleon_psychotherapy_2_stu___7 VARCHAR (50),
chameleon_psychotherapy_other_stu VARCHAR (50),
chameleon_medicine_stu VARCHAR (50),
chameleon_medicine_2_stu___1 VARCHAR (50),
chameleon_medicine_2_stu___2 VARCHAR (50),
chameleon_medicine_2_stu___3 VARCHAR (50),
chameleon_medicine_2_stu___4 VARCHAR (50),
chameleon_medicine_2_stu___5 VARCHAR (50),
chameleon_medicine_other_stu VARCHAR (50),
chameleon_notes_stu VARCHAR (50));


CREATE TABLE redcap_data.demographics_f(
    primary_key VARCHAR (20) PRIMARY KEY,
    demographic_parents_f_timestamp VARCHAR (50),
parents_who_f VARCHAR (50),
parent_who_other_f VARCHAR (50),
parents_age_f VARCHAR (50),
parents_born_f VARCHAR (50),
parents_born_2_f VARCHAR (50),
born_child_f VARCHAR (50),
born_child_2_f VARCHAR (50),
parent_religion_f VARCHAR (50),
parent_religion_other_f VARCHAR (50),
parents_economy_f VARCHAR (50),
parents_education_f VARCHAR (50),
parents_education_other_f VARCHAR (50),
parents_work_f VARCHAR (50),
paresnts_work_2_f VARCHAR (50),
together_live_f VARCHAR (50),
with_who_f___1 VARCHAR (50),
with_who_f___2 VARCHAR (50),
with_who_f___3 VARCHAR (50),
with_who_f___4 VARCHAR (50),
with_who_f___5 VARCHAR (50),
with_who_f___6 VARCHAR (50),
with_who_f___7 VARCHAR (50),
with_who_other_f VARCHAR (50));
