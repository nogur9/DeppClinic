"""
sci_af_ac 5 factors

sdq - reverse questions
sdq - normal questions
"""
from utils.consts.questions_columns import sdq, maris_soq_sf

swan_factors = {
    'attention': [f'swan_{i}m' for i in range(1, 10)],
    'impulsivity': [f'swan_{i}m' for i in range(10, 19)]

}

sci_af_ac_factors = {
  'sci_af_ca_Factor1': ['sci_af_ca_5',
  'sci_af_ca_6',
  'sci_af_ca_13',
  'sci_af_ca_15',
  'sci_af_ca_16',
  'sci_af_ca_19',
  'sci_af_ca_20',
  'sci_af_ca_22',
  'sci_af_ca_24',
  'sci_af_ca_25'],

 'sci_af_ca_Factor2': ['sci_af_ca_1',
  'sci_af_ca_2',
  'sci_af_ca_3',
  'sci_af_ca_7',
  'sci_af_ca_8',
  'sci_af_ca_9',
  'sci_af_ca_10',
  'sci_af_ca_11',
  'sci_af_ca_14',
  'sci_af_ca_17',
  'sci_af_ca_26'],

 'sci_af_ca_Factor3': ['sci_af_ca_4',
  'sci_af_ca_12',
  'sci_af_ca_18',
  'sci_af_ca_21',
  'sci_af_ca_23',
  'sci_af_ca_27',
  'sci_af_ca_28'],

 'sci_af_ca_Factor4': ['sci_af_ca_29',
  'sci_af_ca_30',
  'sci_af_ca_31',
  'sci_af_ca_32',
  'sci_af_ca_33',
  'sci_af_ca_34',
  'sci_af_ca_40'],

 'sci_af_ca_Factor5': ['sci_af_ca_35',
  'sci_af_ca_36',
  'sci_af_ca_37',
  'sci_af_ca_38',
  'sci_af_ca_39']}
sci_af_ca_new_questions = [f'sci_af_ca_{i}' for i in range(26, 41)]
"""
SCS mother - factors

SCS clin - factors

"""

maris_soq_sf_reverse = ['maris_soq_sf_2', 'maris_soq_sf_3', 'maris_soq_sf_5']
maris_soq_sf_normal = [i for i in maris_soq_sf if i not in maris_soq_sf_reverse]

# SDQ

sdq_reverse = ['sdq_7', 'sdq_11', 'sdq_14', 'sdq_21', 'sdq_25']
sdq_normal = [i for i in sdq if i not in sdq_reverse]


conduct_columns = ['SDQ_5', 'SDQ_7R', 'SDQ_12', 'SDQ_18', 'SDQ_22']
emo_columns = ['SDQ_3', 'SDQ_8', 'SDQ_13', 'SDQ_16', 'SDQ_24']
hyper_columns = ['SDQ_2', 'SDQ_10', 'SDQ_15', 'SDQ_21', 'SDQ_25']
peer_columns = ['SDQ_6', 'SDQ_11', 'SDQ_14', 'SDQ_19', 'SDQ_23']

# Recode values in SDQ_Hyper using the recoding criteria
recode_dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 2, 8: 2, 9: 2, 10: 2}
df['SDQ_Hyper_CAT'] = df['SDQ_Hyper'].map(recode_dict)

SDQ_factors = {
    'conduct': conduct_columns,
    'emo': emo_columns,
    'hyper': hyper_columns,
    'peer': peer_columns,
    'Externalizing': conduct_columns + hyper_columns,
    'Internalizing': emo_columns + peer_columns,


}

sdq_columns = ['SDQ_2', 'SDQ_3', 'SDQ_5', 'SDQ_6', 'SDQ_7', 'SDQ_8', 'SDQ_10', 'SDQ_11',
               'SDQ_12', 'SDQ_13', 'SDQ_14', 'SDQ_15', 'SDQ_16', 'SDQ_18', 'SDQ_19',
               'SDQ_21', 'SDQ_22', 'SDQ_23', 'SDQ_24', 'SDQ_25']


MAST_factors = {
    'MAST_AL': ['MAST_1', 'MAST_5', 'MAST_6', 'MAST_13', 'MAST_18', 'MAST_19', 'MAST_25', 'MAST_28'],
    'MAST_RL': ['MAST_2', 'MAST_9', 'MAST_14', 'MAST_15', 'MAST_16', 'MAST_21', 'MAST_30'],
    'MAST_AD': ['MAST_8', 'MAST_17', 'MAST_22', 'MAST_23', 'MAST_26', 'MAST_27', 'MAST_29'],
    'MAST_RD': ['MAST_3', 'MAST_4', 'MAST_7', 'MAST_10', 'MAST_11', 'MAST_12', 'MAST_20', 'MAST_24']
}


