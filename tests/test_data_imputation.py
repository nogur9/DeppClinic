import unittest

import numpy as np
import pandas as pd

from utils.data_manipulation.data_imputation import impute_mean_questionnaire_score


class TestImputeRowWithMean(unittest.TestCase):
    def test_impute_row_with_mean(self):
        # Define the column names
        ATHENS = [
            'athens_1',
            'athens_2',
            'athens_3',
            'athens_4',
            'athens_5',
            'athens_6',
            'athens_7',
            'athens_8'
        ]

        # Create a test DataFrame
        data = np.array([
            [1, np.nan, 3, np.nan, 5, 6, np.nan, np.nan],
            [2, 3, np.nan, 4, 5, np.nan, 7, np.nan],
            [np.nan, 2, 3, np.nan, np.nan, 6, np.nan, 8]
        ])
        df = pd.DataFrame(data, columns=ATHENS)

        # Impute missing values
        df = impute_mean_questionnaire_score(df, 'ATHENS')

        # Expected output
        expected_output = pd.DataFrame(
            np.array([
                [1, 3.75, 3, 3.75, 5, 6, 3.75, 3.75],
                [2, 3, 4.2, 4, 5, 4.2, 7, 4.2],
                [4.75, 2, 3, 4.75, 4.75, 6, 4.75, 8]
            ]),
            columns=ATHENS
        )

        # Compare the expected output with the actual result
        self.assertTrue(df.equals(expected_output))


