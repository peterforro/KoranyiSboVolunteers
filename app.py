from queries import *
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html', users = get_users())


if __name__ == "__main__":
    app.run()