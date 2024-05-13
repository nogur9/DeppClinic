import pandas as pd
from source.utils.consts.questions_columns import full_questionnaire_list, sci_af_ca, mfq, sdq, c_ssrs_intake, siq, CGI


class ExportColumnsManager:
    INFO_COLUMNS = ['gender', 'redcap_event_name', 'age_child_pre']
    TIME_COLUMNS = ['sciafca_timestamp']

    def __init__(self, questionnaires=None, id_column='id'):
        self.id_column = id_column
        self.columns = self.setup_initial_columns(questionnaires)
        self.ordered_columns_with_id = self.setup_ordered_columns()

    def setup_initial_columns(self, questionnaires):
        if questionnaires is None:
            # Define the default columns using class-level constants
            return self.INFO_COLUMNS + self.TIME_COLUMNS + full_questionnaire_list
        else:
            return self.INFO_COLUMNS + self.TIME_COLUMNS + questionnaires

    def setup_ordered_columns(self):
        # Create a unique list of columns starting with id_column and avoiding duplicates
        unique_columns = {self.id_column}  # start with id_column to ensure it is first
        unique_columns.update(self.columns)
        return list(unique_columns)

    def add_columns(self, new_columns):
        # Add new columns ensuring no duplicates and maintaining order
        current_set = set(self.ordered_columns_with_id)
        for column in new_columns:
            if column not in current_set:
                self.ordered_columns_with_id.append(column)
                current_set.add(column)

    def get_export_columns(self, include_id=True):
        # Return the ordered list of columns with duplicates removed
        if include_id:
            return self.ordered_columns_with_id
        else:
            return [i for i in self.ordered_columns_with_id if i != self.id_column]