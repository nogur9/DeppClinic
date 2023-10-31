# 1-2 binary variables
binary_variables_need_adjustment = [
'mfq_34', 'mfq_35', 'mfq_36', 'mfq_37']

Max = 100

binary = [0, 1]

positive = range(0, Max)


variables_type = {
    'c_ssrs_1': binary,
    'c_ssrs_2': binary,
    'c_ssrs_3': binary,
    'c_ssrs_4': binary,
    'c_ssrs_5': binary,
    'c_ssrs_6': binary,
    'c_ssrs_last_visit_6': binary,
    'c_ssrs_7': positive,
    'c_ssrs_8': positive,
    
    
    
    'c_ssrs_1_life': binary,
    'c_ssrs_2_life': binary,
    'c_ssrs_3_life': binary,
    'c_ssrs_4_life': binary,
    'c_ssrs_5_life': binary,
    'c_ssrs_6_life': binary,
    'c_ssrs_1_2weeks': binary,
    'c_ssrs_2_2weeks': binary,
    'c_ssrs_3_2weeks': binary,
    'c_ssrs_4_2weeks': binary,
    'c_ssrs_5_2weeks': binary,
    'c_ssrs_6_2weeks': binary,
    'c_ssrs_6_3month': binary,
    'c_ssrs_7_intake': positive,
    'c_ssrs_8_intake': positive,
}


mfq = {
     'mfq_1': range(0, 3),
     'mfq_2': range(0, 3),
     'mfq_5': range(0, 3),
     'mfq_7': range(0, 3),
     'mfq_8': range(0, 3),
     'mfq_14': range(0, 3),
     'mfq_21': range(0, 3),
     'mfq_23': range(0, 3),
     'mfq_24': range(0, 3),
     'mfq_27': range(0, 3),
     'mfq_28': range(0, 3),
     'mfq_30': range(0, 3),
     'mfq_31': range(0, 3),
     'mfq_34': binary,
     'mfq_35': binary,
     'mfq_36': binary,
     'mfq_37': binary
    }


siq = {
'siq_1': range(0, 7),
 'siq_2': range(0, 7),
 'siq_3': range(0, 7),
 'siq_4': range(0, 7),
 'siq_5': range(0, 7),
 'siq_6': range(0, 7),
 'siq_7': range(0, 7),
 'siq_8': range(0, 7),
 'siq_9': range(0, 7),
 'siq_10': range(0, 7),
 'siq_11': range(0, 7),
 'siq_12': range(0, 7),
 'siq_13': range(0, 7),
 'siq_14': range(0, 7),
 'siq_15': range(0, 7)
 }


sdq = {
 'sdq_1': range(0, 3),
 'sdq_2': range(0, 3),
 'sdq_3': range(0, 3),
 'sdq_4': range(0, 3),
 'sdq_5': range(0, 3),
 'sdq_6': range(0, 3),
 'sdq_7': range(0, 3),
 'sdq_8': range(0, 3),
 'sdq_9': range(0, 3),
 'sdq_10': range(0, 3),
 'sdq_11': range(0, 3),
 'sdq_12': range(0, 3),
 'sdq_13': range(0, 3),
 'sdq_14': range(0, 3),
 'sdq_15': range(0, 3),
 'sdq_16': range(0, 3),
 'sdq_17': range(0, 3),
 'sdq_18': range(0, 3),
 'sdq_19': range(0, 3),
 'sdq_20': range(0, 3),
 'sdq_21': range(0, 3),
 'sdq_22': range(0, 3),
 'sdq_23': range(0, 3),
 'sdq_24': range(0, 3),
 'sdq_25': range(0, 3)
}


scared = {
'scared_1':range(0, 3),
'scared_2':range(0, 3),
'scared_3':range(0, 3),
'scared_4':range(0, 3),
'scared_5':range(0, 3),
'scared_6': range(0, 3),
'scared_7': range(0, 3),
'scared_8': range(0, 3),
'scared_9': range(0, 3),
'scared_10': range(0, 3),
'scared_11': range(0, 3),
'scared_12': range(0, 3),
'scared_13': range(0, 3),
'scared_14': range(0, 3),
'scared_15': range(0, 3),
'scared_16': range(0, 3),
'scared_17': range(0, 3),
'scared_18': range(0, 3),
'scared_19': range(0, 3),
'scared_20': range(0, 3),
'scared_21': range(0, 3),
'scared_22': range(0, 3),
'scared_23': range(0, 3),
'scared_24': range(0, 3),
'scared_25': range(0, 3),
'scared_26': range(0, 3),
'scared_27': range(0, 3),
'scared_28': range(0, 3),
'scared_29': range(0, 3),
'scared_30': range(0, 3),
'scared_31': range(0, 3),
'scared_32': range(0, 3),
'scared_33': range(0, 3),
'scared_34': range(0, 3),
'scared_35': range(0, 3),
'scared_36': range(0, 3),
'scared_37': range(0, 3),
'scared_38': range(0, 3),
'scared_39': range(0, 3),
'scared_40': range(0, 3),
'scared_41': range(0, 3),
}



