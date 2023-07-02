from utils.consts.questions_columns import sci_af_ca, c_ssrs, sci_mother, scs_clin, siq, sdq, c_ssrs_intake, mfq, \
    scared, ATHENS, SAS, c_ssrs_clin, demographics_m, swan_m
from utils.consts.pathology_variables import all_pathology_variables
from utils.consts.assistment_consts import imputation_questionnaires
from utils.util_functions import questionnaire_is_empty, impute_from_questionnaire
from utils.data_manipulation.data_imputation import impute_from_column
import pandas as pd
import pandas_profiling as pp


class Columns:
    extra_columns = ['chameleon_behavior_stu', 'chameleon_attempt_stu', 'chameleon_suicide_er_stu',
                     'chameleon_ideation_stu', 'mfq_34', 'mfq_36', 'mfq_35', 'mfq_37', 'chameleon_nssi_stu']

    info_columns = ['gender', 'redcap_event_name', 'age_child_pre']

    default_columns = info_columns + demographics_m + c_ssrs_intake + c_ssrs + c_ssrs_clin + sci_af_ca + scs_clin + \
                      sci_mother + siq + sdq + mfq + scared + ATHENS + SAS + demographics_m + swan_m

    def __init__(self, columns=[], id_column='id'):
        self.id_column = id_column

        if len(columns):
            self.columns = columns
        else:
            self.columns = self.default_columns

        self.define()

    def define(self):
        self.ordered_columns = self.columns
        self.unique_columns = set(self.columns + self.extra_columns)

        self.ordered_columns_with_id = [self.id_column] + self.columns
        self.unique_columns_with_id = set([self.id_column] + self.columns + self.extra_columns)

    def add(self, items):
        self.unique_columns.update(set(items))
        self.unique_columns_with_id.update(set(items))

        self.ordered_columns.extend(items)
        self.ordered_columns_with_id.extend(items)


def do_imputations(df):
    for questionnaire_imputation in imputation_questionnaires:
        impute_from_questionnaire(df, questionnaire_imputation['origin'], questionnaire_imputation['replacement'])

    return df


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


def compute_questions_scores(df, questionnaires_map, variables_list):
    for questionnaire in questionnaires_map.keys():
        try:
            df, scores_columns_names = questionnaires_map[questionnaire]['scoring_function'](df)
            variables_list.add(scores_columns_names)
        except KeyError:
            pass

    return df, variables_list


def save_df(df, columns, axis='patient', profile=False):
    if axis == 'patient':

        df_intake = df[df.measurement == 'time1'][columns.ordered_columns_with_id]
        df_target = df[df.measurement == 'time2'][columns.ordered_columns_with_id]

        df = pd.merge(df_intake, df_target, on='id', how='outer', suffixes=('_time1', '_time2'))
        df = df.drop(['measurement_time1', 'measurement_time2'], axis=1)

        df.to_csv("DeppClinic_patient_data.csv", index=False)

    elif axis == 'time':
        df[columns.ordered_columns_with_id].to_csv("DeppClinic_prediction_task.csv", index=False)
        if profile:
            to_profile = df[columns.unique_columns]
            profile = pp.ProfileReport(to_profile, title="DeppClinic_prediction_task")
            profile.to_file(
                fr"research/create_dataset/dataset_for_prediction_task/pandas_profiling/DeppClinic_prediction_task_profile_report.html")
