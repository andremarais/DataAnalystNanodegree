#!/usr/bin/env python
"""
In an earlier exercise we looked at the cities dataset and asked which region in India contains
the most cities. In this exercise, we'd like you to answer a related question regarding regions in
India. What is the average city population for a region in India? Calculate your answer by first
finding the average population of cities in each region and then by calculating the average of the
regional averages.


"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ ]
    return pipeline

def aggregate(db, pipeline):
    return [doc for doc in db.cities.aggregate(pipeline)]


if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result) == 1
    # Your result should be close to the value after the minus sign.
    assert abs(result[0]["avg"] - 196025.97814809752) < 10 ** -8
    import pprint
    pprint.pprint(result)
