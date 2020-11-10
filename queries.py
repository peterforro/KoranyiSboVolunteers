from postgresql_connection import dbconnector

@dbconnector
def get_users(cursor):
    query = '''
        SELECT
            CONCAT(firstname, ' ', lastname) AS fullname
        FROM
            Accounts
    '''
    cursor.execute(query)
    return cursor.fetchall()