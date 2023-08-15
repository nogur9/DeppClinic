
import pandas as pd
from Irit.psychodiagnostic_computations import compute_swan_scores, compute_sdq_scores, compute_cbcl_scores

from utils.consts.assistment_consts import Questionnaires
from utils.consts.pathology_variables import pathology_variables_times
from utils.consts.questions_columns import basic_info_columns, swan_m, sdq
from utils.target_variable import TargetVariable

df = pd.read_csv(r"../creating_the_clinic_dataset/preprocessed_data/merged_2021_and_2022.csv")
df = df[df['redcap_event_name'] == 'intake_arm_1']

questionnaires = Questionnaires().questionnaires


info_columns = basic_info_columns
swan_m_columns = questionnaires['swan_mother']['columns']
sdq_columns = questionnaires['sdq']['columns']

columns = []
for questionnaire_name, items in pathology_variables_times['intake'].items():
    tv = TargetVariable(questionnaire_name, {'measurement': 'time1'}, items)
    df = tv.calculate_value(df)
    df = tv.calculate_missing_values(df)
    columns.append([questionnaire_name, f'ratio_of_missing_{questionnaire_name}_values'])

df = df[basic_info_columns + swan_m_columns + sdq_columns]

df, scores_columns_names = questionnaires['sdq']['scoring_function'](df)

df, params_swan = compute_swan_scores(df)
df, params_sdq = compute_sdq_scores(df)





