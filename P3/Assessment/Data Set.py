CT_osm = "C:/Github/DataAnalystNanodegree\P3/Assessment/CT-sample.osm"

import xml.etree.cElementTree as ET
import re
import codecs
import json



lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
is_address = re.compile(r'(addr:).*')

CREATED = ["version", "changeset", "timestamp", "user", "uid"]


def shape_element(element):
    node = {'created': {}, 'address': {}, 'pos': {}, 'node_refs': {}}

    if element.tag == "node" or element.tag == "way":
        for n in element.attrib:
            if n in CREATED:
                node['created'][n] = element.attrib[n]
            if n in ['lat', 'lon']:
                node['pos'] = [float(element.attrib['lat']), float(element.attrib['lon'])]
            if n not in CREATED and n not in ['lat', 'lon']:
                node[n] = element.attrib[n]
            node['type'] = element.tag

        for tag in element.iter("tag"):
            if is_address.search(tag.attrib['k']):
                if tag.attrib['k'].count(":") > 1:
                    pass
                else:
                    node['address'][re.sub('addr:','',tag.attrib['k'])] = tag.attrib['v']
            else:
                node[tag.attrib['k']] = tag.attrib['v']

        if element.tag == 'way':
            ref_set = []
            for ref in element.iter("nd"):
                ref_set.append(ref.attrib['ref'])
            node['node_refs'] = ref_set

        if len(node['address']) == 0:
            node.pop('address')
        if len(node['pos']) == 0:
            node.pop('pos')
        if len(node['node_refs']) == 0:
            node.pop('node_refs')

        return node
    else:
        return None


def process_map(file_in, pretty=False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2) + "\n")
                else:
                    fo.write(json.dumps(el) + "\n")


    return data



data = process_map(CT_osm, True)

