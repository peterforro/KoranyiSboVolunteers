from os import environ
import urllib
import psycopg2, psycopg2.extras

class PostgreSQL:
    def __init__(self):
        self.__is_local = bool(environ.get('db_local', False))
        self.__conn_type = None
        self.__connection = None
        self.__cursor = None
    
    def __del__(self):
        print('Deleted!')
        if self.__connection is not None:
            self.__cursor.close()
            self.__connection.close()

    def __local_connection(self):
        self.__conn_type = 'local'
        self.__connection = psycopg2.connect(
            host = environ.get('db_host'),
            port = environ.get('db_port'),
            user = environ.get('db_user'),
            password = environ.get('db_password'),
            database = environ.get('db_name')
        )

    def __remote_connection(self):
        self.__conn_type = 'remote'
        urllib.parse.uses_netloc.append('postgres')
        url = urllib.parse.urlparse(environ.get('DATABASE_URL'))
        self.__connection = psycopg2.connect(
            host=url.hostname,
            port=url.port,
            user=url.username,
            password=url.password,
            database=url.path[1:]
        )

    def connect(self):
        try:
            if self.__is_local:
                self.__local_connection()
            else:
                self.__remote_connection()
            self.__connection.autocommit = True
            type = psycopg2.extras.RealDictCursor
            self.__cursor = self.__connection.cursor(cursor_factory = type)
            return self.__cursor
        except psycopg2.DatabaseError as exception:
            print('Database connection problem')
            raise exception


def dbconnector(function):
    def wrapper(*args, **kwargs):
        postgres = PostgreSQL()
        cursor = postgres.connect()
        return function(cursor, *args, **kwargs)
    return wrapper
