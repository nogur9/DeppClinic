from source.utils.consts.subsets_of_questionnaires import c_ssrs_life_values_map, c_ssrs_2weeks_values_map


def calculate_clinician_c_ssrs_individual_score(df, score_info, rolling_negative):
    if score_info['agg_method'] == 'max':
        if rolling_negative:
            df = c_ssrs_roll_negative(df, score_info['columns'])

        c_ssrs_values_map = {value: (idx + 1) for idx, value in enumerate(score_info['columns'])}
        score = get_max_index(df, c_ssrs_values_map)

    elif score_info['agg_method'] == 'no':
        score = df[score_info['columns']]
    else:
        raise ValueError

    return score


def calculate_intake_c_ssrs_individual_score(df, severity='stb', time='life'):
    if time == 'life':
        c_ssrs_values_map = c_ssrs_life_values_map

    elif time == '2weeks':
        c_ssrs_values_map = c_ssrs_2weeks_values_map

    elif time == 'recent':
        c_ssrs_values_map = c_ssrs_2weeks_values_map
        c_ssrs_values_map['c_ssrs_6_3month'] = 6
    else:
        raise ValueError

    if severity == 'idea':
        stb_questions = [i for i in c_ssrs_values_map.keys() if c_ssrs_values_map[i] > 5]
        for question in stb_questions:
            c_ssrs_values_map.pop(question)
    elif severity == 'stb':
        pass
    else:
        raise ValueError

    agg_score = get_max_index(df, c_ssrs_values_map)

    return agg_score


def c_ssrs_roll_negative(df, c_ssrs_columns):
    # Check if the first 2 items are 0 and the last 4 items are missing (NaN)

    c_ssrs_columns = list(c_ssrs_columns)
    negative_columns_condition = (df[c_ssrs_columns[0]] == 0) & (df[c_ssrs_columns[1]] == 0)
    redundant_columns_condition = df[c_ssrs_columns[2:]].isna().all(axis=1)
    redundant_columns = c_ssrs_columns[2:]

    mask = negative_columns_condition & redundant_columns_condition

    # Impute the last 4 items with 0 where the conditions are met
    df.loc[mask, redundant_columns] = 0

    return df


def calculate_c_ssrs_individual_score(df, severity):
    """
    Calculates the C-SSRS (Columbia-Suicide Severity Rating Scale) individual scores based on the severity level.

    The C-SSRS is a scale used to assess suicide risk and consists of questions with increasing severity of symptoms.
    This function calculates the individual scores by determining the maximal question index with a positive answer.

    Args:
        df (pandas.DataFrame): The input DataFrame containing the questionnaire answers.
        severity (str): The severity level to consider. Can be 'idea' or 'stb'.
            - If severity is 'idea', the function excludes questions with severity levels above 5.
            - If severity is 'stb', the function considers all questions.
            - If severity is neither 'idea' nor 'stb', a ValueError is raised.

    Returns:
        pandas.Series: A Series containing the individual scores calculated for each row in the DataFrame.

    Raises:
        ValueError: If severity is neither 'idea' nor 'stb'.


    """
    c_ssrs_values_map = {
        'c_ssrs_1': 1,
        'c_ssrs_2': 2,
        'c_ssrs_3': 3,
        'c_ssrs_4': 4,
        'c_ssrs_5': 5,
        'c_ssrs_6': 6,
        'c_ssrs_last_visit_6': 6
    }

    if severity == 'idea':
        stb_questions = [i for i in c_ssrs_values_map.keys() if c_ssrs_values_map[i] > 5]
        for question in stb_questions:
            c_ssrs_values_map.pop(question)
    elif severity == 'stb':
        pass
    else:
        raise ValueError

    agg_score = get_max_index(df, c_ssrs_values_map)

    return agg_score


def get_max_index(df, questions_values_map):
    """
    Returns the maximal index of the question with a positive answer.

    Args:
        df (pandas.DataFrame): The input DataFrame containing the questionnaire answers.
        questions_values_map (dict): A dictionary mapping question names to their respective values.

    Returns:
        pandas.Series: A Series containing the maximal index of the question with a positive answer for each row.

    """
    questions_values = df[questions_values_map.keys()] * questions_values_map.values()
    max_value = questions_values.max(axis=1)
    return max_value