import pandas as pd
import psycopg2


def creating_empty_old_data_tables(conn_str):

    conn = psycopg2.connect(conn_str)
    sql = "SELECT * FROM auxiliary_questionnaires_data.old_data_questionnaires_columns_names;"
    df = pd.read_sql_query(sql, conn)
    conn.close()

    number_of_questionnaires = len(list(df.questionnaire_name))

    for i in range(number_of_questionnaires):

        if len(df.column_names[i]) > 0:

            questions_str = [f"{column} VARCHAR (4096)" for column in df.column_names[i]]

            create_table = """CREATE TABLE old_data.{0}(
            primary_key VARCHAR (50) PRIMARY KEY,
            {1});""".format(df.questionnaire_name[i], ',\n'.join(questions_str))

        else:
            create_table = """CREATE TABLE old_data.{0}(
            primary_key VARCHAR (50) PRIMARY KEY
            );""".format(df.questionnaire_name[i])

        conn = psycopg2.connect(conn_str)
        cur = conn.cursor()
        cur.execute(create_table)
        conn.commit()
        cur.close()
        conn.close()


def delete_old_data_tables(conn_str):

    conn = psycopg2.connect(conn_str)
    sql = "SELECT * FROM auxiliary_questionnaires_data.old_data_questionnaires_columns_names;"
    df = pd.read_sql_query(sql, conn)
    conn.close()

    number_of_questionnaires = len(list(df.questionnaire_name))

    for i in range(number_of_questionnaires):
        delete_table = """
        DROP TABLE old_data.{0}
        """.format(df.questionnaire_name[i])

        conn = psycopg2.connect(conn_str)
        cur = conn.cursor()
        cur.execute(delete_table)
        conn.commit()
        cur.close()
        conn.close()


