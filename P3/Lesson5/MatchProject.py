from pymongo import MongoClient
from pprint import pprint
import json


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db


def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$match" : {"user.time_zone" : "Brasilia",
                             "user.statuses_count" : {"$gt" : 100}}},
                {"$project" : {"followers" : "$user.followers_count",
                               "screen_name" : "$user.screen_name",
                               "tweets" : "$user.statuses_count"
                               }},
                {"$sort" : {"followers" : -1}},
                {"$limit" : 1}
                ]
    return pipeline


def aggregate(db, pipeline):
    return [doc for doc in db.twitter.aggregate(pipeline)]


db = get_db('twitter')
pipeline = make_pipeline()
result = aggregate(db, pipeline)
import pprint
pprint.pprint(result)
assert len(result) == 1
assert result[0]["followers"] == 17209


