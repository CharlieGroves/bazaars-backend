# import the api library
import flask
# import some specific functions from the api library
from flask import jsonify, request

# import the cross-origin resource sharing manager
from flask_cors import CORS

# import json file handler
import json

# import my own functions from firestore.py
from firestore import createUser, getAllShops, getShopWithName, getUser, getAllUsers, makeShop, getShopsWithId, createNewItem, getItems, getAllItems, getItem


# initilise the app
app = flask.Flask(__name__)

# allow cross-origin resource sharing
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# open json file with all errors in
with open("./errors.json") as json_file:
    errors = json.load(json_file)


@app.route('/get', methods=['GET'])
# get all users
def getAllUsersRoute():
    data = getAllUsers()
    return jsonify(data)


@app.route('/get/user/<user_id>', methods=['GET'])
# get user with id
def getUserIdRoute(user_id):
    user = getUser(user_id)
    return jsonify(user)


@app.route('/get/shop/name/<shop_name>', methods=['GET'])
# get shop with name
def getShopWithNameRoute(shop_name):
    shop = getShopWithName(shop_name)
    return jsonify(shop)


@app.route('/get/shop/id/<id>', methods=['GET'])
# get all shops that a manager owns
def getShopsWithIdRoute(id):
    shop = getShopsWithId(id)
    return jsonify(shop)


@app.route("/get/all-shops", methods=['GET'])
# get all shops
def getAllShopsRoute():
    shops = getAllShops()
    return jsonify(shops)


@app.route('/post/newshop', methods=['POST'])
# make a new shop
def makeShopRoute():

    data = request.get_json()

    owner_id = data["owner_id"]
    shop_name = data["shop_name"]
    shop_description = data["shop_description"]
    createdAt = data["createdAt"]
    if makeShop(owner_id, shop_name, shop_description, createdAt) == 0:
        return json.dumps({"error": errors["0"]}), 409, {'ContentType': 'application/json'}
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/post/newuser', methods=['POST'])
# make a new user
def makeUserRoute():

    data = request.get_json()

    id = data["id"]
    username = data["username"]
    url = data["url"]
    photoURL = data["photoURL"]
    createdAt = data["createdAt"]
    admin = data = ["admin"]

    createUser(id, username, url, photoURL, createdAt, admin)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/post/newitem', methods=['POST'])
# make a new item in a shop
def makeItemRoute():
    data = request.get_json()

    itemName = data["itemName"]
    itemPrice = data["itemPrice"]
    itemDescription= data["itemDescription"]
    itemImageURL = data["itemImageURL"]
    shopName = data["shopName"]
    createdAt = data["createdAt"]
    staffId = data["staffId"]
    tags = data["tags"]
    category = data["category"]
    sellerId = data["staffId"]


    createNewItem(itemName, itemPrice, itemDescription, itemImageURL,
                  shopName, createdAt, staffId, tags, category, sellerId)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/get/item/<shop_name>', methods=['GET'])
# get a shop from its id
def getItemsRoute(shop_name):
    items = getItems(shop_name)
    return jsonify(items)

@app.route('/get/all/items', methods=['GET'])
# get all items
def getAllItemsRoute():
    items = getAllItems()
    return jsonify(items)

@app.route('/get/single-item/<item_id>', methods=['GET'])
# get information about a single item
def getSingleItemRoute(item_id):
    print([item_id])
    item = getItem(item_id)
    return jsonify(item)

# if file is file being run
if __name__ == '__main__':
    # start the server on port 9000
    app.run(debug=True, host="0.0.0.0", port=9000, threaded=True)
