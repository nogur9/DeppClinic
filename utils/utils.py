import pandas_profiling as pp
import numpy as np 
import pandas as pd


def impute_from_column(df, impute_to, impute_from):
    """
    test:
    df[(df['c_ssrs_6'].isna()) & (~df['c_ssrs_last_visit_6'].isna())][['c_ssrs_6', 'c_ssrs_last_visit_6']]
    df = impute_from_column(df, impute_to = 'c_ssrs_6', impute_from = 'c_ssrs_last_visit_6')
    df[(df['c_ssrs_6'].isna()) & (~df['c_ssrs_last_visit_6'].isna())][['c_ssrs_6', 'c_ssrs_last_visit_6']]
    
    """
    df[impute_to] = np.where(df[impute_to].isnull(), df[impute_from], df[impute_to])
    
    return df



def simple_eda(df, columns, title, path = '', rename = None, display_additional_columns=True):
    if display_additional_columns:
        additional_columns = ['id', 'gender', 'redcap_event_name', 'age_child']
    else:
        additional_columns = []
    if rename is None:
        to_profile = df[columns + additional_columns]
    else:
        to_profile = df[columns + additional_columns].rename(rename, axis=1)
    profile = pp.ProfileReport(to_profile, title=title)
    if path:
        profile.to_file(fr"{path}/{title}.html")
    else:
        profile.to_file(fr"{title}.html")


    