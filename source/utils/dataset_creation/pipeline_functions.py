import pandas as pd


def compute_questions_scores(df, questionnaires_map, export_columns_manager):
    for questionnaire in questionnaires_map.keys():
        try:
            df, scores_columns_names = questionnaires_map[questionnaire]['scoring_function'](df)
            export_columns_manager.add_columns(scores_columns_names)
        except KeyError:
            pass

    return df, export_columns_manager

