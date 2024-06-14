import pingouin as pg
import pandas as pd
import os
from source.utils.consts.predefined_pathologies import pathology_variables_times
import statsmodels.api as sm
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
import plotly.graph_objs as go


def create_directories(path, dir_name):
    if not os.path.exists(path):
        os.mkdir(path)

    if not os.path.exists(f"{path}/{dir_name}"):
        os.mkdir(f"{path}/{dir_name}")


def used_app(x):
    app_ids = pd.read_csv(r"../../../Data/helper_docs/APP_patient_ids.csv")
    if x['id'] in list(app_ids['patient_id']):
        return True
    else:
        return False


def filter_samples(df, age, groups):
    df = df[df.age_child_pre <= age]
    df = df[df.group.isin(groups)]
    return df


def load_data(group):
    if group == 'treatment':
        df = pd.read_csv(r"data\DeppClinic_patient_data_treatment.csv")
    elif group == 'control':
        df = pd.read_csv(r"data\DeppClinic_patient_data_control.csv")
    elif group == 'all':
        df = pd.read_csv(r"data\DeppClinic_patient_data_all.csv")
    else:
        raise ValueError
    df["intake_date"] = pd.to_datetime(df["sciafca_timestamp"], errors='coerce')

    df['used_app'] = df.apply(used_app, axis=1)
    return df


def get_target_variables():
    intake_target_variables = list(pathology_variables_times['intake'].keys()) + ['c_ssrs_intake_life_stb']

    time2_target_variables = list(pathology_variables_times['time2'].keys()) + ['c_ssrs_stb_score']

    target_variables_per_time = {
        'Time 1': intake_target_variables,
        'Time 2': time2_target_variables,
        'Time 3': time2_target_variables}

    intake_to_time2_map = {
        'c_ssrs_intake_life_stb': 'c_ssrs_stb_score',
        'suicidal_behavior_intake': 'suicidal_behavior_time2',
        'nssi_intake': 'nssi_time2',
        'suicidal_ideation_life_intake': 'suicidal_ideation_time2'
    }

    continuous_target_vars = ['DERS_score', 'DERS_non_accept', 'DERS_goals',
                            'DERS_IMPULS', 'DERS_STRATEG', 'DERS_CLARITY', 'DERS_AWARE',
                              'erc_rc_anxiety', 'erc_rc_avoidance', 'mfq_score']
    discrete_target_vars = ['suicidal_ideation_time2', 'suicidal_behavior_time2', 'nssi_time2']
    info_cols = ['group', 'used_app', 'measurement', 'id']

    target_variables = {
        'continuous_target_vars': continuous_target_vars,
        'discrete_target_vars': discrete_target_vars,
        'wai_target_vars': ['wai_goal', 'wai_task', 'wai_bond'],
        'info_cols': info_cols,
        'intake_to_time2_map': intake_to_time2_map,
        'target_variables_per_time': target_variables_per_time,
        'time2_target_variables': time2_target_variables,
        'intake_target_variables': intake_target_variables
    }
    return target_variables


def align_multiple_measurement_times(df, target_variables, age, groups):
    df = filter_samples(df, age=age, groups=groups)
    time1_df = df[df.measurement.isin(['Time 1'])]
    time1_df = time1_df.drop(target_variables['time2_target_variables'], axis=1)
    time1_df = time1_df.rename(target_variables['intake_to_time2_map'], axis=1)

    time2_df = df[df.measurement.isin(['Time 2'])]
    time3_df = df[df.measurement.isin(['Time 3'])]
    df = pd.concat([time1_df, time2_df, time3_df])

    df = df[target_variables['continuous_target_vars'] + target_variables['discrete_target_vars'] +
            target_variables['info_cols'] + target_variables['wai_target_vars']]
    df['time'] = df['measurement']
    return df


