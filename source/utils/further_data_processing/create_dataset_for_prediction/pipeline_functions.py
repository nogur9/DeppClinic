from source.utils.consts.pathology_variables import pathology_variables_times
from source.utils.consts.questions_columns import all_questionarries
from source.utils.consts.assistment_consts import imputation_questionnaires
from source.utils.util_functions import impute_from_questionnaire
from source.utils.data_manipulation.data_imputation import impute_from_column
import pandas as pd
#import pandas_profiling as pp


class Columns:

    def __init__(self, columns=[], id_column='id'):

        self.info_columns = ['gender', 'redcap_event_name', 'age_child_pre']
        self.extra_columns =  all_questionarries + ['chameleon_attempt_stu', 'chameleon_psychiatric_stu', 'chameleon_suicide_er_stu']
        default_columns = self.info_columns

        self.id_column = id_column

        if len(columns):
            self.columns = columns
        else:
            self.columns = default_columns

        self.ordered_columns = []
        self.unique_columns = set()
        self.ordered_columns_with_id = []
        self.unique_columns_with_id = set()
        self.define()

    def define(self):
        self.ordered_columns.extend(self.columns)
        self.unique_columns.update(set(self.columns + self.extra_columns))

        self.ordered_columns_with_id.extend([self.id_column] + self.columns)
        self.unique_columns_with_id.update(set([self.id_column] + self.columns + self.extra_columns))

    def add(self, items):

        self.unique_columns.update(set(items))
        self.unique_columns_with_id.update(set(items))

        self.ordered_columns.extend(items)
        self.ordered_columns_with_id.extend(items)
        self.columns.extend(items)


def do_imputations(df):
    for questionnaire_imputation in imputation_questionnaires:
        try:
            df = impute_from_questionnaire(df, questionnaire_imputation['origin'], questionnaire_imputation['replacement'])
        except KeyError:
            pass

    return df


def create_single_event_name(df, columns, event_names):

    df_event_name = df[df.redcap_event_name == event_names[0]][list(columns.unique_columns_with_id)]

    for event_name in event_names[1:]:
        df_new_measurement = df[df.redcap_event_name == event_name][list(columns.unique_columns_with_id)]

        df_event_name = impute_events(df_event_name, df_new_measurement, columns, suffix=event_name)

    return df_event_name


def split_to_multiple_measurement_times(df, columns, times):
    all_events_datasets_collection = []
    intake_data = None
    for time in times.keys():
        events = times[time]

        event_dataset = df[df.redcap_event_name == events[0]][list(columns.unique_columns_with_id)]

        if len(events) > 1:

            for event_name in events[1:]:
                df_new_measurement = df[df.redcap_event_name == event_name][list(columns.unique_columns_with_id)]
                event_dataset = impute_events(event_dataset, df_new_measurement, columns, suffix=event_name)

        event_dataset['measurement'] = time

        if (time == 'intake') or (time == 'Time 1'):
            intake_data = event_dataset
        else:
            all_events_datasets_collection.append(event_dataset)

    return intake_data, pd.concat(all_events_datasets_collection)


def split_two_measurement_times(df, columns):
    time1_event = 'intake_arm_1'
    time2_events = ['control_5weeks_arm_1', 'pre_treatment_arm_1', 'followup_3month_arm_1']

    df_time1 = df[df.redcap_event_name == time1_event][columns.unique_columns_with_id]
    df_time2 = df[df.redcap_event_name == time2_events[0]][columns.unique_columns_with_id]

    for event_name in time2_events[1:]:
        df_new_measurement = df[df.redcap_event_name == event_name][columns.unique_columns_with_id]

        df_time2 = impute_events(df_time2, df_new_measurement, columns, suffix=event_name)

    df_time1['measurement'] = 'time1'
    df_time2['measurement'] = 'time2'

    return df_time1, df_time2


def impute_events(df1, df2, columns, suffix):
    imputed_data = pd.merge(df1, df2, on=['id'], how='outer', suffixes=('', f'_{suffix}'))

    for column_name in columns.unique_columns:
        imputed_data = impute_from_column(imputed_data, impute_to=column_name,
                                          impute_from=f'{column_name}_{suffix}')

    duplicated_columns = [i for i in imputed_data.columns if i.endswith(f'_{suffix}')]
    imputed_data = imputed_data.drop(duplicated_columns, axis=1)

    return imputed_data


def compute_questions_scores(df, questionnaires_map, variables_list, only_relevant=False):
    for questionnaire in questionnaires_map.keys():
        try:
            df, scores_columns_names = questionnaires_map[questionnaire]['scoring_function'](df)
            variables_list.add(scores_columns_names)
        except KeyError:
            pass

    return df, variables_list


def save_df(df, columns, axis='patient', profile=False, directory_path=None, suffix=''):
    if axis == 'patient':

        df_intake = df[df.measurement == 'Time 1'][columns.ordered_columns_with_id]
        df_intake = df_intake.drop(pathology_variables_times['time2'], axis=1)
        df_target_time2 = df[df.measurement == 'Time 2'][columns.ordered_columns_with_id]
        df_target_time2 = df_target_time2.drop(list(pathology_variables_times['intake'].keys()) + columns.info_columns, axis=1)
        df_target_time3 = df[df.measurement == 'Time 3'][columns.ordered_columns_with_id]
        df_target_time3 = df_target_time3.drop(list(pathology_variables_times['intake'].keys()) + columns.info_columns, axis=1)

        df = pd.merge(df_target_time2, df_target_time3, on='id', how='outer', suffixes=('_time2', '_time3'))

        df = pd.merge(df_intake, df, on='id', how='outer')
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
