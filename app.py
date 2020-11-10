from flask import Flask, request
from db_connection import connection_handler

app = Flask(__name__)

@connection_handler
def get_users(cursor):
    query = ''' SELECT * FROM users'''
    cursor.execute(query)
    return cursor.fetchall()


@app.route("/", methods=["GET"])
def index():
    users = get_users()
    result = ""
    for user in users:
        result += f"<h1>{user.get('firstname')} {user.get('lastname')}</h1>"
    return result


if __name__ == "__main__":
    app.run()