def continuous_treatment_improvement_plot(df, target, time):
    chart_data = pd.concat([
        pd.Series(df.index, index=df.index, name='__index__'),
        df[target],
        df['used_app'],
        df['time'],
    ], axis=1)

    chart_data = chart_data.query(f"""`time` == '{time}'""")
    chart_data = chart_data.sort_values(['used_app', target])

    chart_data = chart_data.rename(columns={target: 'x'})
    chart_data = chart_data.dropna()

    chart_data_control = chart_data.query("""`used_app` == False""")
    chart_data_used_app = chart_data.query("""`used_app` == True""")
    charts = [go.Histogram(
        x=chart_data_control['x'],
        nbinsx=10,
        name="Didn't used the app"
    ), go.Histogram(
        x=chart_data_used_app['x'],
        nbinsx=10,
        name="Used the app"
    )]

    figure = go.Figure(data=charts, layout=go.Layout({
        'legend': {'orientation': 'h', 'y': -0.3},
        'title': {'text': f'{target} X {time}'},
        'xaxis': {'title': {'text': target}},
        'yaxis': {'tickformat': '0:g', 'title': {'text': 'Count of __index__'}, 'type': 'linear'}
    }))

    figure.show()
    return figure


def discrete_treatment_improvement_plot(df, target_variable, time="Time 3"):
    # remove any pre-existing indices for ease of use in the D-Tale code, but this is not required
    df = df.reset_index().drop('index', axis=1, errors='ignore')
    df.variables_to_export = [str(c) for c in df.variables_to_export]  # update columns to strings in case they are numbers

    chart_data = pd.concat([
        df['used_app'],
        df[target_variable],
        df['time'],
    ], axis=1)
    chart_data = chart_data.query(f"""(`time` == 'Time 1') or (`time` == '{time}')""")
    chart_data = chart_data.rename(columns={'used_app': 'x'})
    chart_data_mean = chart_data.groupby(['time', 'x'], dropna=True)[[target_variable]].mean()
    chart_data_mean.variables_to_export = [f'{target_variable}||mean']
    chart_data = chart_data_mean.reset_index()
    chart_data = chart_data.dropna()
    # WARNING: This is not taking into account grouping of any kind, please apply filter associated with
    #          the group in question in order to replicate chart. For this we're using '"""`time` == 'intake'"""'

    charts = []

    intake_chart_data = chart_data.query("""`time` == 'Time 1'""")
    charts.append(go.Bar(
        x=intake_chart_data['x'],
        y=intake_chart_data[f'{target_variable}||mean'],
        name='(time: intake)'
    ))

    time3_chart_data = chart_data.query(f"""`time` == '{time}'""")
    charts.append(go.Bar(
        x=time3_chart_data['x'],
        y=time3_chart_data[f'{target_variable}||mean'],
        name='(time: follow up)'
    ))

    figure = go.Figure(data=charts, layout=go.Layout({
        'barmode': 'group',
        'legend': {'orientation': 'h', 'y': -0.3},
        'title': {'text': f"Rate of {target_variable.replace('_time2', '')} by Used App"},
        'xaxis': {'title': {'text': 'used_app'}},
        'yaxis': {'title': {'text': f"Rate of {target_variable.replace('_time2', '')}"}, 'type': 'linear'}
    }))

    figure.show()
    return figure


