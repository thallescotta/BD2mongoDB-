import pymongo
from parametros import *
# from Models import Item
from pymongo import MongoClient

client =  pymongo.MongoClient(servidor)
db = client['rpg-db']
itemsCo = db.users

# item = Item
# item.itemName = "Olympus sword"
# item.weight = 90

itemObjs = [{"username" : "dolugas",
            "password" : "dolugas123"}]

itemsCo_id = itemsCo.insert_many(itemObjs)
print(itemsCo_id)