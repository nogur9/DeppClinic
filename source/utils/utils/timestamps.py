import pandas as pd


class TimestampCreator:
    INTAKE_TIMESTAMPS = ['opening_timestamp', 'mfq_short_timestamp', 'complaint_date']

    FOLLOWUP_TIMESTAMPS = ['sciafca_timestamp', 'mfq_short_timestamp', 'chameleon_timestamp',
                    'chameleon_suicide_er_date_stu', 'chameleon_psychiatric_date_stu',
                    'opening_child_pre_timestamp', 'cssrs_timestamp', 'siq_timestamp']


    def __init__(self):
        pass

    @staticmethod
    def convert_datetime(date_str):
        try:
            return pd.to_datetime(date_str)
        except ValueError:
            try:
                return pd.to_datetime(int(date_str))
            except ValueError:
                try:
                    return pd.to_datetime(date_str.split(" ")[0], errors='coerce')

                except AttributeError:
                    return pd.NaT

    @staticmethod
    def parse_datetime(date_str):
        try:
            return pd.to_datetime(date_str)
        except ValueError:
            try:
                return pd.to_datetime(date_str.split(" ")[0], errors='coerce')

            except AttributeError:
                return pd.NaT

