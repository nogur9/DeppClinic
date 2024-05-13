from source.utils.consts.assistment_consts import imputation_questionnaires
from source.utils.util_functions import impute_from_questionnaire
from to_delete.data_manipulation.data_imputation import impute_from_column
import pandas as pd



def do_questionnaires_imputations(df):
    for questionnaire_imputation in imputation_questionnaires:
        try:
            df = impute_from_questionnaire(df, questionnaire_imputation['origin'], questionnaire_imputation['replacement'])
        except KeyError:
            pass

    return df



def impute_events(df1, df2, columns, suffix):
    imputed_data = pd.merge(df1, df2, on=['id'], how='outer', suffixes=('', f'_{suffix}'))

    for column_name in columns.get_export_columns(include_id=False):
        imputed_data = impute_from_column(imputed_data, impute_to=column_name,
                                          impute_from=f'{column_name}_{suffix}')

    duplicated_columns = [i for i in imputed_data.columns if i.endswith(f'_{suffix}')]
    imputed_data = imputed_data.drop(duplicated_columns, axis=1)

    return imputed_data