ATHENS = {
'athens_1': range(0, 4),
'athens_2': range(0, 4),
'athens_3': range(0, 4),
'athens_4': range(0, 4),
'athens_5': range(0, 4),
'athens_6': range(0, 4),
'athens_7': range(0, 4),
'athens_8': range(0, 4)
}

SAS = {
'sas_1': range(1, 7),
'sas_2': range(1, 7),
'sas_3': range(1, 7),
'sas_4': range(1, 7),
'sas_5': range(1, 7),
'sas_6': range(1, 7),
'sas_7': range(1, 7),
'sas_8': range(1, 7),
'sas_9': range(1, 7),
'sas_10': range(1, 7),
'sas_11': range(1, 7),
'sas_12': range(1, 7),
'sas_13': range(1, 7),
'sas_14': range(1, 7),
'sas_15': range(1, 7),
'sas_16': range(1, 7),
'sas_17': range(1, 7),
'sas_18': range(1, 7),
'sas_19': range(1, 7),
'sas_20': range(1, 7),
'sas_21': range(1, 7),
'sas_22': range(1, 7),
'sas_23': range(1, 7)
}


sci_af_ca= {
'sci_af_ca_1': range(0, 5),
'sci_af_ca_2': range(0, 5),
'sci_af_ca_3': range(0, 5),
'sci_af_ca_4': range(0, 5),
'sci_af_ca_5': range(0, 5),
'sci_af_ca_6': range(0, 5),
'sci_af_ca_7': range(0, 5),
'sci_af_ca_8': range(0, 5),
'sci_af_ca_9': range(0, 5),
'sci_af_ca_10': range(0, 5),
'sci_af_ca_11': range(0, 5),
'sci_af_ca_12': range(0, 5),
'sci_af_ca_13': range(0, 5),
'sci_af_ca_14': range(0, 5),
'sci_af_ca_15': range(0, 5),
'sci_af_ca_16': range(0, 5),
'sci_af_ca_17': range(0, 5),
'sci_af_ca_18': range(0, 5),
'sci_af_ca_19': range(0, 5),
'sci_af_ca_20': range(0, 5),
'sci_af_ca_21': range(0, 5),
'sci_af_ca_22': range(0, 5),
'sci_af_ca_23': range(0, 5),
'sci_af_ca_24': range(0, 5),
'sci_af_ca_25': range(0, 5),
'sci_af_ca_26': range(0, 5),
'sci_af_ca_27': range(0, 5),
'sci_af_ca_28': range(0, 5),
'sci_af_ca_29': range(0, 5),
'sci_af_ca_30': range(0, 5),
'sci_af_ca_31': range(0, 5),
'sci_af_ca_32': range(0, 5),
'sci_af_ca_33': range(0, 5),
'sci_af_ca_34': range(0, 5),
'sci_af_ca_35': range(0, 5),
'sci_af_ca_36': range(0, 5),
'sci_af_ca_37': range(0, 5),
'sci_af_ca_38': range(0, 5),
'sci_af_ca_39': range(0, 5),
'sci_af_ca_40': range(0, 5)
}




scs_clin = [
    'sci_c_1_1_clin',
    'scs_2_1_clin',
    'scs_2_2_clin',
    'scs_2_3_clin',
    'scs_2_4_clin',
    'sci_c_3_1_clin',
    'sci_c_3_2_clin',
    'sci_c_3_3_clin',
    'sci_c_3_4_clin',
    'sci_c_4_1_clin',
    'sci_c_4_2_clin',
    'sci_c_4_3_clin',
    'sci_c_4_4_clin',
    'sci_c_5_1_clin',
    'sci_c_5_2_clin'
]


scs_stu = [
    'sci_c_1_1_stu',
    'scs_2_1_stu',
    'scs_2_2_stu',
    'scs_2_3_stu',
    'scs_2_4_stu',
    'sci_c_3_1_stu',
    'sci_c_3_2_stu',
    'sci_c_3_3_stu',
    'sci_c_3_4_stu',
    'sci_c_4_1_stu',
    'sci_c_4_2_stu',
    'sci_c_4_3_stu',
    'sci_c_4_4_stu',
    'sci_c_5_1_stu',
    'sci_c_5_2_stu'
]

sci_mother = [
    'sci_p_1_m',
    'sci_p_2_m',
    'sci_p_3_m',
    'sci_p_4_m',
    'sci_p_5_m',
    'sci_p_6_m',
    'sci_p_7_m',
    'sci_p_8_m',
    'sci_p_9_m',
    'sci_p_10_m',
    'sci_p_11_m',
    'sci_p_12_m',
    'sci_p_13_m',
    'sci_p_14_m',
    'sci_p_15_m'
]

sci_father = [
    'sci_p_1_f',
    'sci_p_2_f',
    'sci_p_3_f',
    'sci_p_4_f',
    'sci_p_5_f',
    'sci_p_6_f',
    'sci_p_7_f',
    'sci_p_8_f',
    'sci_p_9_f',
    'sci_p_10_f',
    'sci_p_11_f',
    'sci_p_12_f',
    'sci_p_13_f',
    'sci_p_14_f',
    'sci_p_15_f'
]