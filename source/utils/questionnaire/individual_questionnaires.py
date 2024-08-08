from source.utils.questionnaire.questionnaire_scorer import QuestionnaireScorer
from source.utils.consts.subsets_of_questionnaires import *
from source.utils.consts.questions_columns import *


class SDQScorer(QuestionnaireScorer):
    def __init__(self, sdq_columns=sdq, sdq_reverse_columns=sdq_reverse, sdq_factors=SDQ_factors):
        super().__init__('sdq', sdq_columns, sdq_reverse_columns, sdq_factors, max_score=2)

    def _calculate_aggregated_score(self, df, columns):
        return df[columns].sum(axis=1, skipna=True)


class MFQScorer(QuestionnaireScorer):
    def __init__(self, mfq_columns=mfq):
        super().__init__('mfq', mfq_columns)

    def _calculate_aggregated_score(self, df, columns):
        return df[columns].sum(axis=1, skipna=True)


class SIQScorer(QuestionnaireScorer):
    def __init__(self, siq_columns=siq):
        super().__init__('siq', siq_columns)

    def _calculate_aggregated_score(self, df, columns):
        return df[columns].sum(axis=1)

