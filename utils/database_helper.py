import psycopg2


# connect postgres DB
def connect_dababase():
    """
    Connect the database
    :return: connection
    """
    try:
        connect = psycopg2.connect(
            host="localhost",
            database="upre_automation",
            user="postgres",
            password="admin"
        )

        return connect

    except (Exception, psycopg2.DatabaseError) as error:
        raise error


def insert(execution_id, execution_date, feature, test_name, outcome):
    """
    Insert results to the database
    :param execution_id: test execution id
    :param execution_date: test execution date
    :param feature: tested module/feature/section
    :param test_name: test name
    :param outcome: result failed or passed
    :return: error
    """
    try:
        conn = connect_dababase()
        cursor = conn.cursor()
        sql = '''
        insert into results (execution_id, execution_date, feature, test_name, outcome)
        values (%s,%s,%s,%s,%s)
        '''
        values = (execution_id, execution_date, feature, test_name, outcome)

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        raise error
    