
import pandas as pd
import os

from source.utils.consts.standard_names import INTAKE


def save_results(df, columns, axis='patient', directory_path=None, suffix=''):
    if axis == 'patient':
        save_patient_axis(df, columns, directory_path, suffix)
    elif axis == 'time':
        save_time_axis(df, columns, directory_path, suffix)


def save_time_axis(df, columns, directory_path, suffix):
    df_to_save = df[columns.columns_for_extraction]
    save_to_csv(df_to_save, directory_path, f"data_measurement_axis{suffix}.csv")


def save_patient_axis(df, columns, directory_path, suffix):
    intake_df = df[df.measurement == INTAKE][columns.columns_for_extraction].copy()

    followup_df = get_followup_data(df, columns)
    df_wide = convert_long_to_wide(intake_df, followup_df, columns)

    save_to_csv(df_wide, directory_path, f"data_patient_axis{suffix}.csv", columns)


def get_followup_data(df, columns):
    columns_to_include = [i for i in columns.columns_for_extraction if i not in columns.INFO_COLUMNS]
    followup_df = df[df.measurement != INTAKE][columns_to_include]
    return followup_df


def convert_long_to_wide(df_intake, followup_df, columns):

    new_columns = []
    irrelevant_columns = ['measurement']

    info_columns = columns.INFO_COLUMNS + [columns.id_column, 'measurement']
    columns_to_rename = [col for col in df_intake.columns if col not in info_columns]
    rename_map = {col: f"{col}_{INTAKE}" for col in columns_to_rename}

    irrelevant_columns.extend(rename_map)
    new_columns.extend(list(rename_map.values()))
    merged_df = df_intake.rename(rename_map, axis=1)

    for measurement in followup_df["measurement"].unique():
        current_measurement_dataset = followup_df[followup_df["measurement"] == measurement].copy()
        current_measurement_dataset = current_measurement_dataset.drop(['measurement'], axis=1)

        rename_map = {col: f"{col}_{measurement}" for col in current_measurement_dataset.columns if col != columns.id_column}
        current_measurement_dataset.rename(columns=rename_map, inplace=True)  # Modify subset in-place
        merged_df = pd.merge(merged_df, current_measurement_dataset, on=columns.id_column, how="outer")
        new_columns.extend(list(rename_map.values()))
    else:

        columns.add_columns(new_columns)
        columns.drop(irrelevant_columns)

    return merged_df


def save_to_csv(df, directory_path, filename, columns):
    if directory_path is None:
        df[columns.columns_for_extraction].to_csv(filename, index=False)
    else:
        df[columns.columns_for_extraction].to_csv(os.path.join(directory_path, filename), index=False)

