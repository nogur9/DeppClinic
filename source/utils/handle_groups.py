import pandas as pd
import os

class GroupManager:
    GROUPS = ['group___1', 'group___2', 'group___3']
    GROUP_NAMES_MAP = {
        '0': 'invalid',
        '1': 'ipt',  # חירום
        '2': 'tau',  # רגיל
        '3': 'control'  # מינימלית
    }
    GROUP_IMPUTATION_FILE = r"Data\helper_docs\group_imputations.csv"

    def __init__(self, df, content_root):
        self.content_root = content_root
        self.df = df.copy()

    def decode_group_column(self):
        """Decodes group flags into a single group column based on predefined mappings."""
        df = self.df.copy()
        df['group'] = '0'
        df.loc[df['group___1'] == 1, 'group'] = '1'
        df.loc[df['group___2'] == 1, 'group'] = '2'
        df.loc[df['group___3'] == 1, 'group'] = '3'
        df['group'] = df['group'].map(self.GROUP_NAMES_MAP)
        self.df = df

    def impute_missing_groups(self):
        df = self.df.copy()
        group_imputation_file_path = os.path.join(self.content_root, self.GROUP_IMPUTATION_FILE)
        filling_map = pd.read_csv(group_imputation_file_path)
        inv_group_names = {v: k for k, v in self.GROUP_NAMES_MAP.items()}

        for _, row in filling_map.iterrows():
            group_number = row['group_name']
            group_col_name = f"group___{inv_group_names[group_number]}"
            df.loc[df['id'] == row['id'], 'group'] = group_number
            df.loc[df['id'] == row['id'], group_col_name] = 1
        self.df = df

    def process(self):
        self.decode_group_column()
        self.impute_missing_groups()
        return self.df


def fill_group_column_redcap_dataset(df, group_column_name):

    df = df.copy()
    group_map = df.dropna(subset=[group_column_name]).groupby('id')[group_column_name].first()
    group_map = {key: group_map[key] for key in group_map.keys()}

    df[group_column_name] = df['id'].apply(lambda x: group_map.get(x))

    return df

