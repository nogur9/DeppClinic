# Define the measurement times based on the previous dictionary provided
from source.utils.consts.measurement_times import measurement_times
from source.utils.dataset_creation_process.dataset_creation_input_parameter import InputParametersForDatasetCreationProcess
from source.utils.dataset_creation_process.dataset_creation_process import DatasetCreationProcess


def main(input_params):
    # Set the content root directory
    extraction_process = DatasetCreationProcess(input_params)
    extraction_process.run()


# Create an instance of InputParameters with custom and default values
input_parameters_for_dataset_creation_process = InputParametersForDatasetCreationProcess(
    measurement_times=measurement_times,
    questionnaires_for_scoring=['sdq'],
    indicator_questionnaires=['mfq'],
    assign_groups=True,
    impute_from_parallel_questionnaires=True,
    calculate_questionnaires_scores=True,
    compute_target_variable=True,
    include_app_data=True,
    file_name='patient_data',
    directory_path=r'Data\processed_data\test',
    axis='patient',
    content_root=r"C:\Users\nogur\Documents\DeppClinic",
)

main(input_parameters_for_dataset_creation_process)
