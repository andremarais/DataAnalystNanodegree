import xml.etree.cElementTree as ET
from collections import defaultdict
import pprint

CT_osm = 'CT-sample.osm'
tags = defaultdict(int)

def count_tags(filename):
    for value, elm in ET.iterparse(CT_osm):
        m = elm.tag
        tags[m] += 1
    return tags

tags_ = count_tags(CT_osm)
pprint.pprint(tags_)

"""
{'node': 96974,
'nd': 120433,
'member': 2471,
'tag': 43426,
'relation': 234,
'way': 17247,
'osm': 1})

tags are quite similar to the chicago data. will look into nodes and ways.
looking at a subset of the sample, ways seem to refer to highways
relation doesn't seem to have data of a uniform nature. It refers to malls, boundaries and traffic rules

"""

