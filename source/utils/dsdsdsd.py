
import pandas as pd
import os


def save_results(df, columns, axis='patient', directory_path=None, suffix='', intake_name='Time 1'):
    if axis == 'patient':
        save_patient_axis(df, columns, directory_path, suffix, intake_name)
    elif axis == 'time':
        save_time_axis(df, columns, directory_path, suffix)


def save_patient_axis(df, columns, directory_path, suffix, intake_name):
    df_intake = get_intake_data(df, columns, intake_name)
    df_intake = rename_intake_columns(df_intake, columns)

    followup_df = get_followup_data(df, columns, intake_name)
    df_wide = convert_long_to_wide(df_intake, followup_df)

    save_to_csv(df_wide.drop(['measurement'], axis=1), directory_path, f"data_patient_axis{suffix}.csv")


def save_time_axis(df, columns, directory_path, suffix):
    df_to_save = df[columns.columns_for_extraction]
    save_to_csv(df_to_save, directory_path, f"data_measurement_axis{suffix}.csv")


def get_intake_data(df, columns, intake_name):
    return df[df.measurement == intake_name][columns.columns_for_extraction]


def rename_intake_columns(df_intake, columns):
    info_columns = [columns.INFO_COLUMNS, columns.id_column, 'measurement']
    intake_scores = [col for col in df_intake.columns if col not in info_columns]
    intake_scores_rename = {col: f"{col}_intake" for col in intake_scores}
    return df_intake.rename(intake_scores_rename, axis=1)


def get_followup_data(df, columns, intake_name):
    followup_df = df[df.measurement != intake_name][columns.columns_for_extraction]
    return followup_df.drop(columns.INFO_COLUMNS, errors='ignore', axis=1)


def convert_long_to_wide(df_intake, followup_df, event_col='measurement', id_col="id"):
    wide_df = df_intake
    for event in followup_df[event_col].unique():
        subset = followup_df[followup_df[event_col] == event]
        subset_columns_rename = {col: f"{col}_{event}" for col in subset.columns if col != id_col}
        subset.rename(columns=subset_columns_rename, inplace=True)
        wide_df = pd.merge(wide_df, subset, on=id_col, how="outer")
    return wide_df


def save_to_csv(df, directory_path, filename):
    if directory_path is None:
        df.to_csv(filename, index=False)
    else:
        df.to_csv(os.path.join(directory_path, filename), index=False)
#
#
# def long_to_wide(df_intake, followup_df, event_col='measurement', id_col="id"):
#
#     wide_df = df_intake
#     for event in followup_df[event_col].unique():
#         subset = followup_df.loc[followup_df[event_col] == event, followup_df.columns]
#         subset_columns_rename = {col: f"{col}_{event}" for col in subset.columns if col != id_col}
#         subset.rename(columns=subset_columns_rename, inplace=True)  # Modify subset in-place
#         wide_df = pd.merge(wide_df, subset, on=id_col, how="outer")
#
#     return wide_df
#
#
#
# def save_df(df, columns, axis='patient', directory_path=None, suffix='', intake_name='Time 1'):
#     if axis == 'patient':
#         df_intake = df[df.measurement == intake_name][columns.columns_for_extraction]
#         info_columns = [columns.INFO_COLUMNS, columns.id_column, 'measurement']
#         intake_scores = [i for i in df_intake.columns if i not in info_columns]
#         intake_scores_rename = {i: f"{i}_intake" for i in intake_scores}
#         df_intake = df_intake.rename(intake_scores_rename, axis=1)
#
#         followup_df = df[df.measurement != intake_name][columns.columns_for_extraction]
#         followup_df = followup_df.drop(columns.INFO_COLUMNS, errors='ignore', axis=1)
#
#         df = long_to_wide(df_intake, followup_df)
#
#         df = df.drop(['measurement'], axis=1)
#
#         if directory_path is None:
#             df.to_csv(f"data_patient_axis{suffix}.csv", index=False)
#         else:
#             df.to_csv(rf"{directory_path}\data_patient_axis{suffix}.csv", index=False)
#
#     elif axis == 'time':
#         df = df[columns.columns_for_extraction]
#         if directory_path is None:
#             df.to_csv(f"data_measurement_axis{suffix}.csv", index=False)
#         else:
#             df.to_csv(rf"{directory_path}\data_measurement_axis{suffix}.csv", index=False)
