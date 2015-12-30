#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    return


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if 'user' in element.attrib:
            u = element.attrib['user']
            users.add(u)
        pass

    return users


def test():

    users = process_map('C:/Github/DataAnalystNanodegree/P3/Lesson6/example3.osm')
    pprint.pprint(users)
    print len(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()