import flask
from flask import jsonify, request
from firestore import getAllShops, getShop, getUser, getAllUsers, makeShop
import json

app = flask.Flask(__name__)

with open("./errors.json") as json_file:
    errors = json.load(json_file)

@app.route('/get', methods=['GET'])
def getAllUsersRoute():
    data = getAllUsers()
    return jsonify(data)

@app.route('/get/user/<user_id>', methods=['GET'])
def getUserIdRoute(user_id):
    user = getUser(user_id)
    return jsonify(user)

@app.route('/get/shop/<shop_name>', methods=['GET'])
def getShopRoute(shop_name):
    shop = getShop(shop_name);
    return jsonify(shop)

@app.route("/get/all-shops")
def getAllShopsRoute():
    shops = getAllShops()
    return jsonify(shops)

@app.route('/post/newshop', methods=['POST'])
def makeShopRoute():
    data = request.get_json()
    print(data["user_id"])
    user_id = data["user_id"]
    shop_name = data["shop_name"]
    if makeShop(user_id, shop_name) == 0:
       return json.dumps({"error": errors["0"]}), 409, {'ContentType':'application/json'}
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port=9000, threaded=True)


