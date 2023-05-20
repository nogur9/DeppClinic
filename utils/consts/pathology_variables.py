"""
intake & time 2

suicidal ideation, suicidal behavior, suicidal attempt, NSSI

"""

# intake

suicidal_behavior_intake = [
    'c_ssrs_t_11_life_clin',
    'c_ssrs_t_12_life_clin',
    'c_ssrs_t_13_life_clin',
    'c_ssrs_t_14_life_clin',
    'c_ssrs_t_15_life_clin',

    'c_ssrs_6_life', 'mfq_34', 'mfq_36', 'c_ssrs_6_2weeks',
    'c_ssrs_6_3month'

]


suicide_attempt_intake = [
    'mfq_36', 'mfq_34', 'c_ssrs_t_11_life_clin',
    'c_ssrs_t_12_life_clin',
    'c_ssrs_t_13_life_clin',
]

nssi_intake = [
    'c_ssrs_t_16_life_clin', 'mfq_35', 'mfq_37',
]


suicidal_ideation_2weeks_intake = [

    'c_ssrs_t_2weeks_1_clin',
    'c_ssrs_t_2weeks_2_clin',
    'c_ssrs_t_2weeks_3_clin',
    'c_ssrs_t_2weeks_4_clin',
    'c_ssrs_t_2weeks_5_clin',

    'c_ssrs_1_life',
    'c_ssrs_2_life',
    'c_ssrs_3_life',
    'c_ssrs_4_life',
    'c_ssrs_5_life',

    'c_ssrs_1_2weeks',
    'c_ssrs_2_2weeks',
    'c_ssrs_3_2weeks',
    'c_ssrs_4_2weeks',
    'c_ssrs_5_2weeks',

]


suicidal_ideation_life_intake = [

    'c_ssrs_t_life_1_clin',
    'c_ssrs_t_life_2_clin',
    'c_ssrs_t_life_3_clin',
    'c_ssrs_t_life_4_clin',
    'c_ssrs_t_life_5_clin',

    'c_ssrs_t_2weeks_1_clin',
    'c_ssrs_t_2weeks_2_clin',
    'c_ssrs_t_2weeks_3_clin',
    'c_ssrs_t_2weeks_4_clin',
    'c_ssrs_t_2weeks_5_clin',

    'c_ssrs_1_life',
    'c_ssrs_2_life',
    'c_ssrs_3_life',
    'c_ssrs_4_life',
    'c_ssrs_5_life',

    'c_ssrs_1_2weeks',
    'c_ssrs_2_2weeks',
    'c_ssrs_3_2weeks',
    'c_ssrs_4_2weeks',
    'c_ssrs_5_2weeks',
]


# time 2

suicidal_behavior_time2 = [
    'suicidal_behavior_last_11_clin',
    'suicidal_behavior_last_12_clin',
    'suicidal_behavior_last_13_clin',
    'suicidal_behavior_last_14_clin',
    'suicidal_behavior_last_15_clin',

    'c_ssrs_6', 'mfq_36',
    'c_ssrs_last_visit_6',
    'chameleon_behavior_stu',
    'chameleon_attempt_stu',
    'chameleon_suicide_er_stu',
    'chameleon_ideation_stu'
]


nssi_time2 = [
    'suicidal_behavior_last_16_clin', 'mfq_37',
]

suicidal_ideation_time2 = [

    'c_ssrs_t_last_1_clin',
    'c_ssrs_t_last_2_clin',
    'c_ssrs_t_last_3_clin',
    'c_ssrs_t_last_4_clin',
    'c_ssrs_t_last_5_clin',

    'c_ssrs_t_2weeks_1_clin',
    'c_ssrs_t_2weeks_2_clin',
    'c_ssrs_t_2weeks_3_clin',
    'c_ssrs_t_2weeks_4_clin',
    'c_ssrs_t_2weeks_5_clin',

    'c_ssrs_1',
    'c_ssrs_2',
    'c_ssrs_3',
    'c_ssrs_4',
    'c_ssrs_5',

    'chameleon_ideation_stu'
]


# grouping

pathology_variables_times = {
    'intake': {'suicidal_behavior_intake': suicidal_behavior_intake,
               'suicide_attempt_intake': suicide_attempt_intake,
               'nssi_intake': nssi_intake,
               'suicidal_ideation_2weeks_intake': suicidal_ideation_2weeks_intake,
               'suicidal_ideation_life_intake': suicidal_ideation_life_intake},

    'time2': {'suicidal_behavior_time2': suicidal_behavior_time2,
              'nssi_time2': nssi_time2,
              'suicidal_ideation_time2': suicidal_ideation_time2,
              }

}

all_pathology_variables = ['suicidal_behavior_intake', 'suicide_attempt_intake', 'nssi_intake',
                'suicidal_ideation_2weeks_intake', 'suicidal_ideation_life_intake', 'suicidal_behavior_time2',
                'nssi_time2', 'suicidal_ideation_time2', 'suicidal_behavior_time2']
