
def fill_patient_id_from_first_record(df):
    """
    This function takes a DataFrame as input and populates empty 'id' values in all patient records
    by matching them to the 'id' value in the first record of each patient.

    Parameters:
        df (pandas DataFrame): The DataFrame to be processed, typically sourced from a RedCap database.

    Returns:
        pandas DataFrame: The DataFrame with 'id' values filled based on the first record of each patient.
    """
    record_to_patient_id_map = df.dropna(subset=['patient_id']).groupby('record_id')['patient_id'].first()
    record_to_patient_id_map = {key: record_to_patient_id_map[key] for key in record_to_patient_id_map.keys()}
    try:
        df['patient_id'] = df['record_id'].apply(lambda x: record_to_patient_id_map[x])
    except KeyError:
        raise KeyError("Probably 'record_id' missing 'patient_id'")

    return df


