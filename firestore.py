# import database management and authentication modules
from emails import sendRecommendationEmail
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime

from recombee_recommend import recommendUser

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


def createUser(uid, username, url, photoURL, createdAt, admin):
    user_ref = db.collection('users').document(uid)
    data = {
        "id": uid,
        "username": username,
        "url": url,
        "photoURL": photoURL,
        "createdAt": createdAt,
        "admin": admin,
    }
    # add this json object to the database
    return user_ref.set(data)

# create a new item in a shop


def createNewItem(itemName, itemPrice, itemDescription, itemImageURL, shopName, createdAt, staffId, tags, category, sellerId):
    item_ref = db.collection('items').document(itemName)
    item = {
        "itemName": itemName,
        "itemPrice": itemPrice,
        "itemDescription": itemDescription,
        "itemImageURL": itemImageURL,
        "shopName": shopName,
        "createdAt": createdAt,
        "staffId": staffId,
        "tags": tags,
        "category": category,
        "sellerId": sellerId,
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

# get a single item


def getItem(item_id):
    item_ref = db.collection('items').document(item_id)
    print(item_ref)
    item = item_ref.get()
    print(item.to_dict())
    return (item.to_dict())


def searchForItems(query):
    print(query)
    items_ref = db.collection('items').where(
        "tags", "array_contains_any", [query])
    items = []
    all_items = items_ref.stream()
    for item in all_items:
        items.append(item.to_dict())
    return (items)


def searchForItemsAsc(query):
    print(query)
    items_ref = db.collection('items').where(
        "tags", "array_contains_any", [query]).order_by("itemPrice", 
         direction=firestore.Query.ASCENDING).limit(30)
    items = []
    all_items = items_ref.stream()
    for item in all_items:
        items.append(item.to_dict())
    return (items)
 
def searchForItemsDsc(query):
    print(query)
    items_ref = db.collection('items').where(
        "tags", "array_contains_any", [query]).order_by("itemPrice", 
        direction=firestore.Query.DESCENDING).limit(30)
    items = []
    all_items = items_ref.stream()
    for item in all_items:
        items.append(item.to_dict())
    return (items)


def createNewReview(ReviewTitle, ReviewText, ReviewRating, UserID, ProductID,):
    # reference to item reviews in database
    review_ref = db.collection('items').document(
        ProductID).collection('reviews')
    # creating review object to add to review_ref
    review = {
        "ReviewTitle": ReviewTitle,
        "ReviewText": ReviewText,
        "ReviewRating": ReviewRating,
        "UserID": UserID,
        "ProductID": ProductID,
    }
    # adding review object to review_ref
    review_ref.add(review)
    # once it has been added, pull down all reviews for the product
    reviews = review_ref.stream()
    # define variables to be used to calculate mean rating
    ratings = 0
    all_reviews = []
    r_counter = 0

    # for every reference to a review in all reviews, pull down the actual data
    # and increment the counter
    for r in reviews:
        all_reviews.append(r.to_dict())
        r_counter += 1

    # now add up all of the ratings
    for rate in all_reviews:
        ratings += (rate["ReviewRating"])

    # divide the total rating by the number of ratings to get the mean average
    mean_rating = ratings/r_counter

    # add this information to the database on the item document
    db.collection('items').document(ProductID).set({
        "MeanRating": mean_rating,
    }, merge=True)


def getReviewsForItem(ProductID):
    reviews_ref = db.collection('items').document(
        ProductID).collection('reviews')
    reviews = []
    all_reviews = reviews_ref.stream()
    for review in all_reviews:
        reviews.append(review.to_dict())
    return (reviews)


def updateShoppingCart(user_id, cart):
    # update a shopping cart
    shoppingCart_ref = db.collection('users').document(user_id)
    print(cart)
    shoppingCart_ref.set({
        "cart": cart,
    }, merge=True)
    return


def getShoppingCart(user_id):
    # get a shopping cart
    shoppingCart_ref = db.collection('users').document(user_id)
    user = shoppingCart_ref.get()
    user_data = user.to_dict()
    cart = user_data["cart"]
    return cart


def get30Items():
    items = []
    items_ref = items_ref = db.collection('items')
    query = items_ref.order_by("createdAt").limit_to_last(30)
    all_items = query.get()
    for item in all_items:
        items.append(item.to_dict())
    return items


def itemSale(shop_id, item_id):
    # initilise variables
    item_sales = 0 
    shop_sales = 0
    shop_sales_revenue = 0

    # get shop data and item data using functions I wrote earlier
    item_data = getItem(item_id)
    shop_data = getShopWithName(shop_id)

    # define a reference to the shop and the item in the database
    item_ref = db.collection('items').document(item_id)
    shop_ref = db.collection('shops').document(shop_id)

    # get the current month as a number in a string
    currentMonth = str(datetime.now().month)

    # if the item/shop has had sales, update the variables
    if("sales" in shop_data):
        shop_sales = shop_data["sales"][currentMonth]

    if("sales_revenue" in shop_data):
        shop_sales_revenue = shop_data["sales_revenue"][currentMonth]

    if("sales" in item_data):
        item_sales = item_data["sales"][currentMonth]

    # update information in database
    shop_ref.set({
        "sales": {
            currentMonth: shop_sales + 1
        },
        "sales_revenue": {
            currentMonth: shop_sales_revenue + item_data["itemPrice"]
        }
    }, merge=True)

    item_ref.set({
        "sales": {
            currentMonth: item_sales + 1
        }
    }, merge=True)

def bestItem(shop_id):
    items = []
    items_ref = db.collection('items').where("shopName", "==", shop_id).order_by('sales', direction=firestore.Query.ASCENDING)
    all_items = items_ref.get()
    for item in all_items:
        items.append(item.to_dict())
    print(items)
    return items

def worstItem(shop_id):
    items = []
    items_ref = db.collection('items').where("shopName", "==", shop_id).order_by('sales', direction=firestore.Query.DESCENDING).limit_to_last(1)
    all_items = items_ref.get()
    for item in all_items:
        items.append(item.to_dict())
    return items

def itemPurchase(user_id, item_id, shop_id):
    sales_ref = db.collection('sales')
    sales_ref.add({
        "shop": shop_id,
        "item": item_id,
        "user": user_id
    })

def getSalesFromShop(shop_id):
    sales = []
    sales_ref = db.collection('sales').where("shop", "==", shop_id)
    all_sales = sales_ref.get()
    for sale in all_sales:
        sales.append(sale.to_dict())
    return sales

def recommendShop(shop_id, percentage):
    sales = getSalesFromShop(shop_id)
    for sale in sales:
        user = sale["user"]
        # create reference to that user in the database
        user_ref = db.collection('users').document(user)
        # get the data in this document
        user = user_ref.get()
        # return the user
        user_info = user.to_dict()
        print(user_info)
        item = recommendUser(user)
        sendRecommendationEmail("charlie.groves@coopersschool.com", item, percentage)