class StatisticalAnalyzer:

    def __init__(self, df, target_variable, time, data_type):
        self.df = df
        self.target_variable = target_variable
        self.time = time
        self.data_type = data_type
        self.results = None
        self.data = None
        self.perform_statistical_test()

    def is_significant(self):
        if self.results is None:
            return False
            #raise ValueError
        elif self.data_type == 'Discrete':
            p_value = self.results.pvalue
        elif self.data_type == 'Continuous':
            p_value = self.results.query("Source == 'used_app * time'")['p-unc'].values[0]

        elif self.data_type == 'wai':
            p_value = self.results['p-val'].values[0]
        else:
            raise ValueError

        return p_value <= 0.1

    def create_directories(self):
        create_directories(f'results', self.time)
        create_directories(f'results/{self.time}', self.target_variable)

    def anova_test(self):
        df = self.df[self.df.time.isin(['Time 1', self.time])]
        try:
            results = pg.anova(data=df, dv=self.target_variable, between=['used_app', 'time'])[['Source', 'F', 'p-unc']]
            data = df[['id', 'used_app', 'time', self.target_variable]]
            self.results = results
            self.data = data
        except ValueError:
            print('Invalid data')

    def plot(self):
        # remove any pre-existing indices for ease of use in the D-Tale code, but this is not required
        df = self.df.reset_index().drop('index', axis=1, errors='ignore')
        df.loc[df['used_app']==True, 'used_app'] = 'App User'
        df.loc[df['used_app']==False, 'used_app'] = 'Not used App'
        df.variables_to_export = [str(c) for c in df.variables_to_export]  # update columns to strings in case they are numbers

        chart_data = pd.concat([
            df['used_app'],
            df[self.target_variable],
            df['time'],
        ], axis=1)
        chart_data = chart_data.query(f"""(`time` == 'Time 1') or (`time` == '{self.time}')""")
        chart_data = chart_data.rename(columns={'used_app': 'x'})
        chart_data_mean = chart_data.groupby(['time', 'x'], dropna=True)[[self.target_variable]].mean()
        chart_data_mean.variables_to_export = [f'{self.target_variable}||mean']
        chart_data = chart_data_mean.reset_index()
        chart_data = chart_data.dropna()
        # WARNING: This is not taking into account grouping of any kind, please apply filter associated with
        #          the group in question in order to replicate chart. For this we're using '"""`time` == 'intake'"""'

        charts = []

        intake_chart_data = chart_data.query("""`time` == 'Time 1'""")
        charts.append(go.Bar(
            x=intake_chart_data['x'],
            y=intake_chart_data[f'{self.target_variable}||mean'],
            name='(time: intake)'
        ))

        time3_chart_data = chart_data.query(f"""`time` == '{self.time}'""")
        charts.append(go.Bar(
            x=time3_chart_data['x'],
            y=time3_chart_data[f'{self.target_variable}||mean'],
            name='(time: follow up)'
        ))

        figure = go.Figure(data=charts, layout=go.Layout({
            'barmode': 'group',
            'legend': {'orientation': 'h', 'y': -0.3},
            'title': {'text': f"Rate of {self.target_variable.replace('_time2', '')} by Used App"},
            'xaxis': {'title': {'text': 'used_app'}},
            'yaxis': {'title': {'text': f"Rate of {self.target_variable.replace('_time2', '')}"}, 'type': 'linear'}
        }))

        figure.show()
        return figure

    def wai_plot(self):
        # remove any pre-existing indices for ease of use in the D-Tale code, but this is not required
        df = self.df.reset_index().drop('index', axis=1, errors='ignore')
        df.loc[df['used_app']==True, 'used_app'] = 'App User'
        df.loc[df['used_app']==False, 'used_app'] = 'Not used App'

        chart_data = pd.concat([
            df['used_app'],
            df[self.target_variable],
            df['time'],
        ], axis=1)
        chart_data = chart_data.query(f"""(`time` == '{self.time}')""")
        chart_data = chart_data.rename(columns={'used_app': 'x'})
        chart_data_mean = chart_data.groupby(['x'], dropna=True)[[self.target_variable]].mean()
        chart_data_mean.variables_to_export = [f'{self.target_variable}||mean']
        chart_data = chart_data_mean.reset_index()
        chart_data = chart_data.dropna()
        # WARNING: This is not taking into account grouping of any kind, please apply filter associated with
        #          the group in question in order to replicate chart. For this we're using '"""`time` == 'intake'"""'

        chart = go.Bar(
            x=chart_data['x'],
            y=chart_data[f'{self.target_variable}||mean'],
        )

        figure = go.Figure(data=chart, layout=go.Layout({
            'barmode': 'group',
            'legend': {'orientation': 'h', 'y': -0.3},
            'title': {'text': f"Rate of {self.target_variable.replace('_time2', '')} by Used App"},
            'xaxis': {'title': {'text': 'used_app'}},
            'yaxis': {'title': {'text': f"Rate of {self.target_variable.replace('_time2', '')}"}, 'type': 'linear'}
        }))

        figure.show()
        return figure

    def perform_statistical_test(self):
        if self.data_type == 'Discrete':
            self.logistic_regression_test()
        elif self.data_type == 'Continuous':
            self.anova_test()
        elif self.data_type == 'wai':
            self.t_test()
        else:
            raise ValueError

    def logistic_regression_test(self):
        df = self.df[self.df.time.isin(['Time 1', self.time])]
        df = df.dropna(subset=[self.target_variable])
        X = df[['time', 'used_app']]
        Y = df[self.target_variable]

        label_encoder_of_group = LabelEncoder()
        standard_scaler = StandardScaler()

        X['used_app'] = label_encoder_of_group.fit_transform(X['used_app'])
        X['time'] = label_encoder_of_group.fit_transform(X['time'])
        X[['used_app', 'time']] = standard_scaler.fit_transform(X[['used_app', 'time']])
        X['interaction'] = X['time'] * X['used_app']

        model = sm.Logit(Y, X).fit()
        wald_test_with_interation = model.wald_test('time + used_app + interaction = 0')
        data = df[['id', 'used_app', 'time', self.target_variable]]

        self.results = wald_test_with_interation
        self.data = data

        wald_test_linear = model.wald_test('time + used_app = 0')

    def t_test(self):
        df = self.df[self.df.time == self.time]
        x = df[df.used_app][self.target_variable]
        y = df[~ df.used_app][self.target_variable]
        try:
            results = pg.ttest(x, y)
            data = df[['id', 'used_app', 'time', self.target_variable]]
            self.results = results
            self.data = data
        except AssertionError:
            print('Invalid data')

    def print_results(self):
        print(self.target_variable, 'X', self.time)
        print(self.results, '\n\n\n\n\n')


