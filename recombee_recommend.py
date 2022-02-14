from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

private_token = "fV0h1ZTMpkULxiUBBFVndsqHMhfIHc8kBDts0kJJcbjrvMLcBpfDVZx8LxAAYt9X"

client = RecombeeClient('charlie-groves-dev', private_token)

def sanitiseItemName(itemName):
    itemNameSanitised = itemName.replace(" ", "")
    itemNameSanitised = itemNameSanitised.replace("'", "")
    itemNameSanitised = itemNameSanitised.replace(",", "")
    itemNameSanitised = itemNameSanitised.replace("(", "")
    itemNameSanitised = itemNameSanitised.replace(")" ,"")
    itemNameSanitised = itemNameSanitised.replace("*" ,"")
    itemNameSanitised = itemNameSanitised.replace("+" ,"")
    itemNameSanitised = itemNameSanitised.replace("&" ,"")
    itemNameSanitised = itemNameSanitised.replace("â" ,"")
    itemNameSanitised = itemNameSanitised.replace("¢" ,"")
    itemNameSanitised = itemNameSanitised.replace(";" ,"")
    itemNameSanitised = itemNameSanitised.replace("[" ,"")
    itemNameSanitised = itemNameSanitised.replace("]","")
    itemNameSanitised = itemNameSanitised.replace("!","")
    itemNameSanitised = itemNameSanitised.replace("Â","")
    itemNameSanitised = itemNameSanitised.replace("®","")
    itemNameSanitised = itemNameSanitised.replace("~","")
    itemNameSanitised = itemNameSanitised.replace("€","")
    itemNameSanitised = itemNameSanitised.replace("±","")
    itemNameSanitised = itemNameSanitised.replace("â","")
    return itemNameSanitised


def recommendItemItem(itemName):
    itemNameSanitised = sanitiseItemName(itemName)
    temp = client.send(RecommendItemsToItem(itemNameSanitised, None, 5, scenario='test', return_properties=True))
    return temp

def recommendItemHomepage():
    result = client.send(RecommendItemsToUser('id', 15, return_properties=True))
    return result

def userItemInteraction(user_id, item_id):
    itemNameSanitised = sanitiseItemName(item_id)
    client.send(AddDetailView(user_id, itemNameSanitised))

def recommendUser(user_id):
    #client.send(AddUser(user_id))
    print(user_id)
    user_id = str(user_id)
    item = client.send(RecommendItemsToUser("9beRKaPEJySsCLfNRaIehqVJIme2", 1, return_properties=True))
    return item