from source.utils.consts.pathology_variables import pathology_variables_times
from source.utils.consts.questions_columns import full_questionnaire_list, sci_af_ca, mfq, sdq, c_ssrs_intake, siq, cgi
from source.utils.consts.assistment_consts import imputation_questionnaires
from source.utils.util_functions import impute_from_questionnaire
from to_delete.data_manipulation.data_imputation import impute_from_column
import pandas as pd


def do_questionnaires_imputations(df):
    for questionnaire_imputation in imputation_questionnaires:
        try:
            df = impute_from_questionnaire(df, questionnaire_imputation['origin'], questionnaire_imputation['replacement'])
        except KeyError:
            pass

    return df


def create_single_event_name(df, columns, event_names):

    df_event_name = df[df.redcap_event_name == event_names[0]][list(columns.get_export_columns())]

    for event_name in event_names[1:]:
        df_new_measurement = df[df.redcap_event_name == event_name][list(columns.get_export_columns())]

        df_event_name = impute_events(df_event_name, df_new_measurement, columns, suffix=event_name)

    return df_event_name


def split_to_multiple_measurement_times(df, columns, times):
    all_events_datasets_collection = []
    intake_data = None
    for time in times.keys():
        events = times[time]

        event_dataset = df[df.redcap_event_name == events[0]][list(columns.get_export_columns())]

        if len(events) > 1:

            for event_name in events[1:]:
                df_new_measurement = df[df.redcap_event_name == event_name][list(columns.get_export_columns())]
                event_dataset = impute_events(event_dataset, df_new_measurement, columns, suffix=event_name)

        event_dataset['measurement'] = time

        if (time == 'intake') or (time == 'Time 1'):
            intake_data = event_dataset
        else:
            all_events_datasets_collection.append(event_dataset)
    try:
        return intake_data, pd.concat(all_events_datasets_collection)
    except ValueError:
        return intake_data, pd.DataFrame()


def split_two_measurement_times(df, columns):
    time1_event = 'intake_arm_1'
    time2_events = ['control_5weeks_arm_1', 'pre_treatment_arm_1', 'followup_3month_arm_1']

    df_time1 = df[df.redcap_event_name == time1_event][columns.get_export_columns()]
    df_time2 = df[df.redcap_event_name == time2_events[0]][columns.get_export_columns()]

    for event_name in time2_events[1:]:
        df_new_measurement = df[df.redcap_event_name == event_name][columns.get_export_columns()]

        df_time2 = impute_events(df_time2, df_new_measurement, columns, suffix=event_name)

    df_time1['measurement'] = 'time1'
    df_time2['measurement'] = 'time2'

    return df_time1, df_time2


def impute_events(df1, df2, columns, suffix):
    imputed_data = pd.merge(df1, df2, on=['id'], how='outer', suffixes=('', f'_{suffix}'))

    for column_name in columns.get_export_columns(include_id=False):
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

