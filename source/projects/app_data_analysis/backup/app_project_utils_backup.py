import pingouin as pg
import plotly.graph_objs as go
import pandas as pd
import os
from source.utils.pathology_assessment import pathology_variables_times
import plotly.express as px
import statsmodels.api as sm
from sklearn.preprocessing import LabelEncoder, StandardScaler


def anova_test(df, target, time):
    print(target, 'X', time)
    df = df[df.time.isin(['Time 1', time])]
    try:
        results = pg.anova(data=df, dv=target, between=['used_app', 'time'])[['Source', 'F', 'p-unc']]
    except ValueError:
        results = 'Invalid data'
    print(results, '\n\n\n\n\n')


def logistic_regression_test(df, target, time):
    df = df[df.time.isin(['Time 1', time])]
    X = df[['time', 'used_app']]
    Y = df[target]

    label_encoder_of_group = LabelEncoder()
    standard_scaler = StandardScaler()

    X['used_app'] = label_encoder_of_group.fit_transform(X['used_app'])
    X['time'] = label_encoder_of_group.fit_transform(X['time'])
    X[['used_app', 'time']] = standard_scaler.fit_transform(X[['used_app', 'time']])
    X['interaction'] = X['time'] * X['used_app']

    model = sm.Logit(Y, X).fit()

    wald_test_with_interation = model.wald_test('time + used_app + interaction = 0')
    wald_test_linear = model.wald_test('time + used_app = 0')

    print(time, "\n", target, f"\n{wald_test_with_interation = }")
    #print(f"{wald_test_linear = }")


def create_directories(dir):
    if not os.path.exists("plots"):
        os.mkdir("plots")

    if not os.path.exists(f"plots/{dir}"):
        os.mkdir(f"plots/{dir}")


