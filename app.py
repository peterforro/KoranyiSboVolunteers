from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    name = request.args.get("name", "")
    return f"<h1>Hello {name}!!!</h1>"


if __name__ == "__main__":
    app.run()