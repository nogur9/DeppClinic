from source.utils.consts.pathology_variables import pathology_variables_times
import pandas as pd



def long_to_wide(df_intake, followup_df, useless_cols, event_col='measurement', id_col="id"):

    wide_df = df_intake
    for event in followup_df[event_col].unique():
        subset = followup_df.loc[followup_df[event_col] == event, followup_df.columns.difference(useless_cols)]
        subset_columns_rename = {col: f"{col}_{event}" for col in subset.columns if col != id_col}
        subset.rename(columns=subset_columns_rename, inplace=True)  # Modify subset in-place
        wide_df = pd.merge(wide_df, subset, on=id_col, how="outer")

    return wide_df




def save_df(df, columns, axis='patient', directory_path=None, suffix='', intake_name='Time 1'):
    if axis == 'patient':

        df_intake = df[df.measurement == intake_name][columns.ordered_columns_with_id]
        df_intake = df_intake.drop(pathology_variables_times['time2'], errors='ignore', axis=1)
        intake_scores = [i for i in df_intake.columns if (i not in columns.info_columns) and (i != columns.id_column) and (i != 'measurement')]
        intake_scores_rename = {i: f"{i}_intake" for i in intake_scores}
        df_intake = df_intake.rename(intake_scores_rename, axis=1)
        followup_df = df[df.measurement != intake_name][columns.ordered_columns_with_id]
        useless_cols = list(pathology_variables_times['intake'].keys()) + columns.info_columns

        df = long_to_wide(df_intake, followup_df, useless_cols)

        df = df.drop(['measurement'], axis=1)

        if directory_path is None:
            df.to_csv(f"data_patient_axis{suffix}.csv", index=False)
        else:
            df.to_csv(rf"{directory_path}\data_patient_axis{suffix}.csv", index=False)

    elif axis == 'time':
        df = df[columns.ordered_columns_with_id]
        if directory_path is None:
            df.to_csv(f"data_measurement_axis{suffix}.csv", index=False)
        else:
            df.to_csv(rf"{directory_path}\data_measurement_axis{suffix}.csv", index=False)
