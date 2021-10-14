import flask
from flask import jsonify
from firestore import getUser, getAllUsers, makeShop
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def getAllUsersRoute():
    data = getAllUsers()
    return jsonify(data);

@app.route('/get/user/<page_id>', methods=['GET'])
def getUserIdRoute(page_id):
    user = getUser(page_id)
    return jsonify(user)

@app.route('/post/user/<user_id>/shop/<shop_name>', methods=['POST'])
def makeShopRoute(user_id, shop_name):
    makeShop(user_id, shop_name)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


app.run()