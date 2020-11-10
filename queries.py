from postgresql_connection import dbconnector

@dbconnector
def get_users(cursor):
    query = ''' SELECT * FROM users'''
    cursor.execute(query)
    return cursor.fetchall()
