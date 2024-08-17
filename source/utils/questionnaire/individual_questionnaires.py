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


class PIUScorer(QuestionnaireScorer):
    def __init__(self, piu_columns=piu_cyberbulling):
        super().__init__('piu_cyberbulling', piu_columns)


class ErqCaScorer(QuestionnaireScorer):
    def __init__(self, erq_ca_columns=erq_ca):
        super().__init__('erq-ca', erq_ca_columns)


class CTSScorer(QuestionnaireScorer):
    def __init__(self, cts_columns=cts):
        super().__init__('cts', cts_columns)


class DshiPreScorer(QuestionnaireScorer):
    def __init__(self, dshi_pre_columns=dshi_pre):
        super().__init__('dshi-pre', dshi_pre_columns)


class DshiPostScorer(QuestionnaireScorer):
    def __init__(self, dshi_post_columns=dshi_post):
        super().__init__('dshi_post', dshi_post_columns)


class INQScorer(QuestionnaireScorer):
    def __init__(self, inq_columns=inq):
        super().__init__('inq', inq_columns)


class MASTScorer(QuestionnaireScorer):
    def __init__(self, mast_columns=MAST):
        super().__init__('MAST', mast_columns)


class DERSScorer(QuestionnaireScorer):
    def __init__(self, ders_columns=DERS):
        super().__init__('DERS', ders_columns)


class AthensScorer(QuestionnaireScorer):
    def __init__(self, athens_columns=ATHENS):
        super().__init__('Athens', athens_columns)


class AriSScorer(QuestionnaireScorer):
    def __init__(self, ari_s_columns=ARI_S):
        super().__init__('ari-s', ari_s_columns)


class ErcRcScorer(QuestionnaireScorer):
    def __init__(self, erc_rc_columns=erc_rc):
        super().__init__('erc-rc', erc_rc_columns)


class SasScorer(QuestionnaireScorer):
    def __init__(self, sas_columns=erc_rc):
        super().__init__('sas', sas_columns)


class ScaredScorer(QuestionnaireScorer):
    def __init__(self, scared_columns=scared):
        super().__init__('scared', scared_columns)


class Sci_af_ca_Scorer(QuestionnaireScorer):
    def __init__(self, sci_af_ca_columns=sci_af_ca):
        super().__init__('sci_af_ca', sci_af_ca_columns)


class Maris_sci_sf_Scorer(QuestionnaireScorer):
    def __init__(self, maris_sci_sf_columns=maris_sci_sf):
        super().__init__('maris_sci_sf', maris_sci_sf_columns)


class C_ssrs_intake_Scorer(QuestionnaireScorer):
    def __init__(self, c_ssrs_intake_columns=c_ssrs_intake):
        super().__init__('c_ssrs_intake', c_ssrs_intake_columns)

