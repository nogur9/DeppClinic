# import pandas_profiling as pp
import numpy as np


class TargetVariable:
    def __init__(self, name, info, columns, do_preprocessing=True):

        self.info = info
        self.name = name
        self.columns = columns
        self.do_preprocessing = do_preprocessing

    def calculate_value(self, df):
        df = self.calculate_missing_values(df)

        columns_need_preprocessing = [i for i in self.columns if 'chameleon' in i]
        columns_need_preprocessing += [i for i in self.columns if i in ['mfq_34', 'mfq_35', 'mfq_36', 'mfq_37']]
        fine_columns = [i for i in self.columns if i not in columns_need_preprocessing]
        aligned_columns = [f"{i}_align" for i in columns_need_preprocessing]

        align_df = df

        align_df[aligned_columns] = align_df[columns_need_preprocessing].replace(2, 0)
        align_df[aligned_columns] = align_df[aligned_columns].replace(3, 0)

        align_df = align_df[fine_columns + aligned_columns]

        df[self.name] = (align_df.sum(axis=1) > 0).astype(int)
        df.loc[df[f'ratio_of_missing_{self.name}_values'] >= 1, self.name] = np.nan

        return df

    def calculate_missing_values(self, df):

        missing_values = df[self.columns].isnull()
        missing_values_sum = missing_values.sum(axis=1)
        df[f'ratio_of_missing_{self.name}_values'] = missing_values_sum / len(self.columns)

        return df

    def create_plot(self, df, path='plots'):
        to_profile = df[[self.name]+self.columns]
        profile = pp.ProfileReport(to_profile)
        profile.to_file(fr"{path}/{self.name}.html")