import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(rc={'figure.figsize':(11,8)})
sns.set(font_scale=1.2)
import numpy as np
from old_process.step2_merge_2021_2022.utils import fix_wrong_record_id, fill_id, format_datetime_columns, delete_redundant_columns, mark_inattentive_participants, fix_age, \
    delete_negative_age, fill_missing_age, fill_age
from transferring_data_to_postgreSQL.original_process.creating_the_clinic_dataset.step2_merge_2021_2022.columns_index_for_merging import columns_dict, merging_functions_by_columns_set, weird_text_columns


def impute_from_column(df, impute_to, impute_from):
    """
    test:
    df[(df['c_ssrs_6'].isna()) & (~df['c_ssrs_last_visit_6'].isna())][['c_ssrs_6', 'c_ssrs_last_visit_6']]
    df = impute_from_column(df, impute_to = 'c_ssrs_6', impute_from = 'c_ssrs_last_visit_6')
    df[(df['c_ssrs_6'].isna()) & (~df['c_ssrs_last_visit_6'].isna())][['c_ssrs_6', 'c_ssrs_last_visit_6']]

    """
    df[impute_to] = np.where(df[impute_to].isnull(), df[impute_from], df[impute_to])

    return df


df_2022 = pd.read_csv(r'../preprocessed_data/2022_data_imputed_with_clin_stu.csv', na_values=' ')
df_2021 = pd.read_csv(r'../preprocessed_data/2021_data_imputed_with_clin_stu.csv', na_values=' ')

df_2022 = delete_negative_age(df_2022)
df_2021 = delete_negative_age(df_2021)

df_2021 = impute_from_column(df_2021, impute_to = 'age_child_pre', impute_from = 'age_child_pre_first')


df_2021 = fix_wrong_record_id(df_2021, year=2021)
df_2022 = fix_wrong_record_id(df_2022, year=2022)

df_2022 = fill_id(df_2022)
