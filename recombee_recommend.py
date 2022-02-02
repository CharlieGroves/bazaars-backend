from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

private_token = "fV0h1ZTMpkULxiUBBFVndsqHMhfIHc8kBDts0kJJcbjrvMLcBpfDVZx8LxAAYt9X"

client = RecombeeClient('charlie-groves-dev', private_token)

def recommendItemItem(itemName):
    # problem_chars = [" ", "'", ",", "(", ")", "*", "+", "&", "â", "¢", ";", "[", "]", "!", "Â", "®", "~", "€", "±", "â",]

    # itemNameSanitised = itemName

    # for char in problem_chars:
    #     itemNameSanitised.replace(char, "")
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

    print(itemNameSanitised)

    temp = client.send(RecommendItemsToItem(itemNameSanitised, None, 5, scenario='test', return_properties=True))
    print(temp)
    return temp
