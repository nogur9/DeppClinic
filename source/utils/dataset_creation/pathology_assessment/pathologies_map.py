from source.utils.dataset_creation.pathology_assessment.pathology_variable import PathologyVariable
from source.utils.dataset_creation.pathology_assessment.predefined_pathologies import suicidal_behavior_intake, suicide_attempt_intake, nssi_intake, \
    self_harm_intake, modcon_target, survival_target, suicidal_behavior_time2, nssi_time2, suicidal_attempt_time2

PathologiesMap = {
    "suicidal_behavior_intake": PathologyVariable('suicidal_behavior', suicidal_behavior_intake,
                                            only_intake_evaluation=True),
    "suicide_attempt_intake": PathologyVariable('suicide_attempt', suicide_attempt_intake,
                                            only_intake_evaluation=True),
    "NSSI_intake": PathologyVariable('NSSI', nssi_intake,
                                            only_intake_evaluation=True),
    "self_harm_intake": PathologyVariable('self_harm', self_harm_intake,
                                            only_intake_evaluation=True),

    "MODCON": PathologyVariable('MODCON', modcon_target,
                                            only_follow_up_evaluation=True),
    "survival_analysis": PathologyVariable('survival_analysis', survival_target,
                                            only_follow_up_evaluation=True),
    "suicidal_behavior_follow-up": PathologyVariable('suicidal_behavior', suicidal_behavior_time2,
                                            only_follow_up_evaluation=True),
    "suicidal_attempt_follow-up": PathologyVariable('suicide_attempt', suicidal_attempt_time2,
                                            only_follow_up_evaluation=True),
    "NSSI_follow-up": PathologyVariable('NSSI', nssi_time2,
                                            only_follow_up_evaluation=True),
}
