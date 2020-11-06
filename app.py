from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    print("\n\n\n!!!!!!!!!!!!Teszt trace log!!!!!!!!!!!!\n\n\n")
    return "<h1>Hello World!</h1>"



if __name__ == "__main__":
    app.run(
        host = "0.0.0.0,",
        port = 80,
        debug = True
    )