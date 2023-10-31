from creating_the_clinic_dataset.step1_fill_missing_2021_clin_stu.completing_missing_clinician_questionnaire_2021 import \
    prepare_datasets, get_columns_range, create_columns_names_mapping, \
    map_additional_column_name_to_2021_clinician_column_name, map_additional_column_name_to_2021_student_column_name
import psycopg2
import pandas as pd


def upload_to_redcap_data(conn_str, questionnaire, old_2_redcap_map):

    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()

    cur.execute("""UPDATE  auxiliary_questionnaires_data.questionnaires_columns_names
    SET old_data_column_names_map = '{0}'
    WHERE questionnaire_name = {1};""".format(repr(old_2_redcap_map).replace("'", "\""), questionnaire))

    # Make the changes to the database persistent
    conn.commit()

    # Close cursor and communication with the database
    cur.close()
    conn.close()


def upload_to_old_data(conn_str, questionnaire, imputation_2_old_map):
    conn = psycopg2.connect(conn_str, questionnaire)
    cur = conn.cursor()

    cur.execute("""UPDATE  auxiliary_questionnaires_data.old_data_questionnaires_columns_names
    SET imputation_data_to_old_data_map = '{0}'
    WHERE questionnaire_name = {1};""".format(repr(imputation_2_old_map).replace("'", "\""), questionnaire))

    # Make the changes to the database persistent
    conn.commit()

    # Close cursor and communication with the database
    cur.close()
    conn.close()


def add_name_mapping_to_DB(conn_str, questionnaires_cluster, columns_range_mapping, transformation_function,
                           is_student_data=False, is_clinician_data=False):

    old_data, redcap_data, imputation_data = prepare_datasets()
    old_data_columns, redcap_data_columns, imputation_data_columns = get_columns_range(old_data, redcap_data,
                                                                                       imputation_data,
                                                                                       columns_range_mapping,
                                                                                       is_student_data=is_student_data,
                                                                                       is_clinician_data=is_clinician_data)

    old_data_2_imputation_data_mapping = create_columns_names_mapping(old_data_columns, imputation_data_columns,
                                                                      transformation_function,
                                                                      is_clinician_imputation_data=is_clinician_data)

    redcap_data_2_old_data_mapping = create_columns_names_mapping(old_data_columns, imputation_data_columns,
                                                                  transformation_function)

    upload_to_db(questionnaires_cluster, conn_str, upload_to_old_data, old_data_2_imputation_data_mapping, "old_data")
    upload_to_db(questionnaires_cluster, conn_str, upload_to_redcap_data, redcap_data_2_old_data_mapping, "redcap_data")


def upload_to_db(questionnaires_cluster, conn_str, upload_function, columns_names_mapping, table_name):

    conn = psycopg2.connect(conn_str)
    sql = f"SELECT * FROM auxiliary_questionnaires_data.{table_name};"
    column_names_table = pd.read_sql_query(sql, conn)
    conn.close()

    for questionnaire in questionnaires_cluster:
        questionnaire_columns = \
        column_names_table.loc[column_names_table['questionnaire_name'] == questionnaire, 'column_names'].values[0]
        filtered_mapping = {key: columns_names_mapping[key] for key in questionnaire_columns if
                            key in columns_names_mapping}

        upload_function(conn_str, questionnaire, filtered_mapping)


def add_column_names_mapping(conn_str):
    # Chameleon

    columns_range_mapping = {
        'old_data_start_column': 'chameleon_timestamp',
        'old_data_end_column': 'chameleon_complete',
        'redcap_data_start_column': 'chameleon_timestamp',
        'redcap_data_end_column': 'chameleon_complete',
        'imputation_data_start_column': 'chameleon_timestamp',
        'imputation_data_end_column': 'chameleon_complete'

    }

    transformation_function = map_additional_column_name_to_2021_student_column_name
    add_name_mapping_to_DB(conn_str, ['chameleon'], columns_range_mapping, transformation_function)

    # Student

    student_questionnaires = ["opening_students", "trq_sf_maris_stu", "remote_stu", "cps_stu", "scs_stu",
                              "mini_kid_sum_stu", "c_ssrs_stu"]
    columns_range_mapping = {
        'old_data_start_column': 'opening_students_timestamp',
        'old_data_end_column': 'opening_students_timestamp',
        'redcap_data_start_column': 'opening_students_timestamp',
        'redcap_data_end_column': 'opening_students_timestamp',
        'imputation_data_start_column': 'opening_clinicians_complete',
        'imputation_data_end_column': 'cssrs_t_complete'

    }

    transformation_function = map_additional_column_name_to_2021_student_column_name
    add_name_mapping_to_DB(conn_str, student_questionnaires, columns_range_mapping, transformation_function,
                           is_student_data=True)

    # Clinician

    clinician_questionnaires = ['c_ssrs_clin', 'mini_kid_sum_clin', 'screening_form', 'suicide_form_clin', 'ffq',
                                'cdrsr_clin', 'scs_clin', 'er_questionnaire_clin', 'cps_clin', 'remote_clin',
                                'opening_therapist_battery', 'cgi_s_clin', 'trq_sf_maris_clin', 'maris_y_scars_clin',
                                'wai_immirisk_clin']
    columns_range_mapping = {
        'old_data_start_column': 'wai_immirisk_clin_timestamp',
        'old_data_end_column': 'cssrs_t_clin_complete',
        'redcap_data_start_column': 'wai_immirisk_clin_timestamp',
        'redcap_data_end_column': 'cssrs_t_clin_complete',
        'imputation_data_start_column': 'wai_immirisk_clin_timestamp',
        'imputation_data_end_column': 'cssrs_t_complete',
        'redcap_data_start_column_2': 'cssrs_fw_maya_timestamp',
        'redcap_data_end_column_2': 'cssrs_fw_maya_complete'

    }

    transformation_function = map_additional_column_name_to_2021_clinician_column_name
    add_name_mapping_to_DB(conn_str, clinician_questionnaires, columns_range_mapping, transformation_function,
                           is_clinician_data=True)

