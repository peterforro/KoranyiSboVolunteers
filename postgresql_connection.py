import psycopg2, psycopg2.extras
from os import environ
import urllib

class PostgreSQL:
    '''
    This class is responsible for creating the connection object of the
    on-prem (developer) or the cloud (Heroku) PostgreSQL database
    '''

    def __init__(self):
        '''
        Constructor method of the PostgreSQL object
        Determines whether the database is on-prem (developer) or cloud (Heroku) hosted
        '''
        self.__is_local = bool(environ.get('db_local', False))
        self.__conn_type = None
        self.__connection = None
        self.__cursor = None
    
    def __del__(self):
        '''
        Destructor of the class
        Releases the connection and the cursor object of the
        PostgreSQL database
        '''
        if self.__connection is not None:
            self.__connection.close()
            self.__cursor.close()

    def __local_connection(self):
        '''
        If the enivronment variable "db_local" is set as True, then 
        establishes connection with the on-prem developer PostgreSQL database
        '''
        self.__conn_type = 'local'
        self.__connection = psycopg2.connect(
            host = environ.get('db_host'),
            port = int(environ.get('db_port')),
            user = environ.get('db_user'),
            password = environ.get('db_password'),
            dbname = environ.get('db_name')
        )
    
    def __remote_connetion(self):
        '''
        If the enivronment variable "db_local" is set as True, or does not exists then 
        establishes connection with the Heroku PostgreSQL RDBMS service.
        '''
        self.__conn_type = 'remote'
        urllib.parse.uses_netloc.append('postgres')
        url = urllib.parse.urlparse(environ.get('DATABASE_URL'))
        self.__connection = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )

    def connect(self):
        '''
        Connects to the underlying on-prem (developer) or cloud (Heroku) PostgreSQL database,
        depending on the value of the "db_local" environment variable
        Returns: the cursor object of the PostgreSQL database connection
        '''
        try:
            if self.__is_local:
                self.__local_connection()
            else:
                self.__remote_connetion()
            self.__connection.autocommit = True
            type = psycopg2.extras.RealDictCursor
            self.__cursor = self.__connection.cursor(cursor_factory = type)
            return self.__cursor
        except psycopg2.DatabaseError as exception:
            print(f'Could not connect to {self.__conn_type} database')
            raise exception


def dbconnector(function):
    '''
    Decorator method that establishes the PostgreSQL database connection
    for the backend query functions.
    @Param1: function that has to be "decorated"
    Returns: The decorated function 
    '''
    def wrapper(*args, **kwargs):
        postgres = PostgreSQL()
        try:
            cursor = postgres.connect()
            result = function(cursor, *args, **kwargs)
            return result
        except Exception as exception:
            print(exception)
            raise exception
    return wrapper