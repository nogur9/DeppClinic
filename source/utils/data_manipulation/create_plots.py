import pandas_profiling as pp


def simple_eda(df, columns, title, path='', rename = None, display_additional_columns=True):
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