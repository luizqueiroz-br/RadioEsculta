from flask import Flask

app = Flask(__name__)


@app.route("/api/get_conversation")
def get_conversation():
    return "Hello World!"


@app.route("/api/search_conversation")
def get_conversation():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
