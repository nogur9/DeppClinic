import pandas as pd
from source.utils.further_data_processing.create_dataset_for_prediction.pipeline_functions import Columns, do_questionnaires_imputations, split_two_measurement_times, compute_questions_scores, save_df
from source.utils.consts.pathology_variables import pathology_variables_times
from source.utils.target_variable import TargetVariable
from source.utils.consts.assistment_consts import Questionnaires
import os


def main():
    # Change the current directory to the source root
    os.chdir(r'C:\Users\nogur\Documents\DeppClinic')

    df = pd.read_csv(r"creating_the_clinic_dataset/preprocessed_data/merged_2021_and_2022.csv", na_values=' ')
    columns = Columns()
    df = do_questionnaires_imputations(df)

    df_time1, df_time2 = split_two_measurement_times(df, columns)
    columns.add(['measurement'])
    # calculate pathology variables
    for questionnaire_name, items in pathology_variables_times['intake'].items():
        tv = TargetVariable(questionnaire_name, {'measurement': 'time1'}, items)
        df_time1 = tv.calculate_value(df_time1)
        columns.add([questionnaire_name])

    for questionnaire_name, items in pathology_variables_times['time2'].items():
        tv = TargetVariable(questionnaire_name, {'measurement': 'time2'}, items)
        df_time2 = tv.calculate_value(df_time2)
        columns.add([questionnaire_name])

    df = pd.concat([df_time1, df_time2])
    df = df[columns.unique_columns_with_id]

    questionnaires = Questionnaires().questionnaires
    df, columns = compute_questions_scores(df, questionnaires, columns)

    save_df(df, columns, axis='patient', profile=False)
    save_df(df, columns, axis='time', profile=False)


main()




