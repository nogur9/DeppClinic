# import pandas_profiling as pp


class TargetVariable:
    def __init__(self, name, info, columns, do_preprocessing=True):

        self.info = info
        self.name = name
        self.columns = columns
        self.do_preprocessing = do_preprocessing

    def calculate_value(self, df):
        columns_aligns = [i for i in self.columns if 'chameleon' not in i]
        columns_chameleon = [i for i in self.columns if 'chameleon' in i]
        aligned_columns_chameleon = [f"{i}.align" for i in columns_chameleon]

        align_df = df
        align_df[aligned_columns_chameleon] = align_df[columns_chameleon].replace(2, 0)
        align_df[aligned_columns_chameleon] = align_df[columns_chameleon].replace(3, 0)
        align_df = align_df[columns_aligns + aligned_columns_chameleon]
        df[self.name] = (align_df.sum(axis=1) > 0).astype(int)
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