# import database management and authentication modules
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# use a service account to have uninterrupted access to database
cred = credentials.Certificate('cred/shop-builder-dev-firebase-adminsdk-tgh0r-9e9be1f435.json')
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
def makeShop(user_id, shop_name):
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
    }
    # add this json object to the database
    return shop_ref.set(data)

def getShop(shop_name):
    shop_ref = db.collection('shops').document(shop_name)
    shop = shop_ref.get()
    return (shop.to_dict())

def getAllShops():
    shops=[]
    shops_ref = db.collection('shops')
    all_shops = shops_ref.stream()
    for shop in all_shops:
        shops.append(shop.to_dict())
    return (shops)


getUser("QMKon2v385TLlFwkxGgzc0Il7x52")

#getUsers()