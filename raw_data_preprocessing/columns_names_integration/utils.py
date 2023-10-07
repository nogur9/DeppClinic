import re


def map_additional_column_name_to_2021_student_column_name(column_name, target_columns_names):
    # Case 1: Special case for 'cgi_s'
    if column_name == 'cgi_s':
        return 'cgi_s_base_stu', True

    # Case 2: Check if the column_name is already in target_columns_names
    if column_name in target_columns_names:
        return column_name, True

    # Case 3: Check for a pattern like '___\d+' and transform it
    match = re.search(r'___\d+$', column_name)
    if match:
        suffix = match.group(0)
        new_column_name = column_name.replace(suffix, f'_stu{suffix}')
        if new_column_name in target_columns_names:
            return new_column_name, True

    # Case 4: Try adding '_stu' at the end and validate
    new_column_name = f'{column_name}_stu'
    if new_column_name in target_columns_names:
        return new_column_name, True

    # Case 5: If all else fails, try replacing the last word with 'stu' and validate
    words = column_name.split('_')
    words[-1] = 'stu'
    new_column_name = '_'.join(words)
    if new_column_name in target_columns_names:
        return new_column_name, True

    # If none of the cases match, return the original column_name with success=False
    return column_name, False
