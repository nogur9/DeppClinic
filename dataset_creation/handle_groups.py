import pandas as pd

GROUPS = ['group___1', 'group___2', 'group___3']

GROUP_NAMES_MAP = {
    '0': 'invalid',
    '1': 'ipt', # חירום
    '2': 'tau', # רגיל
    '3': 'control' # מינימלית
}

def fill_group(df, group):

    df = df.copy()
    group_map = df.dropna(subset=[group]).groupby('id')[group].first()
    group_map = {key: group_map[key] for key in group_map.keys()}

    def try_group_map(x):
        try:
            group_name = group_map[x]
            return group_name
        except KeyError:
            print(x)

    df[group] = df['id'].apply(try_group_map)

    return df


def rename_groups(df, group_names):
    df['group'] = '0'
    df.loc[df['group___1'] == 1, 'group'] = '1'
    df.loc[df['group___2'] == 1, 'group'] = '2'
    df.loc[df['group___3'] == 1, 'group'] = '3'
    df['group'] = df['group'].map(group_names)
    return df


def fill_missing_groups(df, group_names):
    filling_map = pd.read_csv(r"Data/helper_docs/group_imputations.csv")
    inv_group_names = {v: k for k, v in group_names.items()}
    for _, row in filling_map.iterrows():
        df.loc[df['id'] == row['id'], 'group'] = row['group_name']
        df.loc[df['id'] == row['id'], f"group___{inv_group_names[row['group_name']]}"] = 1
    return df

