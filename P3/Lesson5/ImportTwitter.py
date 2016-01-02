import pprint
import json
from pymongo import MongoClient


#import twitter data
client = MongoClient('localhost:27017')
db = client.twitter
infile = 'C:/Github/twitter2.json'
i = 0
with open(infile, 'rb') as json_file:
    for line in json_file:
        i += 1
        print line, '\n'
        if i > 5:
            break
'''
#import cities data
client = MongoClient('localhost:27017')
db = client.cities
infile = 'C:/Github/twitter2.json'
with open(infile, 'rb') as json_file:
    for line in json_file:
        db.twitter.insert(json.loads(line))
        pprint(json.loads(line))

'''