def perform_continuous_tests(df, target_variables):
    for time in ['Time 2', 'Time 3']:
        for target in target_variables['continuous_target_vars']:
            continuous_test = StatisticalAnalyzer(df, target, time, 'Continuous')
            if continuous_test.is_significant():
                continuous_test.create_directories()
                figure = continuous_test.plot()
                figure.write_html(os.path.join(f"results/{time}/{target}", "plot.html"))
                continuous_test.data.to_csv(f"results/{time}/{target}/data.html", index=False)
                continuous_test.print_results()


def perform_discrete_tests(df, target_variables):
    for time in ['Time 2', 'Time 3']:
        for target in target_variables['discrete_target_vars']:
            print(f"{target = }")
            continuous_test = StatisticalAnalyzer(df, target, time, 'Discrete')
            if continuous_test.is_significant():
                continuous_test.create_directories()
                figure = continuous_test.plot()
                figure.write_html(os.path.join(f"results/{time}/{target}", "plot.html"))
                continuous_test.data.to_csv(f"results/{time}/{target}/data.html", index=False)
                continuous_test.print_results()


def perform_wai_tests(df, target_variables):
    for time in ['Time 2', 'Time 3']:
        for target in target_variables['wai_target_vars']:
            continuous_test = StatisticalAnalyzer(df, target, time, 'wai')
            if continuous_test.is_significant():
                continuous_test.create_directories()
                figure = continuous_test.wai_plot()
                figure.write_html(os.path.join(f"results/{time}/{target}", "plot.html"))
                continuous_test.data.to_csv(f"results/{time}/{target}/data.html", index=False)
                continuous_test.print_results()

#
# def anova_test(df, target, time):
#     print(target, 'X', time)
#     df = df[df.time.isin(['Time 1', time])]
#     try:
#         results = pg.anova(data=df, dv=target, between=['used_app', 'time'])[['Source', 'F', 'p-unc']]
#     except ValueError:
#         results = 'Invalid data'
#     print(results, '\n\n\n\n\n')
#
#
# def logistic_regression_test(df, target, time):
#     df = df[df.time.isin(['Time 1', time])]
#     X = df[['time', 'used_app']]
#     Y = df[target]
#
#     label_encoder_of_group = LabelEncoder()
#     standard_scaler = StandardScaler()
#
#     X['used_app'] = label_encoder_of_group.fit_transform(X['used_app'])
#     X['time'] = label_encoder_of_group.fit_transform(X['time'])
#     X[['used_app', 'time']] = standard_scaler.fit_transform(X[['used_app', 'time']])
#     X['interaction'] = X['time'] * X['used_app']
#
#     model = sm.Logit(Y, X).fit()
#
#     wald_test_with_interation = model.wald_test('time + used_app + interaction = 0')
#     wald_test_linear = model.wald_test('time + used_app = 0')
#
#     print(time, "\n", target, f"\n{wald_test_with_interation = }")
#     #print(f"{wald_test_linear = }")
