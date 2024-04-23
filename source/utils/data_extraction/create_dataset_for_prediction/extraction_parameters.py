
class InputParameters:
    # Set immutable default parameters as class attributes
    DEFAULT_FILE_NAME = 'patient_data'
    DEFAULT_DIRECTORY_PATH = r'C:\Users\nogur\Documents\DeppClinic\Data\processed_data\only_final_scores'
    DEFAULT_AXIS = 'patient'
    DEFAULT_DF_PATH = r"C:\Users\nogur\Documents\DeppClinic\Data\postgres_db\merged_data\merged_2021_and_2022.csv"

    def __init__(self, measurement_times, questionnaires=all_questionnaires,
                 assign_groups=True, impute_from_parallel_questionnaires=True,
                 compute_target_variable=True, calculate_questionnaires_scores=True,
                 file_name=DEFAULT_FILE_NAME, directory_path=DEFAULT_DIRECTORY_PATH,
                 axis=DEFAULT_AXIS, df_path=DEFAULT_DF_PATH):
        self.measurement_times = measurement_times
        self.questionnaires = questionnaires
        self.assign_groups = assign_groups
        self.impute_from_parallel_questionnaires = impute_from_parallel_questionnaires
        self.compute_target_variable = compute_target_variable
        self.calculate_questionnaires_scores = calculate_questionnaires_scores
        self.file_name = file_name
        self.directory_path = directory_path
        self.axis = axis
        self.df_path = df_path

