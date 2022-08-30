import pymongo
from parametros import *
# from Models import Models.item
from bson.objectid import ObjectId
from pymongo import MongoClient
from random import randint

client =  pymongo.MongoClient(servidor)
db = client['rpg-db']
collection = db.Creatures

# item = Item
# item.itemName = "Olympus sword"
# item.weight = 90

# itemObj = {
#             "region_name" : "Goblin\'s forest",
#             "level_range" : {
#                 "min_level" : 0,
#                 "max_level" : 7
#             },
#             "description" : "A beultiful forest full of goblins"            
#         }

document = collection.find_one({'_id' : ObjectId("609c835b27efee118d146559")})

itemObjs = []

for x in range(100):
    itemObjs += [
        {
            "creature_name" : "Adorable Goblin %s" %(x),
            "creature_level" : randint(0,7),
            "locations" : ObjectId("609c835b27efee118d146559"),
            "stats" : {
                "max_hp" :randint(10, 100),
                "max_res" :randint(0,300),
                "max_mana":randint(0,300),
            },
        }   
    ]

# print(itemObjs)

itemsCo_id = collection.insert_many(itemObjs) #.inserted_id
print(itemsCo_id)