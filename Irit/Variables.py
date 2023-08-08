import numpy as np
rename_align = {'gender': 'sex',
                'age_child_pre': 'age',
                'parent_religion_m': 'religion',

                "swan_1_m": 't1_p_swan_1',
                "swan_2_m": 't1_p_swan_2',
                "swan_3_m": 't1_p_swan_3',
                "swan_4_m": 't1_p_swan_4',
                "swan_5_m": 't1_p_swan_5',
                "swan_6_m": 't1_p_swan_6',
                "swan_7_m": 't1_p_swan_7',
                "swan_8_m": 't1_p_swan_8',
                "swan_9_m": 't1_p_swan_9',
                "swan_10_m": 't1_p_swan_10',
                "swan_11_m": 't1_p_swan_11',
                "swan_12_m": 't1_p_swan_12',
                "swan_13_m": 't1_p_swan_13',
                "swan_14_m": 't1_p_swan_14',
                "swan_15_m": 't1_p_swan_15',
                "swan_16_m": 't1_p_swan_16',
                "swan_17_m": 't1_p_swan_17',
                "swan_18_m": 't1_p_swan_18',

                "swan_attention": 't1_p_swan_sum1-9',
                "swan_impulsivity": 't1_p_swan_sum10-18'
}

info_columns = ['gender', 'age_child_pre']

swan_m = ["swan_1_m", "swan_2_m", "swan_3_m", "swan_4_m", "swan_5_m", "swan_6_m", "swan_7_m",
          "swan_8_m", "swan_9_m", "swan_10_m", "swan_11_m", "swan_12_m", "swan_13_m",
          "swan_14_m", "swan_15_m", "swan_16_m", "swan_17_m", "swan_18_m"]

MFQ_threshold = 12

idx_CBCL_anx = [14, 29, 30, 31, 32, 33, 35, 45, 50, 52, 71, 91, 112]
CBCL_anx = [f"t1_p_rawscore_cbcl_{i}" for i in idx_CBCL_anx]


idx_CBCL_with = [5, 42, 65, 69, 75, 102, 103, 111]
CBCL_with = [f"t1_p_rawscore_cbcl_{i}" for i in idx_CBCL_with]


swan_factors_ = {
    'swan_attention': [f'swan_{i}_m' for i in range(1, 10)],
    'swan_impulsivity': [f'swan_{i}_m' for i in range(10, 19)]

}


CBCL_factors_ = {
    'CBCL_Anxious/Depressed': CBCL_anx,
    'CBCL_Withdrawn/Depressed': CBCL_with
}

CBCL = CBCL_with + CBCL_anx


# Thresholds are based on the files in - DeppClinic\Irit\thresholds (12-18 changed to 11-18, for the purpose of
# creating overlapping ranges)
cbcl_thresholds = {"CBCL_Anxious/Depressed":

                       {"male":
                         {"6-11": {"Normal": 7, "Borderline": 10, "Abnormal": 26},
                         "11-18": {"Normal": 6, "Borderline": 9, "Abnormal": 26}},
                        "female":
                         {"6-11": {"Normal": 7, "Borderline": 10, "Abnormal": 26},
                         "11-18": {"Normal": 7, "Borderline": 10, "Abnormal": 26}}

                        },

                   "CBCL_Withdrawn/Depressed": {
                       "male":
                           {"6-11": {"Normal": 3, "Borderline": 5, "Abnormal": 16},
                            "11-18": {"Normal": 5, "Borderline": 7, "Abnormal": 16}},
                       "female":
                           {"6-11": {"Normal": 4, "Borderline": 6, "Abnormal": 16},
                            "11-18": {"Normal": 5, "Borderline": 7, "Abnormal": 16}}
                        }
                   }

# Thresholds are based on the file in - DeppClinic\Irit\thresholds
SDQ_thresholds = {
    'SDQ_Emo_sum': {"Normal": 2, "Borderline": 3, "Abnormal": 10},
    'SDQ_Conduct_sum': {"Normal": 2, "Borderline": 3, "Abnormal": 10},
    'SDQ_Hyper_sum': {"Normal": 3, "Borderline": 4, "Abnormal": 10},
    'SDQ_Peer_sum': {"Normal": 2, "Borderline": 3, "Abnormal": 10},

 # Factors does not appear in the table
 #   'SDQ_Externalizing_sum': {"Normal": 1, "Borderline": 2, "Abnormal": 3},
 #   'SDQ_Internalizing_sum': {"Normal": 1, "Borderline": 2, "Abnormal": 3},
    }

columns_need_t_score = ['SDQ_Emo_sum', 'SDQ_Conduct_sum',
                'SDQ_Hyper_sum', 'SDQ_Peer_sum',
                'CBCL_Anxious/Depressed', 'CBCL_Withdrawn/Depressed',
                'CBCL_int_raw_score']

swan_columns_need_t_score = ['swan_sum', 'swan_score', 'swan_attention_sum', 'swan_impulsivity_sum']