# C_ssrs intake

c_ssrs_life_values_map = {
    'c_ssrs_1_life': 1,
    'c_ssrs_2_life': 2,
    'c_ssrs_3_life': 3,
    'c_ssrs_4_life': 4,
    'c_ssrs_5_life': 5,
    'c_ssrs_6_life': 6}

c_ssrs_2weeks_values_map = {
    'c_ssrs_1_2weeks': 1,
    'c_ssrs_2_2weeks': 2,
    'c_ssrs_3_2weeks': 3,
    'c_ssrs_4_2weeks': 4,
    'c_ssrs_5_2weeks': 5,
    'c_ssrs_6_2weeks': 6}


# C_ssrs clinician

C_ssrs_clinician = {
    'c_ssrs_clinician_2weeks': {
        'name': 'c_ssrs_clinician_2weeks',
        'agg_method': 'max',
        'columns': {
            'c_ssrs_t_2weeks_1_clin': 1,
            'c_ssrs_t_2weeks_2_clin': 2,
            'c_ssrs_t_2weeks_3_clin': 3,
            'c_ssrs_t_2weeks_4_clin': 4,
            'c_ssrs_t_2weeks_5_clin': 5,
        },
        'group': 'ideation',
        'time': '2 weeks'
    },
    'c_ssrs_clinician_last': {
        'name': 'c_ssrs_clinician_last',
        'agg_method': 'max',
        'columns': {
            'c_ssrs_t_last_1_clin': 1,
            'c_ssrs_t_last_2_clin': 2,
            'c_ssrs_t_last_3_clin': 3,
            'c_ssrs_t_last_4_clin': 4,
            'c_ssrs_t_last_5_clin': 5,
        },
        'group': 'ideation',
        'time': 'last'

    },
    'c_ssrs_clinicinan_life': {
        'name': 'c_ssrs_clinicinan_life',
        'agg_method': 'max',
        'columns': {
            'c_ssrs_t_life_1_clin': 1,
            'c_ssrs_t_life_2_clin': 2,
            'c_ssrs_t_life_3_clin': 3,
            'c_ssrs_t_life_4_clin': 4,
            'c_ssrs_t_life_5_clin': 5,
        },
        'group': 'ideation',
        'time': 'last'
    },

    'c_ssrs_t_6_clin': {
        'name': 'c_ssrs_t_6_clin',
        'agg_method': 'no',
        'columns': ['c_ssrs_t_6_clin'],
        'group': '?',
        'time': '?'
    },
        'c_ssrs_t_7_clin':{
        'name': 'c_ssrs_t_7_clin',
        'agg_method': 'no',
        'columns': ['c_ssrs_t_7_clin'],
        'group': '?',
        'time': '?'
    },
    'c_ssrs_t_8_clin':{
            'name': 'c_ssrs_t_8_clin',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_8_clin'],
            'group': '?',
            'time': '?'
    },
    'c_ssrs_t_9_clin':{
            'name': 'c_ssrs_t_9_clin',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_9_clin'],
            'group': '?',
            'time': '?'
    },
    'c_ssrs_t_10_clin':{
            'name': 'c_ssrs_t_10_clin',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_10_clin'],
            'group': '?',
            'time': '?'
    },
    'c_ssrs_t_6_clin_2':{
            'name': 'c_ssrs_t_6_clin_2',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_6_clin_2'],
            'group': '?',
            'time': '2 weeks'

    },
    'c_ssrs_t_7_clin_2':{
            'name': 'c_ssrs_t_7_clin_2',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_7_clin_2'],
            'group': '?',
            'time': '2 weeks'
    },
    'c_ssrs_t_8_clin_2':{
            'name': 'c_ssrs_t_8_clin_2',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_8_clin_2'],
            'group': '?',
            'time': '2 weeks'

    },
    'c_ssrs_t_9_clin_2':{
            'name': 'c_ssrs_t_9_clin_2',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_9_clin_2'],
            'group': '?',
            'time': '2 weeks'
    },
    'c_ssrs_t_10_clin_2':{
            'name': 'c_ssrs_t_10_clin_2',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_10_clin_2'],
            'group': '?',
            'time': '2 weeks'
    },
    'c_ssrs_t_11_2weeks_clin':{
            'name': 'c_ssrs_t_11_2weeks_clin',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_11_2weeks_clin'],
            'group': 'suicidal_behavior',
            'time': '2 weeks'
    },
    'c_ssrs_t_12_2weeks_clin': {
            'name': 'c_ssrs_t_12_2weeks_clin',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_12_2weeks_clin'],
            'group': 'suicidal_behavior',
            'time': '2 weeks'
    },
    'c_ssrs_t_13_2weeks_clin': {
            'name': 'c_ssrs_t_13_2weeks_clin',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_13_2weeks_clin'],
            'group': 'suicidal_behavior',
            'time': '2 weeks'
    },
    'c_ssrs_t_14_2weeks_clin': {
            'name': 'c_ssrs_t_14_2weeks_clin',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_14_2weeks_clin'],
            'group': 'suicidal_behavior',
            'time': '2 weeks'
    },
    'c_ssrs_t_15_2weeks_clin':{
            'name': 'c_ssrs_t_15_2weeks_clin',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_15_2weeks_clin'],
            'group': 'suicidal_behavior',
            'time': '2 weeks'
    },
    'c_ssrs_t_16_2weeks_clin':{
            'name': 'c_ssrs_t_16_2weeks_clin',
            'agg_method': 'no',
            'columns': ['c_ssrs_t_16_2weeks_clin'],
            'group': 'NSSI',
            'time': '2 weeks'
    },

    'suicidal_behavior_last_11_clin': {
            'name': 'suicidal_behavior_last_11_clin',
            'agg_method': 'no',
            'columns': ['suicidal_behavior_last_11_clin'],
            'group': 'suicidal_behavior',
            'time': 'last'
        },
    'suicidal_behavior_last_12_clin': {
            'name': 'suicidal_behavior_last_12_clin',
            'agg_method': 'no',
            'columns': ['suicidal_behavior_last_12_clin'],
            'group': 'suicidal_behavior',
            'time': 'last'
        },
    'suicidal_behavior_last_13_clin':{
            'name': 'suicidal_behavior_last_13_clin',
            'agg_method': 'no',
            'columns': ['suicidal_behavior_last_13_clin'],
            'group': 'suicidal_behavior',
            'time': 'last'
        },
    'suicidal_behavior_last_14_clin': {
            'name': 'suicidal_behavior_last_14_clin',
            'agg_method': 'no',
            'columns': ['suicidal_behavior_last_14_clin'],
            'group': 'suicidal_behavior',
            'time': 'last'
        },
    'suicidal_behavior_last_15_clin': {
            'name': 'suicidal_behavior_last_15_clin',
            'agg_method': 'no',
            'columns': ['suicidal_behavior_last_15_clin'],
            'group': 'suicidal_behavior',
            'time': 'last'
        },
    'suicidal_behavior_last_16_clin': {
            'name': 'suicidal_behavior_last_16_clin',
            'agg_method': 'no',
            'columns': ['suicidal_behavior_last_16_clin'],
            'group': 'NSSI',
            'time': 'last'
        },

    'suicidal_behavior_last_17_clin': {
            'name': 'suicidal_behavior_last_17_clin',
            'agg_method': 'no',
            'columns': ['suicidal_behavior_last_17_clin'],
            'group': 'suicidal_behavior',
            'time': 'last'
        },
}




