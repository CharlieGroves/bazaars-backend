# import the api library
import flask
# import some specific functions from the api library
from flask import jsonify, request

# import the cross-origin resource sharing manager
from flask_cors import CORS

# import json file handler
import json

# import my own functions from firestore.py
from firestore import createUser, getAllShops, getShopWithName, getUser, getAllUsers, makeShop, getShopsWithId, createNewItem, getItems, getAllItems, getItem, searchForItems, createNewReview, getReviewsForItem, updateShoppingCart, getShoppingCart, get30Items , itemSale, bestItem, worstItem
from recombee_recommend import recommendItemHomepage, recommendItemItem


# initilise the app
app = flask.Flask(__name__)

# allow cross-origin resource sharing
CORS(app)
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
    print(data)
    uid = data["id"]
    username = data["username"]
    url = data["url"]
    photoURL = data["photoURL"]
    createdAt = data["createdAt"]
    admin = data = ["admin"]

    createUser(uid, username, url, photoURL, createdAt, admin)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/post/newitem', methods=['POST'])
# make a new item in a shop
def makeItemRoute():
    data = request.get_json()

    itemName = data["itemName"]
    itemPrice = data["itemPrice"]
    itemDescription = data["itemDescription"]
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


@app.route('/get/search/item/<query>', methods=['GET'])
# get items from the database based on whether they satisfy the query
def searchForItemsRoute(query):
    data = searchForItems(query)
    return jsonify(data)


@app.route('/post/review', methods=['POST'])
# create a new review for an item
def createNewReviewRoute():
    data = request.get_json()

    ReviewTitle = data["ReviewTitle"]
    ReviewText = data["ReviewText"]
    ReviewRating = data["ReviewRating"]
    UserID = data["UserID"]
    ProductID = data["ProductID"]

    createNewReview(
        ReviewTitle,
        ReviewText,
        ReviewRating,
        UserID,
        ProductID,
    )

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/get/reviews/<item_id>')
def getReviewsForItemRoute(item_id):
    reviews = getReviewsForItem(item_id)
    return jsonify(reviews)


@app.route('/post/shoppingCart/<user_id>', methods=['POST'])
# update a shopping cart
def updateShoppingCartRoute(user_id):
    data = request.get_json()
    updateShoppingCart(user_id, data)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/get/shoppingCart/<user_id>')
# get a user's shopping cart
def getShoppingCartRoute(user_id):
    cart = getShoppingCart(user_id)
    return jsonify(cart)

@app.route('/get/30/items')
# get most recent 30 items
def get30ItemsRoute():
    items = get30Items()
    return jsonify(items)

@app.route('/recommend/item/item', methods=['POST'])
# get item recommendations 
def recommendItemItemRoute():
    data = request.get_json()
    item = data["itemName"]
    recommendations = recommendItemItem(item)
    return(jsonify(recommendations))

@app.route('/recommend/welcome', methods=['GET'])
# get items for homepage
def recommendItemHomepageRoute():
    recommendations = recommendItemHomepage()
    return(jsonify(recommendations))

@app.route('/post/sale/<shop_id>/<item_id>', methods=["POST"])
# record an item sale
def itemSaleRoute(shop_id, item_id):
    itemSale(shop_id, item_id)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/get/best/<shop_id>', methods=["GET"])
# get the best performing item from a shop
def bestItemRoute(shop_id):
    item = bestItem(shop_id)
    return(jsonify(item))

@app.route('/get/worst/<shop_id>', methods=["GET"])
# get the worst performing item from a shop
def worstItemRoute(shop_id):
    item = worstItem(shop_id)
    return(jsonify(item))

# if file is file being run
if __name__ == '__main__':
    # start the server on port 9000
    app.run(debug=True, host="0.0.0.0", port=9000, threaded=True)