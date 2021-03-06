#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it, clean it,
come up with a data model, insert it into a MongoDB and then run some queries against your database.
The set contains data about Arachnid class.
Your task in this exercise is to parse the file, process only the fields that are listed in the
FIELDS dictionary as keys, and return a list of dictionaries of cleaned values.

The following things should be done:
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
- if a value of a field is "NULL", convert it to None
- if there is a value in 'synonym', it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the cleanup is up to you,
  eg removing "*" prefixes etc. If there is a singular synonym, the value should still be formatted
  in a list.
- strip leading and ending whitespace from all fields, if there is any
- the output structure should be as follows:
{ 'label': 'Argiope',
  'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
  'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
  'name': 'Argiope',
  'synonym': ["One", "Two"],
  'classification': {
                    'family': 'Orb-weaver spider',
                    'class': 'Arachnid',
                    'phylum': 'Arthropod',
                    'order': 'Spider',
                    'kingdom': 'Animal',
                    'genus': None
                    }
}
  * Note that the value associated with the classification key is a dictionary with
    taxonomic labels.
"""
import codecs
import csv
import json
import pprint
import re
import numpy as np

DATAFILE = 'C:/Github/DataAnalystNanodegree/P3/Lesson4PS1/arachnid.csv'
FIELDS ={'rdf-schema#label': 'label',
         'URI': 'uri',
         'rdf-schema#comment': 'description',
         'synonym': 'synonym',
         'name': 'name',
         'family_label': 'family',
         'class_label': 'class',
         'phylum_label': 'phylum',
         'order_label': 'order',
         'kingdom_label': 'kingdom',
         'genus_label': 'genus'}


# trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
def clean_label(old_label):
    new_label = re.sub(r'\(.*?\)','', old_label)
    return str.strip(new_label)


# if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
def clean_name(old_name, label):
    if old_name == "NULL" or str.isalnum(old_name) is not True:
        return str.strip(label)
    else:
        return str.strip(old_name)


# synonyms to list
def synonyms(old_syn):
    if old_syn == 'NULL':
        return None
    new_syn = re.sub('{|}', '',  old_syn)
    new_syn = re.sub('\*', '',  old_syn)
    new_syn = str.split(new_syn, "|")
    # print old_syn, '|', new_syn
    return new_syn

def remNull(v):
    if v == "NULL":
        return None

def process_file(filename, fields):
    process_fields = fields.keys()
    data = []
    new_data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:
            data.append({value: line[key] for key, value in fields.items()})
            pass

        for d in data:
            new_line = []
            # label cleaner
            d['label'] = clean_label(d['label'])
            # name cleaner
            d['name'] = clean_name(d['name'], d['label'])
            # replaces NULL with None
            d['synonym'] = synonyms(d['synonym'])

            for g in d.keys():
                if d[g] == 'NULL':
                    d[g] = None
                pass

            d["classification"] = {}  # initiate an empty dictionary
            for s_key in ["kingdom", "family", "order", 'phylum', 'genus', 'class']:
                d["classification"][s_key] = d[s_key]  # fill the new dict
                d.pop(s_key)  # remove the old keys
            new_data.append(d)



    return new_data



def test():
    data = process_file(DATAFILE, FIELDS)
    print "Your first entry:"
    pprint.pprint(data[0])
    first_entry = {
        "synonym": None,
        "name": "Argiope",
        "classification": {
            "kingdom": "Animal",
            "family": "Orb-weaver spider",
            "order": "Spider",
            "phylum": "Arthropod",
            "genus": None,
            "class": "Arachnid"
        },
        "uri": "http://dbpedia.org/resource/Argiope_(spider)",
        "label": "Argiope",
        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]


a = process_file(DATAFILE, FIELDS)


test()
# pprint.pprint(a[0])

# pprint.pprint(a[0])
# first_entry = {
#     "synonym": None,
#     "name": "Argiope",
#     "classification": {
#         "kingdom": "Animal",
#         "family": "Orb-weaver spider",
#         "order": "Spider",
#         "phylum": "Arthropod",
#         "genus": None,
#         "class": "Arachnid"
#     }}
#
# pprint.pprint(first_entry)