import pandas as pd

from dataset_creation.handle_groups import GROUPS, fill_group, GROUP_NAMES_MAP, rename_groups, fill_missing_groups
from dataset_creation.pipeline_functions import Columns, do_imputations, compute_questions_scores, save_df, split_to_multiple_measurement_times
from source.utils.consts.pathology_variables import pathology_variables_times
from source.utils.target_variable import TargetVariable
from source.utils.consts.assistment_consts import Questionnaires
import os


def main(times, directory_path=None):
    # Change the current directory to the source root
    os.chdir(r'C:\Users\nogur\Documents\DeppClinic')

    df = pd.read_csv(r"creating_the_clinic_dataset/preprocessed_data/merged_2021_and_2022.csv", na_values=' ')
    columns = Columns()
    df = do_imputations(df)

    # handle groups
    for group in GROUPS:
        df = fill_group(df, group)

    df = rename_groups(df, GROUP_NAMES_MAP)
    df = fill_missing_groups(df, GROUP_NAMES_MAP)
    columns.add(['group'])
    columns.add(['sciafca_timestamp'])
    df_time1, df_time2 = split_to_multiple_measurement_times(df, columns, times)
    columns.add(['measurement'])
    # calculate pathology variables
    for questionnaire_name, items in pathology_variables_times['intake'].items():
        tv = TargetVariable(questionnaire_name, {'measurement': 'time1'}, items)
        df_time1 = tv.calculate_value(df_time1)
        columns.add([questionnaire_name])

    for questionnaire_name, items in pathology_variables_times['time2'].items():
        tv = TargetVariable(questionnaire_name, {'measurement': 'time2'}, items)
        df_time2 = tv.calculate_value(df_time2)
        columns.add([questionnaire_name])

    df = pd.concat([df_time1, df_time2])
    df = df[columns.unique_columns_with_id]

    questionnaires = Questionnaires().questionnaires
    df, columns = compute_questions_scores(df, questionnaires, columns)

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    save_df(df, columns, axis='patient', profile=False, directory_path=directory_path)
    save_df(df, columns, axis='time', profile=False, directory_path=directory_path)


times = {
    'Time 1': ['intake_arm_1', 'pre_treatment_arm_1'],
    'Time 2': ['5th_session_arm_1'],#, 'control_5weeks_arm_1' ],
    'Time 3': ['followup_3month_arm_1', 'control_3month_arm_1', 'control_6month_arm_1']
}

main(times, r"Request_for_app_data_analysis/data/treatment_group")

