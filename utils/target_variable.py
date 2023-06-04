import pandas_profiling as pp


class TargetVariable:
    def __init__(self, name, info, columns, do_preprocessing=True):

        self.info = info
        self.name = name
        self.columns = columns
        self.do_preprocessing = do_preprocessing

    def calculate_value(self, df):
        if self.do_preprocessing:
            aligned_df = df[self.columns].replace(2, 0)
            df[self.name] = (aligned_df.sum(axis=1) > 0).astype(int)
        else:
            df[self.name] = (df[self.columns].sum(axis=1) > 0).astype(int)
        return df

    def create_plot(self, df, path='plots'):
        to_profile = df[[self.name]+self.columns]
        profile = pp.ProfileReport(to_profile)
        profile.to_file(fr"{path}/{self.name}.html")