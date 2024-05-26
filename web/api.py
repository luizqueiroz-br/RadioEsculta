from flask import Flask, jsonify, request

from DataBase.mongohelper import mongoHelper

app = Flask(__name__)

mon = mongoHelper()


@app.route("/api/get_conversation", method=["GET"])
def get_conversation():
    page = request.args.get("page", 1)
    limit = request.args.get("limit", 100)
    skip = (page - 1) * limit
    return jsonify(mon.get_all_conversation(limit, skip))


if __name__ == "__main__":
    app.run(debug=True)
