from flask import Flask, request
from queries import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    users = get_users()
    result = ""
    for user in users:
        result += f"<h1>{user.get('firstname')} {user.get('lastname')}</h1>"
    return result


if __name__ == "__main__":
    app.run()