def used_app(x, app_ids):
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
    else:
        raise ValueError
    df["intake_date"] = pd.to_datetime(df["sciafca_timestamp"], errors='coerce')

    app_ids = pd.read_csv(r"../../../Data/helper_docs/APP_patient_ids.csv")
    df['used_app'] = df.apply(used_app, args=[app_ids], axis=1)
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
        'suicidal_ideation_life_intake': 'suicidal_ideation_time2',
        'ER_intake': 'ER_time2',
        'Psychiatric_hospitalization_intake': 'Psychiatric_hospitalization_time2'
    }

    continuous_target_vars = ['DERS_score', 'erc_rc_anxiety', 'wai_goal', 'wai_task', 'wai_bond']
    discrete_target_vars = ['suicidal_ideation_time2', 'suicidal_behavior_time2', 'nssi_time2']
    info_cols = ['group', 'used_app', 'measurement', 'id']

    target_variables = {
        'continuous_target_vars': continuous_target_vars,
        'discrete_target_vars': discrete_target_vars,
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

    df = df[target_variables['continuous_target_vars'] + target_variables['discrete_target_vars'] + target_variables['info_cols']]
    df['time'] = df['measurement']
    return df


def plot_histogram(df, target, time):
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


def intake_bar_plot(df, target_variable):
    _, _, stats = pg.chi2_independence(data=df, x=target_variable, y='group')
    stats = stats[stats.test == 'pearson'].round(3)[['pval', 'power']].to_string(index=False).split('\n')
    stat_text = f"<b>chi_square Result:</b><br>{stats[0]}</b><br>{stats[1]}"

    chart_data = pd.concat([
        pd.Series(df.index, index=df.index, name='__index__'),
        df['group'],
        df[target_variable],
    ], axis=1)
    chart_data = chart_data.query(f"""(`{target_variable}` == 1) or (`{target_variable}` == 0)""")
    chart_data = chart_data.sort_values([target_variable, 'group'])
    chart_data = chart_data.rename(columns={'group': 'x'})
    chart_data_pctct = chart_data.groupby([target_variable, 'x'])[['__index__']].count()
    chart_data_pctct = chart_data_pctct / chart_data_pctct.groupby(['x']).count()
    chart_data_pctct.variables_to_export = ['__index__|pctct']
    chart_data = chart_data_pctct.reset_index()
    chart_data = chart_data.dropna()

    chart_data = chart_data.query(f"""{target_variable} == 1""")

    charts = [go.Bar(
        x=chart_data['x'],
        y=chart_data['__index__|pctct'],
        name=f"({target_variable.replace('_time2', '')}: 1)",
        marker_color='red'
    )]

    chart_data = pd.concat([
        pd.Series(df.index, index=df.index, name='__index__'),
        df['group'],
        df[target_variable],
    ], axis=1)
    chart_data = chart_data.query(f"""(`{target_variable}` == 1) or (`{target_variable}` == 0)""")
    chart_data = chart_data.sort_values([target_variable, 'group'])
    chart_data = chart_data.rename(columns={'group': 'x'})
    chart_data_pctct = chart_data.groupby([target_variable, 'x'])[['__index__']].count()
    chart_data_pctct = chart_data_pctct / chart_data_pctct.groupby(['x']).count()
    chart_data_pctct.variables_to_export = ['__index__|pctct']
    chart_data = chart_data_pctct.reset_index()
    chart_data = chart_data.dropna()
    # WARNING: This is not taking into account grouping of any kind, please apply filter associated with
    #          the group in question in order to replicate chart. For this we're using '"""`gender` == 'man'"""'
    chart_data = chart_data.query(f"""`{target_variable}` == 0""")

    charts.append(go.Bar(
        x=chart_data['x'],
        y=chart_data['__index__|pctct'],
        name=f"({target_variable.replace('_time2', '')}: 0)",
        marker_color='green'
    ))

    figure = go.Figure(data=charts, layout=go.Layout({
        'barmode': 'group',
        'legend': {'orientation': 'h'},
        'title': {'text': f"Rate of {target_variable.replace('_time2', '')} by Treatment Group"},
        'xaxis': {'tickformat': '0:g', 'title': {'text': 'group'}},
        'yaxis': {'tickformat': '0:g', 'title': {'text': 'Count'}, 'type': 'linear'},
    }))
    figure.add_annotation(
        x=1,
        y=1,
        text=stat_text,
        showarrow=False,
        font=dict(size=11, color='black'),
        bgcolor='lightgray',
        bordercolor='black',
        borderwidth=1,
        borderpad=12,
        xref='paper',
        yref='paper'
    )
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

    import plotly.graph_objs as go

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


def continuous_descriptive_plots(df, target_variables, dir):
    for target_variable in target_variables['continuous_target_vars']:
        figure = px.histogram(df, x=target_variable, color=df['time'], title=f"Distplot of {target_variable} by time", nbins=30)
        figure.write_html(os.path.join(f"plots/{dir}", f"{target_variable} by time.html"))
        figure.show()


def discrete_descriptive_plots(df, target_variables, dir):
    for target_variable in target_variables['discrete_target_vars']:
        figure = px.histogram(df, x=target_variable, color=df['time'], title=f"Distplot of {target_variable} by time", nbins=30)
        figure.write_html(os.path.join(f"plots/{dir}", f"{target_variable} by time.html"))
        figure.show()


def perform_continuous_tests(df, target_variables, dir):
    for time in ['Time 2', 'Time 3']:
        for target in target_variables['continuous_target_vars']:
            figure = plot_histogram(df, target, time)
            figure.write_html(os.path.join(f"plots/{dir}", f"{time}_{target}.html"))
            anova_test(df, target, time)


def perform_discrete_tests(df, target_variables, dir):
    for time in ['Time 2', 'Time 3']:
        for target_variable in target_variables['discrete_target_vars']:
            figure = discrete_treatment_improvement_plot(df, target_variable, time)
            figure.write_html(os.path.join(f"plots/{dir}", f"{time}_{target_variable}.html"))
            logistic_regression_test(df, target_variable, time)
