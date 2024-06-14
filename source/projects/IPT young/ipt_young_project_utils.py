import pingouin as pg
import plotly.graph_objs as go
import pandas as pd
import os
from source.utils.consts.predefined_pathologies import pathology_variables_times
import plotly.express as px
import statsmodels.api as sm
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler


def anova_test(df, target, time):
    print(target, 'X', time)
    df = df[df.time.isin(['Time 1', time])]
    try:
        results = pg.anova(data=df, dv=target, between=['group', 'time'])[['Source', 'F', 'p-unc']]
    except ValueError:
        results = 'Invalid data'
    print(target, '\n', results, '\n\n\n\n\n')


def logistic_regression_test(df, target, time):
    df = df[df.time.isin(['Time 1', time])]
    X = df[['time', 'group']]
    Y = df[target]

    label_encoder_of_group = LabelEncoder()
    standard_scaler = StandardScaler()

    X['group'] = label_encoder_of_group.fit_transform(X['group'])
    X['time'] = label_encoder_of_group.fit_transform(X['time'])
    X[['group', 'time']] = standard_scaler.fit_transform(X[['group', 'time']])
    X['interaction'] = X['time'] * X['group']

    model = sm.Logit(Y, X).fit()

    wald_test_with_interation = model.wald_test('time + group + interaction = 0')
    wald_test_linear = model.wald_test('time + group = 0')

    print(time, "\n", target, f"\n{wald_test_with_interation = }")
    #print(f"{wald_test_linear = }")


def create_directories(path):
    if not os.path.exists("plots"):
        os.mkdir("plots")

    if not os.path.exists(f"plots/{path}"):
        os.mkdir(f"plots/{path}")


def filter_samples(df, age, groups):
    df = df[df.age_child_pre <= age]
    df = df[df.group.isin(groups)]
    return df


def load_data():
    ipt_df = pd.read_csv(r"data\DeppClinic_patient_data_treatment.csv")
    ipt_df = filter_samples(ipt_df, 12.5, ['ipt'])
    control_df = pd.read_csv(r"data\DeppClinic_patient_data_control.csv")
    control_df = filter_samples(control_df, 12.5, ['control'])

    df = pd.concat(([ipt_df, control_df]))
    df["intake_date"] = pd.to_datetime(df["sciafca_timestamp"], errors='coerce')

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

    variable_names_normalization = {
        'suicidal_ideation_time2': 'suicidal_ideation',
        'suicidal_behavior_time2': 'suicidal_behavior',
        'nssi_time2': 'NSSI'
    }

    continuous_target_vars = ['DERS_score', 'erc_rc_anxiety', 'wai_goal', 'wai_task', 'wai_bond']
    discrete_target_vars = ['suicidal_ideation', 'suicidal_behavior', 'NSSI']
    info_cols = ['group', 'measurement', 'id', 'age_child_pre']

    target_variables = {
        'continuous_target_vars': continuous_target_vars,
        'discrete_target_vars': discrete_target_vars,
        'info_cols': info_cols,
        'intake_to_time2_map': intake_to_time2_map,
        'target_variables_per_time': target_variables_per_time,
        'time2_target_variables': time2_target_variables,
        'intake_target_variables': intake_target_variables,
        'variable_names_normalization': variable_names_normalization
    }
    return target_variables


def align_multiple_measurement_times(df, target_variables):
    time1_df = df[df.measurement.isin(['Time 1'])]
    time1_df = time1_df.drop(target_variables['time2_target_variables'], axis=1)
    time1_df = time1_df.rename(target_variables['intake_to_time2_map'], axis=1)

    time2_df = df[df.measurement.isin(['Time 2'])]
    time3_df = df[df.measurement.isin(['Time 3'])]
    df = pd.concat([time1_df, time2_df, time3_df])
    df = df.rename(target_variables['variable_names_normalization'], axis=1)

    df = df[target_variables['continuous_target_vars'] + target_variables['discrete_target_vars'] +
            target_variables['info_cols']]
    df['time'] = df['measurement']
    return df

# ------------------------------------------------------------


def plot_histogram(df, target, time):
    chart_data = pd.concat([
        pd.Series(df.index, index=df.index, name='__index__'),
        df[target],
        df['group'],
        df['time'],
    ], axis=1)

    chart_data = chart_data.query(f"""`time` == '{time}'""")
    chart_data = chart_data.sort_values(['group', target])

    chart_data = chart_data.rename(columns={target: 'x'})
    chart_data = chart_data.dropna()

    chart_data_control = chart_data.query("""`group` == 'ipt'""")
    chart_data_ipt = chart_data.query("""`group` == 'control'""")
    charts = [go.Histogram(
        x=chart_data_control['x'],
        nbinsx=10,
        name="Control"
    ), go.Histogram(
        x=chart_data_ipt['x'],
        nbinsx=10,
        name="IPT"
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


def discrete_treatment_improvement_plot(df, target_variable, time):
    chart_data = pd.concat([
        df['group'],
        df[target_variable],
        df['time'],
    ], axis=1)
    chart_data = chart_data.query(f"""(`time` == "Time 1") or (`time` == '{time}')""")
    chart_data = chart_data.sort_values(['time', 'group'])
    chart_data_mean = chart_data.groupby(['time', 'group'], dropna=True)[[target_variable]].mean()
    chart_data_mean.variables_to_export = [f'{target_variable}||mean']
    chart_data = chart_data_mean.reset_index()
    chart_data = chart_data.dropna()

    fig = px.bar(
        chart_data,
        x='group',
        y=f'{target_variable}||mean',
        color='time',
        barmode='group',
    )

    fig.show()
    return fig


def continuous_descriptive_plots(df, target_variables, path):
    for target_variable in target_variables['continuous_target_vars']:
        figure = px.histogram(df, x=target_variable, color=df['time'], title=f"Distplot of {target_variable} by time", nbins=30)
        figure.write_html(os.path.join(f"plots/{path}", f"{target_variable} by time.html"))
        figure.show()


def discrete_descriptive_plots(df, target_variables):
    for target_variable in target_variables['discrete_target_vars']:
        figure = px.histogram(df, x=target_variable, color=df['time'], barmode='group',
                              title=f"count of {target_variable} by time")
        figure.write_html(os.path.join("plots", f"{target_variable} by time.html"))
        figure.show()


# ---------------------------------------------------------------


def perform_continuous_tests(df, target_variables, path):
    for time in ['Time 2', 'Time 3']:
        for target in target_variables['continuous_target_vars']:
            figure = plot_histogram(df, target, time)
            figure.write_html(os.path.join(f"plots/{path}", f"{time}_{target}.html"))
            anova_test(df, target, time)


def perform_discrete_tests(df, target_variables):
    for time in ['Time 2', 'Time 3']:
        for target_variable in target_variables['discrete_target_vars']:
            figure = discrete_treatment_improvement_plot(df, target_variable, time)
            figure.write_html(os.path.join("plots", f"{time}_{target_variable}.html"))
            logistic_regression_test(df, target_variable, time)
