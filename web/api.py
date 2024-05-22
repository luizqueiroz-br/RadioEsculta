from flask import Flask, jsonify

from DataBase.mongohelper import mongoHelper

app = Flask(__name__)

mon = mongoHelper()


@app.route("/api/get_conversation")
def get_conversation():

    return jsonify(mon.get_all_conversation())


# @app.route("/api/search_conversation")
# def get_conversation():
#     return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
