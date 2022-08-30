import pymongo
from parametros import servidor
from pymongo import MongoClient
from collections import OrderedDict

client =  pymongo.MongoClient(servidor)
db = client['rpg-db']

db.Creatures.drop()

db.create_collection("Creatures")

vexpr = { "$jsonSchema": 
            {
                "bsonType":"object",
                "required": ["creature_name", "creature_level", "stats", "locations"],
                "properties":{
                    "creature_name" : {
                        "bsonType" : "string",
                        "maxLength" : 45
                    },
                    "creature_level" : {
                        "bsonType" : "number",
                        "maximum" : 100
                    },
                    "locations" : {
                        "bsonType" : [ "objectId" ],
                    },
                    "drop_items" : {
                        "bsonType" : [ "objectId" ],
                    },
                    "stats" : {
                        "bsonType":"object",
                        "required": ["max_hp", "max_res", "max_mana"],
                        "properties": {
                            "max_hp" : {
                                "bsonType" : "int",
                                "maximum" : 10000
                            },
                            "max_res" : {
                                "bsonType" : "int",
                                "maximum" : 4000
                            },
                            "max_mana" : {
                                "bsonType" : "int",
                                "maximum" : 2000
                            }
                        }
                    },
                }
            }
        }

cmd = OrderedDict([('collMod', 'Creatures'),
                ('validator', vexpr),
                ('validationLevel', 'moderate')])

db.command(cmd)