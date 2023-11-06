import pandas as pd
import psycopg2
import os


def get_all_table_names(conn_str):
    conn = psycopg2.connect(conn_str)
    sql = """
    SELECT table_name FROM INFORMATION_SCHEMA.TABLES
    WHERE table_schema = N'old_data'
    """
    questionnaire_columns = list(pd.read_sql_query(sql, conn).table_name)
    conn.close()
    return questionnaire_columns


def get_column_names(questionnaire_name, conn_str):
    conn = psycopg2.connect(conn_str)
    sql = """
    SELECT *
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = N'{0}' 
    AND table_schema = N'old_data'
    """.format(questionnaire_name)

    questionnaire_columns = list(pd.read_sql_query(sql, conn).column_name)
    conn.close()
    return questionnaire_columns


def prepare_data(questionnaire_name, questionnaire_columns, old_data_df):
    questionnaire_data = old_data_df[questionnaire_columns]

    file_name = "old_{0}_data.csv".format(questionnaire_name)
    directory = r"C:/Users/nogur/Documents/DeppClinic/Data/postgres_db/old_data"
    full_path = r'{0}/{1}'.format(directory, file_name)
    questionnaire_data.to_csv(full_path, index=False)

    # Change the file permissions
    os.chmod(full_path, 0o777)
    os.chmod(directory, 0o777)

    return full_path


def upload_data(questionnaire_name, full_path, conn_str):
    upload_data = """
    COPY old_data.{0}
    FROM '{1}'
    DELIMITER ','
    CSV HEADER;

    """.format(questionnaire_name, full_path)

    conn = psycopg2.connect(conn_str)
    cur = conn.cursor()
    cur.execute(upload_data)
    conn.commit()
    cur.close()
    conn.close()


def upload_old_data(conn_str):
    old_data_df = pd.read_csv(r"..\Data\Transferring_Data_to_PostgreSQL\old_data.csv")
    table_names = get_all_table_names(conn_str)

    for questionnaire_name in table_names[1:]:
        # print(questionnaire_name)
        questionnaire_columns = get_column_names(questionnaire_name, conn_str)
        full_path = prepare_data(questionnaire_name, questionnaire_columns, old_data_df)
        upload_data(questionnaire_name, full_path, conn_str)

