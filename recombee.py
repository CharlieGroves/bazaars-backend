from xml.etree.ElementTree import tostring
from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *
import pandas as pd
import time

private_token = "fV0h1ZTMpkULxiUBBFVndsqHMhfIHc8kBDts0kJJcbjrvMLcBpfDVZx8LxAAYt9X"

client = RecombeeClient('charlie-groves-dev', private_token)

df = pd.read_csv('dataset.csv',nrows=835,encoding="ISO-8859-1")

client.send(AddUser("id"))

# for x in range (0,834):
#     itemName = df["itemName"][x]
#     itemPrice = df["itemPrice"][x]
#     itemDescription = df["itemDescription"][x]
#     itemImageURL = df["itemImageURL"][x]
#     shopName = df["sellerId"][x]
#     createdAt = int(time.time())
#     staffId = df["sellerId"][x]
#     tags = df["tags"][x]
#     category = df["category"][x]
#     sellerId = df["sellerId"][x]
#     MeanRating = df["MeanRating"][x]

#     problem_chars = [" ", "'", ",", "(", ")", "*", "+", "&", "â", "¢", ";", "[", "]", "!", "Â", "®", "~", "€", "±", "â",]

#     itemNameSanitised = itemName

#     for char in problem_chars:
#       itemNameSanitised.replace(char, "")

#     itemNameSanitised = itemName.replace(" ", "")
#     itemNameSanitised = itemNameSanitised.replace("'", "")
#     itemNameSanitised = itemNameSanitised.replace(",", "")
#     itemNameSanitised = itemNameSanitised.replace("(", "")
#     itemNameSanitised = itemNameSanitised.replace(")" ,"")
#     itemNameSanitised = itemNameSanitised.replace("*" ,"")
#     itemNameSanitised = itemNameSanitised.replace("+" ,"")
#     itemNameSanitised = itemNameSanitised.replace("&" ,"")
#     itemNameSanitised = itemNameSanitised.replace("â" ,"")
#     itemNameSanitised = itemNameSanitised.replace("¢" ,"")
#     itemNameSanitised = itemNameSanitised.replace(";" ,"")
#     itemNameSanitised = itemNameSanitised.replace("[" ,"")
#     itemNameSanitised = itemNameSanitised.replace("]","")
#     itemNameSanitised = itemNameSanitised.replace("!","")
#     itemNameSanitised = itemNameSanitised.replace("Â","")
#     itemNameSanitised = itemNameSanitised.replace("®","")
#     itemNameSanitised = itemNameSanitised.replace("~","")
#     itemNameSanitised = itemNameSanitised.replace("€","")
#     itemNameSanitised = itemNameSanitised.replace("±","")
#     itemNameSanitised = itemNameSanitised.replace("â","")
    
#     client.send(SetItemValues(itemNameSanitised,
#         {
#           "MeanRating": int(MeanRating),
#           "category": category,
#           "createdAt": createdAt,
#           "itemDescription": itemDescription,
#           "itemImageURL": itemImageURL,
#           "itemName": itemName,
#           "itemPrice": int(itemPrice),
#           "sellerId": sellerId,
#           "staffId": staffId,
#           "tags": tags,
#         },
#         cascade_create=True
#     ))

#     print("Item " ,x, " added")