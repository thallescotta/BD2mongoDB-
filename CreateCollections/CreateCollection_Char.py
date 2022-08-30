import pymongo
from parametros import *
from pymongo import MongoClient
from collections import OrderedDict

client =  pymongo.MongoClient(servidor)
db = client['rpg-db']

db.Chars.drop()

db.create_collection("Chars")

vexpr = { "$jsonSchema": 
            {
                "bsonType":"object",
                "required": ["nickname","stats","last_region_id","user_id","coins","race_type","items_id"],
                "properties":{
                    "nickname": {
                        "bsonType" : "string",
                        "description":"must be a string and is required"
                    },
                    "stats": {
                        "bsonType" : "object",
                        "required" : ["char_level","base_hp","base_res","base_mana","max_strength","max_weight"],
                        "properties":{
                            "char_level": {
                                "bsonType" : "number",
                                "maximum" : 100,
                                "minimum" : 0,
                                "description":"must be an integer and is required"
                            },
                            "base_hp": {
                                "bsonType" : "number",
                                "maximum" : 1000,
                                "minimum" : 0,
                                "description":"must be an integer and is required"
                            },
                            "base_res": {
                                "bsonType" : "number",
                                "maximum" : 1000,
                                "minimum" : 0,
                                "description":"must be an integer and is required"
                            },
                            "base_mana": {
                                "bsonType" : "number",
                                "maximum" : 2000,
                                "minimum" : 0,
                                "description":"must be an integer and is required"
                            },
                            "max_strength": {
                                "bsonType" : "number",
                                "maximum" : 100,
                                "minimum" : 0,
                                "description":"must be a float and is required"
                            },
                            "max_weight": {
                                "bsonType" : "number",
                                "maximum" : 130,
                                "minimum" : 0,
                                "description":"must be a float and is required"
                            }
                        }
                    },
                    "last_region_id": {
                        "bsonType" : "object",
                        "description":"must be an id and is required"
                    },
                    "user_id": {
                        "bsonType" : "object",
                        "description":"must be an id and is required"
                    },
                    "coins": {
                        "bsonType" : "number",
                        "description":"must be a float and is required"
                    },
                    "race_types": {
                        "enum": ["Fairies","Elves","Demons"],
                        "description":"must be a string and is required"
                    },
                    "demoniac_breath": {
                        "bsonType" : "number",
                        "description":"must be a number"
                    },
                    "max_speed_flying": {
                        "bsonType" : "number",
                        "description":"must be a number"
                    },
                    "dark_vision_increment": {
                        "bsonType" : "number",
                        "description":"must be a number"
                    },
                    "items_id": {
                        "bsonType" : ["object"],
                        "description":"must be an id and is required"
                    }
                }
            }
        }

cmd = OrderedDict([('collMod', 'Chars'),
                ('validator', vexpr),
                ('validationLevel', 'moderate')])
db.users.create_index([("nickname", 1)], unique = True)

db.command(cmd)