import psycopg2
import pytest


# connect postgres DB
@pytest.fixture(name='setup_db', scope='session')
def connect_dababase():
    try:
        connect = psycopg2.connect(
            host="localhost",
            database="upre",
            user="upre",
            password="admin"
        )

        return print(connect)

    except (Exception, psycopg2.DatabaseError) as error:
        raise error


@pytest.fixture(name='db_insert', scope='function')
def insert(execution_id, execution_date, test_name, results):
    try:
        conn = connect_dababase()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO results (execution_id, execution_date, test_name, results) "
                       f"values ({execution_id}, {execution_date}, {test_name}, {results})")
    except (Exception, psycopg2.DatabaseError) as error:
        raise error



