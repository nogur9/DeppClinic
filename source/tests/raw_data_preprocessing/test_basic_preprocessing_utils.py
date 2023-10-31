import unittest
import pandas as pd

# Import your function
from to_delete.raw_data_preprocessing.basic_preprocessing_utils import fill_patient_id_from_first_record


class TestFillPatientId(unittest.TestCase):

    def test_fill_patient_id_from_first_record(self):
        # Create a sample DataFrame for testing
        data = {'record_id': [1, 1, 2, 2, 2],
                'patient_id': [None, "123D", None, "456A", None]}
        df = pd.DataFrame(data)

        # Expected result after running the function
        expected_data = {'record_id': [1, 1, 2, 2, 2],
                         'patient_id': ["123D", "123D", "456A", "456A", "456A"]}
        expected_df = pd.DataFrame(expected_data)

        # Call the function
        result_df = fill_patient_id_from_first_record(df)

        # Check if the result matches the expected DataFrame
        self.assertTrue(result_df.equals(expected_df))
