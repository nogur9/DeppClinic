from source.utils.consts.standard_names import INTAKE

measurement_times = {
    INTAKE: ['intake_arm_1', 'er_arm_1'],
    'FollowUp': ['5th_session_arm_1', 'control_5weeks_arm_1', 'followup_3month_arm_1',
               'control_3month_arm_1', 'control_6month_arm_1']

}

modcon_measurement_times = {
    INTAKE: ['intake_arm_1', 'pre_treatment_arm_1', 'er_arm_1'],
    'FollowUp': ['5th_session_arm_1', 'control_5weeks_arm_1'],
}

r"""

## Times


treatment_times = {
    'Time 1': ['intake_arm_1', 'pre_treatment_arm_1', 'er_arm_1'],
    'Time 2': ['5th_session_arm_1'],
    'Time 3': ['followup_3month_arm_1', 'control_3month_arm_1', 'control_6month_arm_1']
}
control_times = {
    'Time 1': ['intake_arm_1', 'er_arm_1'],
    'Time 2': ['control_5weeks_arm_1'],
    'Time 3': ['control_3month_arm_1', 'control_6month_arm_1']
}

all_times = {
    'Time 1': ['intake_arm_1', 'pre_treatment_arm_1', 'er_arm_1'],
    'Time 2': ['5th_session_arm_1', 'control_5weeks_arm_1'],
    'Time 3': ['followup_3month_arm_1', 'control_3month_arm_1', 'control_6month_arm_1']
}










all_times = {
    'intake': ['intake_arm_1', 'er_arm_1'],
    'pre_treatment_arm_1': ['pre_treatment_arm_1'],
    'control_5weeks_arm_1': ['control_5weeks_arm_1'],
    '5th_session_arm_1': ['5th_session_arm_1'],
    'followup_3month_arm_1': ['followup_3month_arm_1'],
    'control_3month_arm_1': ['control_3month_arm_1'],
    'control_6month_arm_1': ['control_6month_arm_1'],

    # new times:

    'control_12month_arm_1': ['control_12month_arm_1'],
    'control_9month_arm_1': ['control_9month_arm_1'],
    'er_one_week_arm_1': ['er_one_week_arm_1'],
    'followup_12month_arm_1': ['followup_12month_arm_1'],
    'post_treatment_arm_1': ['post_treatment_arm_1']
}

"""
