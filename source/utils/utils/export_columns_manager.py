from source.utils.consts.standard_names import ID_COLUMN
from source.utils.questionnaire.questionnaires_map import QuestionnairesMap


class ExportColumnsManager:
    INFO_COLUMNS = ['gender', 'age_child_pre']  # redcap_event_name has no meaning since we are using measurement times

    def __init__(self, questionnaires=None, id_column=ID_COLUMN):
        self.questionnaires = questionnaires
        self.id_column = id_column
        self.columns = self.setup_initial_columns(self.questionnaires)
        self.columns_for_extraction = self.setup_ordered_columns()  # ordered columns, with the id column

    def setup_initial_columns(self, questionnaires):
        if type(questionnaires) is QuestionnairesMap:
            questionnaires_columns = questionnaires.get_columns()
            return self.INFO_COLUMNS + questionnaires_columns
        else:
            return self.INFO_COLUMNS + questionnaires

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

    def add_columns(self, new_columns, is_info=False):

        # Add new columns ensuring no duplicates and maintaining order

        if is_info:
            assert not new_columns in self.columns_for_extraction
            self.INFO_COLUMNS.extend(new_columns)
            self.columns = self.setup_initial_columns(self.questionnaires)
            self.columns_for_extraction = self.setup_ordered_columns()  # ordered columns, with the id column
        else:
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

    def drop(self, value):
        if type(value) is list:
            for v in value:
                self.columns_for_extraction.remove(v)
        else:
            self.columns_for_extraction.remove(value)
