from flask import Flask, request, render_template
from queries import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    names = get_users()
    return render_template("index.html", names=names)


if __name__ == "__main__":
    app.run()