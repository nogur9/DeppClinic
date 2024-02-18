import pandas as pd
import os

# Change the current directory to the source root
os.chdir(r'/')

from source.utils.further_data_processing.create_dataset_for_prediction.pipeline_functions import Columns, create_single_event_name, \
    do_imputations, save_df
from source.utils.consts.pathology_variables import Liat_Graphs_pathology_variables_times
from source.utils.target_variable import TargetVariable


def fill_group(df, group):
    """
    This function takes a DataFrame as input, and fills out the empty 'id' values by matching them to the 'record_id' which isn't empty.

    Parameters:
        df (pandas DataFrame): The DataFrame to be cleaned.

    Returns:
        pandas DataFrame : The cleaned DataFrame.
    """
    df = df.copy()
    group_map = df.dropna(subset=[group]).groupby('id')[group].first()
    group_map = {key: group_map[key] for key in group_map.keys()}

    def try_group_map(x):
        try:
            group_name = group_map[x]
            return group_name
        except KeyError:
            print(x)

    df[group] = df['id'].apply(try_group_map)

    return df


def create_dataset(event_names, path=None):

    df = pd.read_csv(r"C:\Users\nogur\Documents\DeppClinic\creating_the_clinic_dataset\preprocessed_data\merged_2021_and_2022.csv", na_values=' ')
    columns = Columns()
    groups = ['group___1', 'group___2', 'group___3']
    columns.add(groups)
    df = do_imputations(df)
    for group in groups:
        df = fill_group(df, group)
    df = create_single_event_name(df, columns, event_names)
    # calculate pathology variables

    if 'intake_arm_1' in event_names:
        for questionnaire_name, items in Liat_Graphs_pathology_variables_times['intake'].items():
            tv = TargetVariable(questionnaire_name, {'measurement': 'time1'}, items)
            df = tv.calculate_value(df)
            columns.add([questionnaire_name])
    else:
        for questionnaire_name, items in Liat_Graphs_pathology_variables_times['time2'].items():
            tv = TargetVariable(questionnaire_name, {'measurement': 'time2'}, items)
            df = tv.calculate_value(df)
            columns.add([questionnaire_name])

    df = df[list(columns.unique_columns_with_id)]

    save_df(df, columns, axis='time', profile=False, directory_path=path)


if __name__ == "__main__":
    times = {'intake': ['intake_arm_1', 'pre_treatment_arm_1'],
             'time2': ['5th_session_arm_1', 'control_5weeks_arm_1'],
             'time3': ['followup_3month_arm_1', 'control_3month_arm_1', 'control_6month_arm_1']}

    for time in times.keys():
        create_dataset(event_names=times[time], path=rf"C:\Users\nogur\Documents\DeppClinic\source\projects\Liat graphs\data\{time}")

