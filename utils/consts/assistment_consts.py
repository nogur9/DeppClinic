from utils.consts.questions_columns import demographics_m, sci_mother, scs_clin, c_ssrs_clin, c_ssrs_intake, c_ssrs, \
    mfq, siq, sdq, scared, ATHENS, SAS, sci_af_ca
from utils.consts.questions_text import intake_c_ssrs_text, c_ssrs_text, mfq_text, siq_text, sdq_text, scared_text, \
    ATHENS_text, SAS_text, sci_af_ca_text, sci_mother_text
from utils.questionnaires_scores.questionnaires_aggregation import compute_c_ssrs_score, compute_sas_score, \
    compute_all_intake_c_ssrs_scores, compute_all_c_ssrs_scores, compute_mfq_score, compute_siq_score, \
    compute_sdq_score, compute_scared_score, compute_athens_score, compute_sci_af_ac_score, \
    compute_all_clin_c_ssrs_scores

imputation_questionnaires = {
    'stu_2_clin': [scs_clin, c_ssrs_clin],
    'father_2_mother': [demographics_m, sci_mother]
}

questionnaires = {

    "c_ssrs_intake": {
      "columns": c_ssrs_intake,
      "scoring_function": compute_all_intake_c_ssrs_scores,
      "group": "C_SSRS",
      "text": intake_c_ssrs_text

    },

    "c_ssrs": {
      "columns": c_ssrs,
      "scoring_function": compute_all_c_ssrs_scores,
      "group": "C_SSRS",
      "text": c_ssrs_text

    },

    "c_ssrs_clin": {
      "columns": c_ssrs,
      "scoring_function": compute_all_c_ssrs_scores,
      "group": "C_SSRS",
      "text": c_ssrs_text

    },

    "mfq": {
      "columns": mfq,
      "scoring_function": compute_mfq_score,
      "group": "MFQ",
      "text": mfq_text

    },

    "siq": {
      "columns": siq,
      "scoring_function": compute_siq_score,
      "group": "SIQ",
      "text": siq_text

    },

    "sdq": {
      "columns": sdq,
      "scoring_function": compute_sdq_score,
      "group": "SDQ",
      "text": sdq_text

    },

    "scared": {
      "columns": scared,
      "scoring_function": compute_scared_score,
      "group": "SCARED",
      "text": scared_text

    },
    "ATHENS":{
      "columns": ATHENS,
      "scoring_function": compute_athens_score,
      "group": "ATHENS",
      "text": ATHENS_text

    },

    "SAS": {
      "columns": SAS,
      "scoring_function": compute_sas_score,
      "group": "SAS",
      "text": SAS_text

    },

    "sci_af_ca": {
      "columns": sci_af_ca,
      "scoring_function": compute_sci_af_ac_score,
      "group": "SCS",
      "text": sci_af_ca_text

    },

    "scs_clin": {
      #"columns": scs_clin,
      "scoring_function": compute_all_clin_c_ssrs_scores,
      "group": "SCS",
      #"text": scs_clin_text

    },
    "sci_mother": {
      "columns": sci_mother,
      #"scoring_function":
      "group": "SCS",
      "text": sci_mother_text

    },

}