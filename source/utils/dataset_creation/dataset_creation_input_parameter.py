from source.utils.questionnaire.questionnaires_map import QuestionnairesMap


class InputParameters:
    # Set immutable default parameters as class attributes
    DEFAULT_FILE_NAME = 'patient_data'
    DEFAULT_DIRECTORY_PATH = r'Data/processed_data/only_final_scores'
    DEFAULT_AXIS = 'patient'
    DEFAULT_DF_PATH = r"Data\postgres_db\merged_data\merged_2021_and_2022.csv"
    DEFAULT_CUSTOM_NA_VALS = ['chameleon_ideation_stu_2022']
    DEFAULT_PATHOLOGIES = ["suicidal_behavior_intake", "suicide_attempt_intake", "NSSI_intake"]

    def __init__(self, measurement_times, content_root, questionnaires_map=QuestionnairesMap(),
                 assign_groups=True, impute_from_parallel_questionnaires=True,
                 compute_target_variable=True, calculate_questionnaires_scores=True,
                 file_name=DEFAULT_FILE_NAME, directory_path=DEFAULT_DIRECTORY_PATH,
                 axis=DEFAULT_AXIS, df_path=DEFAULT_DF_PATH, custom_na_values=DEFAULT_CUSTOM_NA_VALS,
                 add_pathology_missing_ratio=False, pathologies=DEFAULT_PATHOLOGIES, include_individual_questions = True):

        self.measurement_times = measurement_times
        self.questionnaires_map = questionnaires_map
        self.assign_groups = assign_groups
        self.impute_from_parallel_questionnaires = impute_from_parallel_questionnaires
        self.compute_target_variable = compute_target_variable
        self.calculate_questionnaires_scores = calculate_questionnaires_scores
        self.file_name = file_name
        self.directory_path = directory_path
        self.axis = axis
        self.df_path = df_path
        self.custom_na_values = custom_na_values
        self.content_root = content_root
        self.add_pathology_missing_ratio = add_pathology_missing_ratio
        self.pathologies = pathologies
        self.include_individual_questions = include_individual_questions


