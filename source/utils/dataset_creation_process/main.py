# Define the measurement times based on the previous dictionary provided
from source.utils.consts.measurement_times import measurement_times, modcon_measurement_times
from source.utils.dataset_creation_process.dataset_creation_input_parameter import InputParametersForDatasetCreationProcess
from source.utils.dataset_creation_process.dataset_creation_process import DatasetCreationProcess


def main(input_params):
    # Set the content root directory
    extraction_process = DatasetCreationProcess(input_params)
    extraction_process.run()


# Create an instance of InputParameters with custom and default values
input_parameters_for_dataset_creation_process = InputParametersForDatasetCreationProcess(
    measurement_times=modcon_measurement_times,
    impute_from_parallel_questionnaires=True,

    questionnaires=['mfq', 'siq', 'sdq',
                    'piu', "erq-ca", "cts",
                    'dshi-pre', 'dshi-post',
                    'inq', 'mast', "ders",
                    "athens", 'ari-s', 'erc-rc',
                    'sas', 'scared', 'sci_af_ca',
                    "maris_sci_sf", "c_ssrs_intake"
                    ],

    include_individual_questions=True,
    calculate_questionnaires_scores=False,

    compute_target_variable=True,
    pathologies=['MODCON'],


    file_name='Modcon_data_15-8',
    directory_path=r'Data\processed_data\test',
    axis='patient',
    content_root=r"C:\Users\nogur\Documents\DeppClinic",

    include_app_data=True,
    calculate_timestamps=False
)

main(input_parameters_for_dataset_creation_process)
