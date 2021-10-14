import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('cred/shop-builder-dev-firebase-adminsdk-tgh0r-9e9be1f435.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def getAllUsers():
    users = []
    users_ref = db.collection('users')
    all_users = users_ref.stream()
    for user in all_users:
        users.append(user.to_dict())
    return (users)

def getUser(uid):
    user_ref = db.collection('users').document(uid)
    user = user_ref.get()
    return (user.to_dict())

def makeShop(user_id, shop_name):
    shop_ref = db.collection('shops').document(shop_name)
    shop = shop_ref.get()
    if shop.exists:
        raise Exception("Shop already exists")
    data = {
        "shop_name": shop_name,
        "owner_id": user_id,
    }
    shop_ref.set(data)
    return 

getUser("QMKon2v385TLlFwkxGgzc0Il7x52")

#getUsers()