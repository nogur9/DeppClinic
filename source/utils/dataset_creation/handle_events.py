from source.utils.classes.export_columns_manager import ExportColumnsManager
import numpy as np
import pandas as pd


def group_by_measurment_times(df: pd.DataFrame, measurement_times: dict):
    finished_datasets = []
    for measurement_name, times in measurement_times.items():
        measurement_dataset = prepare_single_dataset(df, times)
        measurement_dataset['measurement'] = measurement_name
        finished_datasets.append(measurement_dataset)
    return pd.concat(finished_datasets)


def prepare_single_dataset(df, times):
    events = iter(times)
    first_event = next(events)
    combined_dataset = df[df.redcap_event_name == first_event]

    for event_name in events:
        current_event_dataset = df[df.redcap_event_name == event_name]
        combined_dataset = impute_missing_values(combined_dataset, current_event_dataset)

    return combined_dataset


def impute_missing_values(primary_df, backup_df):
    primary_df = primary_df.copy()
    backup_df = backup_df.copy()

    merged_df = pd.merge(primary_df, backup_df, on='id', how='outer', suffixes=('', f'_backup'))

    for column in [i for i in primary_df.columns if i != 'id']:
        merged_df[column] = np.where(merged_df[column].isna(), merged_df[f'{column}_backup'], merged_df[column])

    merged_df.drop(columns=[col for col in merged_df.columns if col.endswith(f'_backup')], inplace=True)

    return merged_df

