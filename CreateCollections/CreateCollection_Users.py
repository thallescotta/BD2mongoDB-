import pymongo
from parametros import *
from pymongo import MongoClient
from collections import OrderedDict

client =  pymongo.MongoClient(servidor)
db = client['rpg-db']

db.Users.drop()

db.create_collection("Users")

vexpr = { "$jsonSchema": 
            {
                "bsonType":"object",
                "required": ["email","username", "password", "cash"],
                "properties":{
                    "email": {
                        "bsonType" : "string",
                        "description":"must be a string and is required"
                    },
                    "username": {
                        "bsonType" : "string",
                        "description":"must be a string and is required"
                    },
                    "password": {
                        "bsonType" : "string",
                        "description":"must be a string and is required"
                    },
                    "cash": {
                        "bsonType" : "number",
                        "description":"must be a number and is required"
                    }
                }
            }
        }

cmd = OrderedDict([('collMod', 'Users'),
                ('validator', vexpr),
                ('validationLevel', 'moderate')])

db.Users.create_index([("email", 1)], unique = True)
db.Users.create_index([("username", 1)], unique = True)

db.command(cmd)