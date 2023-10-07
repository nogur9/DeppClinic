import pandas as pd

import pandas as pd


def determine_questionnaire_operator(row):
    """
    Determine if data in the row belongs to either a student or a clinician.

    This function first checks the 'who' column:
    - 1 represents a clinician.
    - 2 represents a student.

    If the 'who' column is empty, it checks the 'opening_therapist_battery_timestamp' column:
    If this column is not empty, it's considered as belonging to a clinician.

    Args:
        row (pandas.Series): A row of data from the dataset.

    Returns:
        str: 'clinician' if the data belongs to a clinician, 'student' otherwise.
    """

    default_operator = 'student'  # Default to 'student'

    if not pd.isnull(row['who']):
        if row['who'] == 1:
            return 'clinician'
        elif row['who'] == 2:
            return 'student'
        else:
            raise ValueError("invalid data in 'who' column")

    # If 'who' is empty, check 'opening_therapist_battery_timestamp' column
    if not pd.isnull(row['opening_therapist_battery_timestamp']):
        return 'clinician'

    return default_operator



