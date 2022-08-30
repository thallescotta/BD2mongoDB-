import pymongo
from parametros import servidor
from pymongo import MongoClient
from collections import OrderedDict

client =  pymongo.MongoClient(servidor)
db = client['rpg-db']

db.Regions.drop()

db.create_collection("Regions")

vexpr = { "$jsonSchema": 
            {
                "bsonType":"object",
                "required": ["region_name", "level_range"],
                "properties":{
                    "region_name": {
                        "bsonType" : "string",
                        "maxLength" : 45,
                        "description":"must be a string and is required"
                    },
                    "description": {
                        "bsonType" : "string",
                        "maxLength" : 500 
                    },
                    "level_range": {
                        "bsonType" : "object",
                        "required" : ["min_level", "max_level"],
                        "properties" : {
                            "min_level" : {
                                "bsonType" : "int",
                                "minimum" : 0,
                                "description" : "Minimun player level to enter the region."
                            },
                            "max_level" : {
                                "bsonType" : "int",
                                "maximum" : 1000,
                                "description" : "Maximun"
                            }
                        }
                    }
                }
            }
        }

cmd = OrderedDict([('collMod', 'Regions'),
                ('validator', vexpr),
                ('validationLevel', 'moderate')])

db.command(cmd)