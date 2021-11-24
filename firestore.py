# import database management and authentication modules
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# use a service account to have uninterrupted access to database
cred = credentials.Certificate(
    'cred/shop-builder-dev-firebase-adminsdk-tgh0r-9e9be1f435.json')
# authenticate the server as an admin
firebase_admin.initialize_app(cred)

# establish a connection to the database
db = firestore.client()

# get all users from the database
def getAllUsers():
    # set user arrary to empty
    users = []
    # create reference to users in database
    users_ref = db.collection('users')
    # get users from database using reference
    all_users = users_ref.stream()
    # loop through response
    for user in all_users:
        # add all users to users array
        users.append(user.to_dict())
    # return the array of users
    return (users)

# get a single user from their id
def getUser(uid):
    # create reference to that user in the database
    user_ref = db.collection('users').document(uid)
    # get the data in this document
    user = user_ref.get()
    # return the user
    return (user.to_dict())

# make a new shop
def makeShop(user_id, shop_name, shop_description, createdAt):
    # create reference to the shop in the database
    shop_ref = db.collection('shops').document(shop_name)
    # get current data from that location
    shop = shop_ref.get()
    # if the shop already exists, return 0 which is
    # an error because shop names have to be unique
    if shop.exists:
        return(0)
    # otherwise, make a json object with the shop name and the id of the owner of the shop
    data = {
        "shop_name": shop_name,
        "owner_id": user_id,
        "shop_description": shop_description,
        "createdAt": createdAt,
    }
    # add this json object to the database
    return shop_ref.set(data)

# get information about a shop with its name (which is unique)
def getShopWithName(shop_name):
    shop_ref = db.collection('shops').document(shop_name)
    shop = shop_ref.get()
    return (shop.to_dict())

# get all shops one manager owns using their id
def getShopsWithId(id):
    shops = []
    shops_ref = db.collection('shops').where('owner_id', '==', id)
    all_shops = shops_ref.stream()
    for shop in all_shops:
        shops.append(shop.to_dict())
    return (shops)

# get all shops in the database
def getAllShops():
    shops = []
    shops_ref = db.collection('shops')
    all_shops = shops_ref.stream()
    for shop in all_shops:
        shops.append(shop.to_dict())
    return (shops)

# create a user
def createUser(id, username, url, photoURL, createdAt, admin):
    user_ref = db.collection('users').document(id)
    data = {
        "id": id,
        "username": username,
        "url": url,
        "photoURL": photoURL,
        "createdAt": createdAt,
        "admin": admin,
    }
    # add this json object to the database
    return user_ref.set(data)

# create a new item in a shop
def createNewItem(itemName, itemPrice, itemImageURL, shopName, createdAt, staffId, tags, category):
    item_ref = db.collection('items').document(itemName)
    item = {
        "itemName": itemName, 
        "itemPrice": itemPrice,
        "itemImageURL": itemImageURL,
        "shopName": shopName,
        "createdAt": createdAt,
        "staffId": staffId,
        "tags": tags,
        "category": category,
    }
    return item_ref.set(item)

# get all items in a shop from the shop name (which is unique)
def getItems(shop_name):
    items = []
    items_ref = db.collection('items').where("shopName", "==", shop_name)
    all_items = items_ref.stream()
    for item in all_items:
        print(item.to_dict())
        items.append(item.to_dict())
    return (items)

# get all items
def getAllItems():
    items = []
    items_ref = db.collection('items')
    all_items = items_ref.stream()
    for item in all_items:
        items.append(item.to_dict())
    return (items)
    