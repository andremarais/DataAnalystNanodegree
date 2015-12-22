from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")

db = client.example

def find():
    query = {"foundingDate" : {"$gte" : datetime(2000,1,1)}}