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
    ['sdq_1',
 'sdq_2',
 'sdq_3',
 'sdq_4',
 'sdq_5',
 'sdq_6',
 'sdq_7',
 'sdq_8',
 'sdq_9',
 'sdq_10',
 'sdq_11',
 'sdq_12',
 'sdq_13',
 'sdq_14',
 'sdq_15',
 'sdq_16',
 'sdq_17',
 'sdq_18',
 'sdq_19',
 'sdq_20',
 'sdq_21',
 'sdq_22',
 'sdq_23',
 'sdq_24',
 'sdq_25'}