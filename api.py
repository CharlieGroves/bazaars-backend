import flask
from flask import jsonify
from firestore import getUser, getAllUsers

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    data = getAllUsers()
    return jsonify(data);

@app.route('/get/user/<page_id>', methods=['GET'])
def getUserId(page_id):
    user = getUser(page_id)
    return jsonify(user)

app.run()