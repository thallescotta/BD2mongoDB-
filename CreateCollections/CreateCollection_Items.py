import pymongo
from parametros import *
from pymongo import MongoClient
from collections import OrderedDict

client =  pymongo.MongoClient(servidor)
db = client['rpg-db']

db.Items.drop()

db.create_collection("Items")

vexpr = { "$jsonSchema": 
            {
                "bsonType":"object",
                "required": ["name","equipable","consumable","weight","item_cost"],
                "properties":{
                    "name": {
                        "bsonType" : "string",
                        "description":"must be a string and is required"
                    },
                    "equipable": {
                        "bsonType" : "bool",
                        "description":"must be a boolean and is required"
                    },
                    "consumable": {
                        "bsonType" : "bool",
                        "description":"must be a boolean and is required"
                    },
                    "weight": {
                        "bsonType": "number",
                        "description":"must be an integer and is required"
                    },
                    "item_cost": {
                        "bsonType" : "number",
                        "description":"must be an integer and is required"
                    },
                    "improvement_types": {
                        "enum" : ["res","hp","mana","str"],
                        "description":"must be a string between 'res','hp','mana','str'"
                    },
                    "improvement_value": {
                        "bsonType" : "number",
                        "description":"must be a number"
                    }
                }
            }
        }

cmd = OrderedDict([('collMod', 'Items'),
                ('validator', vexpr),
                ('validationLevel', 'moderate')])

db.command(cmd)