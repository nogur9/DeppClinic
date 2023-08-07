import pandas as pd

def split_to_intersection_and_union(df_2021, df_2022):
    df_2021['original_dataset'] = '2021'
    df_2022['original_dataset'] = '2022'
    
    df_2022['id & redcup'] = df_2022['id'].astype(str) + '_' + df_2022['redcap_event_name'].astype(str)
    df_2021['id & redcup'] = df_2021['id'].astype(str) + '_' + df_2021['redcap_event_name'].astype(str)

    intersection_2022 = df_2022[df_2022['id & redcup'].isin(df_2021['id & redcup'])]
    df_2022_union = df_2022[~df_2022['id & redcup'].isin(df_2021['id & redcup'])]

    intersection_2021 = df_2021[df_2021['id & redcup'].isin(df_2022['id & redcup'])]
    df_2021_union = df_2021[~df_2021['id & redcup'].isin(df_2022['id & redcup'])]
    
    union = pd.concat([df_2022_union, df_2021_union])
    
    union = union.drop('id & redcup', axis=1)
    intersection_2021 = intersection_2021.drop(['id & redcup', 'original_dataset'], axis=1)
    intersection_2022 = intersection_2022.drop(['id & redcup', 'original_dataset'], axis=1)
    
    
    return union, intersection_2021, intersection_2022



def fix_wrong_groups(df):
   
    df = df.copy()
    df = fix_group_scpecific_case(df)
    
    #if group 3 appears with another group:
    #- take the 1/ 2
    
    # ['group___1', 'group___2', 'group___3']
    df.loc[(df['group___1'] == 1) & (df['group___3'] == 1), 'group___3'] = 0
    df.loc[(df['group___2'] == 1) & (df['group___3'] == 1), 'group___3'] = 0
    
    if df[(df['group___2'] == 1) & (df['group___1'] == 1)].shape[0]:
        print(df[(df['group___2'] == 1) & (df['group___1'] == 1)][['id', 'redcap_event_name']])
        raise ValueError
        
    return df


def is_equal(row, index, redcap_event_name, year=None):
    if (row['id'] == index) and (row['redcap_event_name'] == redcap_event_name):
        return True
    return False
    

def fix_scpecific_case(row, col_name, func):
    """
    take 2022:

    ids = 'T4075'
    event_name = 'control_5weeks_arm_1'
    col = 'dass_10_f' - 'dass_20_f'
    
    
    ids = 'O0618'
    event_name = '5th_session_arm_1'
    col = pps_2_f
    
    """
    
    dass = [f'dass_{i}_f' for i in range(10, 21)]
    
    if col_name in dass:
        if is_equal(row, 'T4075', 'control_5weeks_arm_1'):
            return 'take 2022'
    elif col_name == 'pps_2_f':
        if is_equal(row, 'O0618', '5th_session_arm_1'):
            return 'take 2022'

    return func


def apply_group(df, index, group):
    
    df = df.copy()
    
    for i in [1, 2, 3]:
        if i == group:
            df.loc[df['id'] == index, f'group___{i}'] = 1
        else:
            df.loc[df['id'] == index, f'group___{i}'] = 0
    
    return df
        
def fix_group_scpecific_case(df):
    """
    S1313['group___2'] = 0  -> group 1

    M6848['group___2'] = 0 -> group 1

    S7645['group___1'] = 0 -> group 2

    T9466[['group___1', group_2] = 0 / group 3 == 1 -> group 3
    """
    df = df.copy()
    
    change_groups = {
        'S1313': 1,
        'M6848': 1,
        'S7645': 2,
        'T9466': 3,
        'D2016': 2,
    }
    for index, group in change_groups.items():
        df = apply_group(df, index, group)
    
    return df


def resolve_contradiction(row, col_2021, col_2022, function = None, col_name= ''):
  
    if pd.isnull(row[col_2021]):
        return row[col_2022]
    elif pd.isnull(row[col_2022]):
        return row[col_2021]
    elif row[col_2022] == row[col_2021]:
        return row[col_2022]

    else:
        if col_name.startswith('dass_')  or col_name.startswith('pps_2_f'):
            function = fix_scpecific_case(row, col_name, function)
        
        if function == None:
            print(row['id'], row['redcap_event_name'])
            print('2021 =', row[col_2021])
            print('2022 =', row[col_2022])
            raise ValueError
        elif function == 'take 2021':
            return col_2021
        elif function == 'take 2022':
            return col_2022
        else:
            return function(row[col_2021], row[col_2022])