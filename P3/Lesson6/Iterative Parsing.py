import xml.etree.cElementTree as ET
from collections import defaultdict


import pprint
tags = defaultdict(int)


def count_tags(filename):
    for value, elm in ET.iterparse(filename):
        m = elm.tag
        tags[m] += 1
    return tags


def test():
    tags = count_tags('C:/Github/DataAnalystNanodegree/P3/Lesson6/example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}

if __name__ == "__main__":
    test()