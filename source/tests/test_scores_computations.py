import unittest
import pandas as pd
from source.utils.questionnaires_scores import get_max_index, calculate_c_ssrs_individual_score


class TestGetMaxIndex(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        self.df = pd.DataFrame({
            'c_ssrs_1': [0, 1, 0, 0, 1],
            'c_ssrs_2': [0, 1, 1, 0, 0],
            'c_ssrs_3': [1, 0, 1, 1, 1],
            'c_ssrs_4': [0, 0, 0, 1, 1],
            'c_ssrs_5': [1, 0, 0, 0, 0],
            'c_ssrs_6': [0, 0, 0, 1, 0],
            'c_ssrs_last_visit_6': [0, 1, 0, 0, 0]
        })
        # Create a sample questions values map
        self.questions_values_map = {
            'c_ssrs_1': 1,
            'c_ssrs_2': 2,
            'c_ssrs_3': 3,
            'c_ssrs_4': 4,
            'c_ssrs_5': 5,
            'c_ssrs_6': 6,
            'c_ssrs_last_visit_6': 6
        }

    def test_get_max_index(self):
        # Call the function with the sample DataFrame and questions values map
        result = get_max_index(self.df, self.questions_values_map)

        # Define the expected output based on the sample DataFrame
        expected_output = pd.Series([5, 6, 3, 6, 4])

        # Assert that the actual output matches the expected output
        self.assertTrue(result.equals(expected_output))


class TestCalculateCSSRSIndividualScore(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        self.df = pd.DataFrame({
            'c_ssrs_1': [0, 1, 0, 1, 1],
            'c_ssrs_2': [0, 1, 1, 0, 0],
            'c_ssrs_3': [1, 0, 0, 1, 1],
            'c_ssrs_4': [0, 0, 0, 1, 0],
            'c_ssrs_5': [1, 0, 1, 0, 0],
            'c_ssrs_6': [0, 1, 0, 1, 0],
            'c_ssrs_last_visit_6': [0, 1, 1, 0, 0]
        })

    def test_calculate_c_ssrs_individual_score_idea(self):
        # Call the function with severity='idea' and the sample DataFrame
        result = calculate_c_ssrs_individual_score(self.df, 'idea')

        # Define the expected output based on the sample DataFrame and severity='idea'
        expected_output = pd.Series([5, 2, 5, 4, 3])

        # Assert that the actual output matches the expected output
        self.assertTrue(result.equals(expected_output))

    def test_calculate_c_ssrs_individual_score_stb(self):
        # Call the function with severity='stb' and the sample DataFrame
        result = calculate_c_ssrs_individual_score(self.df, 'stb')

        # Define the expected output based on the sample DataFrame and severity='stb'
        expected_output = pd.Series([5, 6, 6, 6, 3])

        # Assert that the actual output matches the expected output
        self.assertTrue(result.equals(expected_output))

    def test_calculate_c_ssrs_individual_score_invalid_severity(self):
        # Call the function with an invalid severity value
        with self.assertRaises(ValueError):
            calculate_c_ssrs_individual_score(self.df, 'invalid')


class TestCalculateCSSRSIndividualScore1(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        self.df = pd.DataFrame({
            'c_ssrs_1': [0, 1, 0],
            'c_ssrs_2': [0, 1, 0],
            'c_ssrs_3': [1, 0, 1],
            'c_ssrs_4': [1, 1, 0],
            'c_ssrs_5': [0, 0, 1],
            'c_ssrs_6': [0, 0, 0],
            'c_ssrs_last_visit_6': [1, 0, 1]
        })

    def test_calculate_c_ssrs_individual_score_idea(self):
        # Call the function with severity as 'idea'
        result = calculate_c_ssrs_individual_score(self.df, 'idea')

        # Define the expected output based on the sample DataFrame and severity
        expected_output = pd.Series([5, 3, 6])

        # Assert that the actual output matches the expected output
        self.assertTrue(result.equals(expected_output))

    def test_calculate_c_ssrs_individual_score_stb(self):
        # Call the function with severity as 'stb'
        result = calculate_c_ssrs_individual_score(self.df, 'stb')

        # Define the expected output based on the sample DataFrame and severity
        expected_output = pd.Series([6, 4, 6])

        # Assert that the actual output matches the expected output
        self.assertTrue(result.equals(expected_output))

    def test_calculate_c_ssrs_individual_score_invalid_severity(self):
        # Call the function with an invalid severity
        with self.assertRaises(ValueError):
            calculate_c_ssrs_individual_score(self.df, 'invalid')
