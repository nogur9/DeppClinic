"""

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


## Which data to include?

questionnaires = all_questionnaires


## Which steps to perform?

assign_groups = True
impute_from_parallel_questionnaires = True
compute_target_variable = True
calculate_questionnaires_scores = True


## Saving parameters

file_name = 'patient_data'
directory_path = r'C:\Users\nogur\Documents\DeppClinic\Data\processed_data\only_final_scores'
axis = 'patient'


"""


# Define the measurement times based on the previous dictionary provided
from source.utils.data_extraction.create_dataset_for_prediction.extraction_process import ExtractionProcess

measurement_times = {
    'Time 1': ['intake_arm_1', 'pre_treatment_arm_1', 'er_arm_1'],
    'Time 2': ['5th_session_arm_1', 'control_5weeks_arm_1'],
    'Time 3': ['followup_3month_arm_1', 'control_3month_arm_1', 'control_6month_arm_1']
}


def main(input_params):
    extraction_process = ExtractionProcess(input_params)
    extraction_process.run()


# Create an instance of InputParameters with custom and default values
input_params = InputParameters(
    measurement_times=measurement_times,
    questionnaires=all_questionnaires,

    assign_groups=True,
    impute_from_parallel_questionnaires=True,
    calculate_questionnaires_scores=True,


    compute_target_variable=True,

    file_name='patient_data',
    directory_path=r'C:\Users\nogur\Documents\DeppClinic\Data\processed_data\only_final_scores',
    axis='patient'
)

main(input_params)


# VariablesToExport