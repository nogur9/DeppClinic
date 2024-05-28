from source.utils.consts.questions_columns import full_questionnaire_list


class ExportColumnsManager:
    INFO_COLUMNS = ['gender', 'redcap_event_name', 'age_child_pre']
    TIME_COLUMNS = ['sciafca_timestamp']

    def __init__(self, questionnaires=None, id_column='id'):
        self.id_column = id_column
        self.columns = self.setup_initial_columns(questionnaires)
        self.columns_for_extraction = self.setup_ordered_columns() #ordered columns, with the id column

    def setup_initial_columns(self, questionnaires):
        if questionnaires is None:
            # Define the default columns using class-level constants
            return self.INFO_COLUMNS + self.TIME_COLUMNS + full_questionnaire_list
        else:
            return self.INFO_COLUMNS + self.TIME_COLUMNS + questionnaires

    def setup_ordered_columns(self):
        # Create a unique list of columns starting with id_column and avoiding duplicates
        ordered_unique_columns = self._remove_duplicates([self.id_column] + self.columns)
        return ordered_unique_columns

    def _remove_duplicates(self, input_list):
        seen = set()
        output_list = []
        for item in input_list:
            if item not in seen:
                seen.add(item)
                output_list.append(item)
        return output_list

    def add_columns(self, new_columns):
        # Add new columns ensuring no duplicates and maintaining order
        current_set = set(self.columns_for_extraction)
        for column in new_columns:
            if column not in current_set:
                self.columns_for_extraction.append(column)
                current_set.add(column)

    def get_export_columns(self, include_id=True):
        # Return the ordered list of columns with duplicates removed
        if include_id:
            return self.columns_for_extraction
        else:
            return [i for i in self.columns_for_extraction if i != self.id_column]