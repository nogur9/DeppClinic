import pandas as pd
import numpy as np

from source.utils.consts.standard_names import INTAKE
from source.utils.dataset_creation.pathology_assessment.pathology_variable import PathologyVariable


class PsychologicalAssessment:
    THRESHOLD = 1
    BINARY_MFQ = ['mfq_34', 'mfq_35', 'mfq_36', 'mfq_37']

    def __init__(self, pathology: PathologyVariable, preprocess=True):

        self.pathology = pathology
        self.preprocess = preprocess

    def calculate_target_pathology(self, df):
        df = self._calculate_missing_values(df)
        columns_to_preprocess = self._identify_columns_to_preprocess()
        processed_df = self._preprocess_columns(df, columns_to_preprocess)
        df[self.pathology.name] = (processed_df.sum(axis=1) > 0).astype(int)
        self._drop_irrelevant_values(df)
        return df

    def _calculate_missing_values(self, df):
        missing_values = df[self.pathology.questions].isnull()
        missing_values_ratio = missing_values.sum(axis=1) / len(self.pathology.questions)
        df[f'ratio_of_missing_{self.pathology.name}_values'] = missing_values_ratio
        return df

    def _identify_columns_to_preprocess(self):

        preprocess_columns = [col for col in self.pathology.questions if 'chameleon' in col]
        preprocess_columns += [col for col in self.pathology.questions if col in self.BINARY_MFQ]
        return preprocess_columns

    def _preprocess_columns(self, df, columns_to_preprocess):
        processed_df = df.copy()
        aligned_columns = [f"{col}_align" for col in columns_to_preprocess]
        processed_df[aligned_columns] = processed_df[columns_to_preprocess].replace({2: 0, 3: 0})
        return processed_df[self.pathology.questions + aligned_columns]

    def _drop_irrelevant_values(self, df):
        df.loc[df[f'ratio_of_missing_{self.pathology.name}_values'] >= 1, self.pathology.name] = np.nan

        if self.pathology.only_intake_evaluation:
            df.loc[df['measurement'] != INTAKE, self.pathology.name] = np.nan
        elif self.pathology.only_follow_up_evaluation:
            df.loc[df['measurement'] == INTAKE, self.pathology.name] = np.nan


def test_psychological_assessment():
    # Example usage
    questions_for_suicide_attempt = [
        'mfq_36', 'mfq_34',
        'c_ssrs_t_11_life_clin',
        'c_ssrs_t_12_life_clin',
        'c_ssrs_t_13_life_clin',
        'chameleon_attempt_stu',
    ]
    disease_name = 'suicide_attempt'

    assessment = PsychologicalAssessment(disease_name, questions_for_suicide_attempt)
    df = pd.DataFrame()  # Replace with your actual DataFrame
    df = assessment.calculate_target_variable(df)
