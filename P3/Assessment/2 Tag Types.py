import xml.etree.cElementTree as ET
import pprint
import re
from collections import defaultdict

CT_osm = 'CT-sample.osm'

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
        elem = element.attrib['k']

        l = lower.search(elem)
        lc = lower_colon.search(elem)
        pc = problemchars.search(elem)
        if l:
            keys['lower'] += 1

        if lc:
            keys['lower_colon'] += 1

        if pc:
            keys['problemchars'] += 1

        if not l and not lc and not pc:
            keys['other'] += 1

        pass
    return keys


def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys

