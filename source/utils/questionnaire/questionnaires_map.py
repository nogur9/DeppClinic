from source.utils.questionnaire.individual_questionnaires import *


class QuestionnairesMap:
    def __init__(self, questionnaires_to_include=None):
        self.questionnaires_to_include: list = questionnaires_to_include
        self.all_of_the_questionnaires: dict = None
        self.questionnaires: dict = None
        self._init_questionnaires()

    def _init_questionnaires(self):
        self._load_all_of_the_questionnaires()

        # apply subset of the questionnaires
        if self.questionnaires_to_include is not None:
            self.questionnaires = {i: self.all_of_the_questionnaires[i] for i in self.questionnaires_to_include}
        else:
            self.questionnaires = self.all_of_the_questionnaires

    def _load_all_of_the_questionnaires(self):
        self.all_of_the_questionnaires = {
            "sdq": SDQScorer(),
            "mfq": MFQScorer(),
            "siq": SIQScorer(),
            "piu": PIUScorer(),
            "erq-ca": ErqCaScorer(),
            "cts": CTSScorer(),
            "dshi-pre": DshiPreScorer(),
            "dshi-post": DshiPostScorer(),
            "inq": INQScorer(),
            "mast": MASTScorer(),
            "ders": DERSScorer(),
            "athens": AthensScorer(),
            'ari-s': AriSScorer(),
            'erc-rc': ErcRcScorer(),
            'sas': SasScorer(),
            'scared': ScaredScorer(),
            'sci_af_ca': Sci_af_ca_Scorer(),
            "maris_sci_sf": Maris_sci_sf_Scorer(),
            "c_ssrs_intake": C_ssrs_intake_Scorer(),

            # Add other questionnaires similarly...
        }

    def get_questionnaire(self, name):
        return self.questionnaires.get(name)

    def get_columns(self, questionnaires=None):
        columns = []
        if questionnaires is None:
            questionnaires = list(self.questionnaires.keys())
        for questionnaire in questionnaires:
            questionnaire_columns = self.get_questionnaire(questionnaire).columns
            columns.extend(questionnaire_columns)
        return columns
