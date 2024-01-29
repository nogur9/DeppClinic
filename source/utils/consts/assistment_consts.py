from source.utils.consts.questions_columns import demographics_m, sci_mother, scs_clin, c_ssrs_clin, c_ssrs_intake, \
    c_ssrs, \
    mfq, siq, sdq, scared, ATHENS, SAS, sci_af_ca, demographics_f, sci_father, scs_stu, c_ssrs_stu, swan_f, swan_m, \
    DERS, wai, erc_rc, dass_m, dass_f

from source.utils.consts.questions_text import intake_c_ssrs_text, c_ssrs_text, mfq_text, siq_text, sdq_text, scared_text, \
    ATHENS_text, SAS_text, sci_af_ca_text, sci_mother_text, scs_clin_text
from source.utils.consts.subsets_of_questionnaires import swan_factors, DERS_reverse_items, DERS_factors, wai_factors, \
    wai_reversed_items, erc_rc_factors, erc_rc_reversed_items
from source.utils.questionnaires_scores.scores_computations import compute_ders_score, compute_wai_score, \
    compute_ecr_score


class Questionnaires:

    def __init__(self):
        from source.utils.questionnaires_scores.scores_computations import compute_sas_score, \
            calculate_c_ssrs_scores_intake, calculate_c_ssrs_scores, compute_mfq_score, compute_siq_score, \
            compute_sdq_score, compute_scared_score, compute_athens_score, compute_sci_af_ac_score, \
            calculate_c_ssrs_scores_clinician, compute_scs_clin_score, compute_scs_mother_score, compute_swan_scores
        self.questionnaires = {
            "demographics_m": {
                "columns": demographics_m,
                "group": "demographics",
            },
            "demographics_f": {
                "columns": demographics_f,
                "group": "demographics",
            },
            "c_ssrs_intake": {
                "columns": c_ssrs_intake,
                "scoring_function": calculate_c_ssrs_scores_intake,
                "group": "C_SSRS",
                "text": intake_c_ssrs_text

            },
            "c_ssrs": {
                "columns": c_ssrs,
                "scoring_function": calculate_c_ssrs_scores,
                "group": "C_SSRS",
                "text": c_ssrs_text

            },
            "c_ssrs_clin": {
                "columns": c_ssrs_clin,
                "scoring_function": calculate_c_ssrs_scores_clinician,
                "group": "C_SSRS",
                "text": c_ssrs_text

            },
            "c_ssrs_stu": {
                "columns": c_ssrs_stu,
                "group": "C_SSRS",
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
            "ATHENS": {
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
                "columns": scs_clin,
                "scoring_function": compute_scs_clin_score,
                "group": "SCS",
                "text": scs_clin_text

            },
            "scs_stu": {
                "columns": scs_stu,
                "group": "SCS",

            },
            "sci_mother": {
                "columns": sci_mother,
                "scoring_function": compute_scs_mother_score,
                "group": "SCS",
                "text": sci_mother_text

            },
            "sci_father": {
                "columns": sci_father,
                "group": "SCS"
            },
            "swan_father": {
                "columns": swan_f,
                "group": "swan"
            },
            "swan_mother": {
                "columns": swan_m,
                "scoring_function": compute_swan_scores,
                "group": "swan",
                "factors": swan_factors
            },
            "ders": {
                "columns": DERS,
                "scoring_function": compute_ders_score,
                "group": "DERS",
                "factors": DERS_factors,
                "reversed_items": DERS_reverse_items
            },
            "wai": {
                "columns": wai,
                "scoring_function": compute_wai_score,
                "group": "wai",
                "factors": wai_factors,
                "reversed_items": wai_reversed_items

            },
            "erc_rc": {
                "columns": erc_rc,
                "scoring_function": compute_ecr_score,
                "group": "erc_rc",
                "factors": erc_rc_factors,
                "reversed_items": erc_rc_reversed_items

            },
            "dass_m": {
                "columns": dass_m,
                "group": "dass",
            },
            "dass_f": {
                "columns": dass_f,
                "group": "dass",
            },
        }


imputation_questionnaires = [
    {'origin': 'scs_clin', 'replacement': 'scs_stu'},
    {'origin': 'c_ssrs_clin', 'replacement': 'c_ssrs_stu'},
    {'origin': 'demographics_m', 'replacement': 'demographics_f'},
    {'origin': 'sci_mother', 'replacement': 'sci_father'},
    {'origin': 'dass_m', 'replacement': 'dass_f'}
]