# C_ssrs maya
"""
c_ssrs_fu_thought_1_clin	Numeric	הנבדק/ת מאשר/ת קיום מחשבות על הרצון למות או לא להיות יותר בין החיים או על המשאלה להירדם ולא להתעורר עוד	{0, לא}...
c_ssrs_fu_thought_2_clin	Numeric	מחשבות כלליות בלתי ספציפיות על הרצון לסיים את החיים / להתאבד, כגון חשבתי להתאבד, ללא מחשבות של צורת ההתאבדות / שיטות קשורות, כוונה או תכנית בתק	{0, לא}...
c_ssrs_fu_thought_3_clin	Numeric	הנבדק/ת מאשר/ת קיום מחשבות על התאבדות וחשב/ה על שיטה אחת לפחות במהלך תקופת ההערכה. דבר זה שונה מתכנית מוגדרת הכוללת פרטים מעובדים של מקום, זמן	{0, לא}...
c_ssrs_fu_thought_4_clin	Numeric	מחשבות פעילות על התאבדות, וכן הנבדק/ת מדווח/ת על כוונה מסוימת לפעול על פי מחשבות אלה, בניגוד ל- יש לי מחשבות כאלה, אך בפירוש לא אעשה כלום על פיה�	{0, לא}...
c_ssrs_fu_thought_5_clin	Numeric	מחשבות התאבדות עם פרטי תכנית מעובדים באופן מלא או חלקי. לנבדק/ת כוונה מסוימת להוציא אותה אל הפועל.	{0, לא}...
c_ssrs_fu_intensity_clin	Numeric	סוג המחשבות האובדניות מ-1 עד 5 המחשבות האובדניות החמורות ביותר הן	None
c_ssrs_fu_frequ_clin	Numeric	כמה פעמים הגיעו מחשבות אלה?	{1, פחות מפעם בשבוע}...
c_ssrs_fu_lengh_clin	Numeric	כשיש לך מחשבות אלה, כמה זמן הן נמשכות?	{1, חולפות - מספר שניות או דקות}...
c_ssrs_fu_control_clin	Numeric	האם יכולת / את/ה יכול/ה להפסיק לחשוב על התאבדות או על המשאלה למות אם את/ה רוצה בכך?	{0, אינו/ה מנסה לשלוט במחשבות}...
c_ssrs_fu_deter_clin	Numeric	האם קיימים דברים או אנשים כלשהם (כגון משפחה, דת, כאב הקשור במוות), אשר מנעו ממך לרצות להתאבד או לפעול על פי המחשבות של התאבדות?	{0, אינו ישים; רוצה רק למות}...
c_ssrs_fu_reason_clin	Numeric	איזה סוג מניעים גרמו לך לחשוב על הרצון למות או להתאבד? האם היה זה כדי לגמור עם הכאב או להפסיק את האופן בו את/ה חש/ה (במלים אחרות, לא היית מסוגל/ת	{0, אינו ישים}...
c_ssrs_fu_attemp_clin	Numeric	פעולה בעלת פוטנציאל של פגיעה עצמית, אשר ננקטה תוך לפחות רצון מסוים למות בעקבות הפעולה. ההתנהגות נחשבה בחלקה כשיטת התאבדות. הכוונה אינה חייבת	{0, לא}...
c_ssrs_fu_attemp_2_3_clin	String	נא להזין מס כולל של ניסיונות	None
c_ssrs_fu_attemp_3_clin	Numeric	האם הנבדק/ת התנהג/ה באופן של פגיעה עצמית שאיננה אובדנית?	{0, לא}...
c_ssrs_fu_attemp_4_clin	Numeric	האם קרה בעבר, שהתחלת לבצע משהו כדי לשים קץ לחייך, אך מישהו או משהו עצר בעדך בטרם הספקת לבצע דבר למעשה?	{0, לא}...
c_ssrs_fu_attemp_4_2_clin	String	אם כן, נא לתאר	None
c_ssrs_fu_attemp_4_3_clin	Numeric	נא להזין מס כולל של מסוכלים	None
c_ssrs_fu_attemp_5_clin	Numeric	האם קרה בעבר, שהתחלת לבצע משהו כדי לנסות לשים קץ לחייך, אך עצרת בעצמך בטרם ביצעת משהו למעשה?	{0, לא}...
c_ssrs_fu_attemp_5_2_clin	String	אם כן, נא לתאר	None
c_ssrs_fu_attemp_5_3_clin	Numeric	נא להזין מס כולל של נזנחים	None
c_ssrs_fu_attemp_6_clin	Numeric	האם נקטת צעדים כלשהם לקראת ביצוע ניסיון התאבדות או התחלת בפעולות הכנה (כגון איסוף כדורים, הצטיידות באקדח, מסירה של דברי ערך או חיבור מכתב פרי�	{0, לא}...
c_ssrs_fu_attemp_6_2_clin	String	אם כן, נא לתאר	None
c_ssrs_fu_attemp_7_clin	Numeric	התנהגות אובדנית הייתה קיימת בתקופת ההערכה	{0, לא}...
c_ssrs_fu_attemp_8_clin	Numeric	התאבדות שבוצעה	{1, כן}...
c_ssrs_fu_done_clin	Numeric	תוצאה קטלנית בפועל / נזק רפואי:	{0, 0 = ללא נזק גופני או נזק גופני מזערי (כגון שריטות שטחיות)}...
c_ssrs_fu_done_2_clin	Numeric	אפשרות של תוצאה קטלנית כתוצאה מהניסיון בפועל ללא פגיעה גופנית (הדוגמאות הבאות, למרות שאין בהן למעשה פגיעה גופנית, יש בהן פוטנציאל קטלני רצינ�	{0, 0 = אין סבירות כי ההתנהגות תגרום לפגיעה}...
cssrs_fw_maya_complete	Numeric	Complete?	{0, Incomplete}...

"""