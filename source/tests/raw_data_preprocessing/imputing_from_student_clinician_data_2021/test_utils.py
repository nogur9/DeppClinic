import unittest
import pandas as pd

# Import your function
from to_delete.raw_data_preprocessing.imputing_from_student_clinician_data_2021.utils import determine_questionnaire_operator


class TestDetermineQuestionnaireOperator(unittest.TestCase):

    def test_determine_questionnaire_operator(self):
        # Test when 'who' column is 1 (clinician)
        df = pd.DataFrame([{'who': 1, 'opening_therapist_battery_timestamp': None},
                            {'who': 2, 'opening_therapist_battery_timestamp': None},
                            {'who': None, 'opening_therapist_battery_timestamp': '01, 04, 1948'},
                            {'who': None, 'opening_therapist_battery_timestamp': None}])

        result = df.apply(determine_questionnaire_operator, axis=1)
        expected = pd.Series(['clinician', 'student', 'clinician', 'student'])
        self.assertTrue(result.equals(expected))


