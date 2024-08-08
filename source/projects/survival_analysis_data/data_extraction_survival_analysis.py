import pandas as pd
from source.utils.consts.questions_columns import demographics_m
from source.utils.consts.assistment_consts import Questionnaires
from source.utils.dataset_creation import GROUP_NAMES_MAP, rename_groups, fill_missing_groups
from source.utils.dataset_creation import VariablesToExport, \
    do_questionnaires_imputations, save_df, split_to_multiple_measurement_times, compute_questions_scores
from source.utils.pathology_assessment import pathology_variables_times
from source.utils.old_questionnaires_scores.target_variable import TargetVariable
import os
from source.utils.util_functions import impute


def parse_datetime(date_str):
    try:
        return pd.to_datetime(date_str)
    except ValueError:
        try:
            return pd.to_datetime(date_str.split(" ")[0], errors='coerce')

        except AttributeError:
            return pd.NaT


def main(times, directory_path=None, suffix='', columns=None, calc_pathology=True, calc_scores=True):
    # Change the current directory to the source root

    df = pd.read_csv(r"C:\Users\nogur\Documents\DeppClinic\Data\postgres_db\merged_data\merged_2021_and_2022.csv",
                     na_values='chameleon_ideation_stu_2022', keep_default_na=True)
    print(f"{df.shape = }")
    columns = VariablesToExport(columns)
    df = do_questionnaires_imputations(df)

    target_times = ['sciafca_timestamp', 'mfq_short_timestamp', 'chameleon_timestamp',
                    'chameleon_suicide_er_date_stu', 'chameleon_psychiatric_date_stu',
                    'opening_child_pre_timestamp', 'cssrs_timestamp', 'siq_timestamp']
    intake_times = ['opening_timestamp', 'mfq_short_timestamp', 'complaint_date']

    for col in target_times + intake_times:
        df[col] = df[col].apply(parse_datetime)

    target_var = ['visit_date_stu'] * (len(target_times)+1)
    intake_var = ['sciafca_timestamp'] * (len(intake_times)+1)

    df = impute(target_var, target_times, df, multiple_options=True)
    df = impute(intake_var, intake_times, df, multiple_options=True)

    df = rename_groups(df, GROUP_NAMES_MAP)
    df = fill_missing_groups(df, GROUP_NAMES_MAP)
    columns.add(['group', 'visit_date_stu', 'sciafca_timestamp'])
    df_time1, df_time2 = split_to_multiple_measurement_times(df, columns, times)
    columns.add(['measurement'])

    if calc_pathology:
        # calculate pathology variables
        for questionnaire_name, items in pathology_variables_times['intake'].items():
            tv = TargetVariable(questionnaire_name, {'measurement': 'time1'}, items)
            df_time1 = tv.calculate_value(df_time1)
            columns.add([questionnaire_name])

        for questionnaire_name, items in pathology_variables_times['time2'].items():
            tv = TargetVariable(questionnaire_name, {'measurement': 'time2'}, items)
            df_time2 = tv.calculate_value(df_time2)
            columns.add([questionnaire_name, f'ratio_of_missing_{questionnaire_name}_values'])

    df = pd.concat([df_time1, df_time2])
    df = df[list(columns.unique_columns_with_id)]

    if calc_scores:
        questionnaires = Questionnaires(['mfq', 'sdq', 'c_ssrs_intake', 'siq', 'sci_af_ca']).questionnaires
        df, columns = compute_questions_scores(df, questionnaires, columns)

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    save_df(df, columns, axis='patient', directory_path=directory_path, suffix=suffix)


all_times = {
    'intake': ['intake_arm_1', 'er_arm_1'],
    'pre_treatment_arm_1': ['pre_treatment_arm_1'],
    'control_5weeks_arm_1': ['control_5weeks_arm_1'],
    '5th_session_arm_1': ['5th_session_arm_1'],
    'followup_3month_arm_1': ['followup_3month_arm_1'],
    'control_3month_arm_1': ['control_3month_arm_1'],
    'control_6month_arm_1': ['control_6month_arm_1'],

    # new times:

    'control_12month_arm_1': ['control_12month_arm_1'],
    'control_9month_arm_1': ['control_9month_arm_1'],
    'er_one_week_arm_1': ['er_one_week_arm_1'],
    'followup_12month_arm_1': ['followup_12month_arm_1'],
    'post_treatment_arm_1': ['post_treatment_arm_1']
}

main(all_times, r"C:\Users\nogur\Documents\DeppClinic\Data\processed_data\survival_analysis_20_3")


single_time = {
    'intake': ['intake_arm_1', 'er_arm_1', 'pre_treatment_arm_1', 'control_5weeks_arm_1',
         '5th_session_arm_1', 'followup_3month_arm_1', 'control_3month_arm_1',
         'control_6month_arm_1', 'control_12month_arm_1', 'control_9month_arm_1',
         'er_one_week_arm_1', 'followup_12month_arm_1', 'post_treatment_arm_1']
}
main(single_time, columns=demographics_m,
     directory_path=r"C:\Users\nogur\Documents\DeppClinic\Data\processed_data\survival_analysis_20_3",
     suffix='_demographics', calc_pathology=False, calc_scores=False)
