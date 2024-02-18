import pandas as pd
import numpy as np
from source.utils.further_data_processing.create_dataset_for_prediction.handle_groups import GROUPS, fill_group, GROUP_NAMES_MAP, rename_groups, fill_missing_groups
from source.utils.further_data_processing.create_dataset_for_prediction.pipeline_functions import Columns, do_imputations, save_df, split_to_multiple_measurement_times
from source.utils.consts.pathology_variables import pathology_variables_times
from source.utils.target_variable import TargetVariable
import os


def main(times, directory_path=None, suffix=''):
    # Change the current directory to the source root

    df = pd.read_csv(r"C:\Users\nogur\Documents\DeppClinic\Data\postgres_db\merged_data\merged_2021_and_2022.csv",
                     na_values='chameleon_ideation_stu_2022', keep_default_na=True)

    columns = Columns()
    df = do_imputations(df)

    columns.add(['sciafca_timestamp'])
    df_time1, df_time2 = split_to_multiple_measurement_times(df, columns, times)
    columns.add(['measurement'])

    for questionnaire_name, items in pathology_variables_times['time2'].items():
        tv = TargetVariable(questionnaire_name, {'measurement': 'time2'}, items)
        df_time2 = tv.calculate_value(df_time2)
        columns.add([questionnaire_name])

    df = pd.concat([df_time1, df_time2])
    df = df[list(columns.unique_columns_with_id)]

    save_df(df, columns, axis='time', profile=False, directory_path=directory_path, suffix=suffix)


all_times = {
    'Time 1': ['intake_arm_1', 'pre_treatment_arm_1', 'er_arm_1'],
    'Time 2': ['5th_session_arm_1', 'control_5weeks_arm_1'],
}
#
main(all_times, r"C:\Users\nogur\Documents\DeppClinic\source\projects\for_guy\data")





