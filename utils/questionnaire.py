
class Questionnaire:

    def __init__(self, name, scoring_function, questions, questions_text={}, subscales={}):
        self.name = name
        self.scoring_function = scoring_function
        self.scores_columns = []
        self.questions = questions
        self.questions_text = questions_text
        self.subscales = subscales
        self.subscales_scores = {}

    def subscales_exists(self):
        return bool(self.subscales)

    def score_questionnaire(self, df):

        if self.subscales_exists():
            df, self.scores_columns, self.subscales_scores = self.scoring_function(df)
        else:
            df, self.scores_columns = self.scoring_function(df)

        return df
