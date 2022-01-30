import pandas as pd
import json
import time

from firestore import createNewItem

df = pd.read_csv('dataset.csv',nrows=835)

for x in range (0,834):
    itemName = df["itemName"][x]
    itemPrice = df["itemPrice"][x]
    itemDescription = df["itemDescription"][x]
    itemImageURL = df["itemImageURL"][x]
    shopName = df["sellerId"][x]
    createdAt = int(time.time())
    staffId = df["sellerId"][x]
    tags = df["tags"][x]
    category = df["category"][x]
    sellerId = df["sellerId"][x]

    tags = tags.split(',')
    
    createNewItem(itemName, itemPrice, itemDescription, itemImageURL, shopName, createdAt, staffId, tags, category, sellerId)
    print("created item ", x)