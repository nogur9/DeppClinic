import numpy as np
import pandas as pd


def remove_invalid_values(df, valid_values, filtered_columns):
    for column in filtered_columns:
        df.loc[~df[column].isin(valid_values), column] = np.nan

    return df


def test_remove_invalid_values():

    # Sample DataFrame
    data = {'A': [1, 2, 3, 4, 5],
            'B': ['apple', 'banana', 'cherry', 'date', 'elderberry']}
    df = pd.DataFrame(data)

    expected_data = {'A': [1, 2, 3, 4, 5],
            'B': ['apple', 'banana', 'cherry', np.nan, np.nan]}
    expected_df = pd.DataFrame(expected_data)
    assert (expected_df == df)