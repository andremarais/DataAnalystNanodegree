import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

CT_osm = "CT-sample.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons", "Way", "Close", "Crescent"]


mapping = { "St": "Street",
            "St.": "Street",
            "Ave" : "Avenue",
            'Rd.' : "Road",
            "st" : "Street"
            }

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types


def update_name(name, mapping):
    to_replace = street_type_re.search(name).group()
    if to_replace in mapping.keys():
        name = re.sub(to_replace,mapping.values()[mapping.keys().index(to_replace)], name)
    return name

street_types = audit(CT_osm)

pprint.pprint(dict(street_types))

