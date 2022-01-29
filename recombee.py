from recombee_api_client.api_client import RecombeeClient
from recombee_api_client.api_requests import *

private_token = "fV0h1ZTMpkULxiUBBFVndsqHMhfIHc8kBDts0kJJcbjrvMLcBpfDVZx8LxAAYt9X"

client = RecombeeClient('charlie-groves-dev', private_token)

client.send(SetItemValues('toilet',
    {
      "MeanRating": 100,
      "category": "bathroom",
      "createdAt": 2346223236,
      "itemDescription": "a golden toilet for your bathroom",
      "itemImageURL": "https://i.guim.co.uk/img/media/6babd768431f1b18e3daaabc3ff8c2e258dd67f5/1053_1195_4826_2896/master/4826.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=5e157e66df37f51722f6821d3ed7897a",
      "itemName": "golden toilet",
      "itemPrice": 229900,
      "sellerId": ";wiurevgw4gggg98qwergwerg34oign3lqwg",
      "staffId": ";eruv93f8ddseurgn-swergersg ergy9p8 eg",
      "tags": "['tag', 'toilet', 'gold', 'gold toilet']",
    },
    cascade_create=True
))