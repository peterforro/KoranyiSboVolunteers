import os
from os import name
import psycopg2, psycopg2.extras
import urllib

def open_database():
    username = os.environ.get('dbuser')
    password = os.environ.get('dbpassword')
    host = os.environ.get('host')
    name = os.environ.get('dbname')
    port = int(os.environ.get('port'))
    try:
        connection = psycopg2.connect(
            user = username,
            password = password,
            host = host,
            port = port,
            dbname = name
        )
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print('Database connection problem')
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value
    return wrapper


if __name__ == "__main__":
    open_database()