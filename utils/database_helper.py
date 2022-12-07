import psycopg2


# connect postgres DB
def connect_dababase():
    try:
        connect = psycopg2.connect(
            host="localhost",
            database="upre",
            user="postgres",
            password="admin"
        )

        return connect

    except (Exception, psycopg2.DatabaseError) as error:
        raise error


def insert(execution_id, execution_date, test_name, outcome):
    try:
        conn = connect_dababase()
        cursor = conn.cursor()
        sql = '''
        insert into results (execution_id, execution_date, test_name, outcome)
        values (%s,%s,%s,%s)
        '''
        values = (execution_id, execution_date, test_name, outcome)

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error



