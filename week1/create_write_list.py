#!/usr/bin/env python
'''
Write a Python program that creates a list. One of the elements of the list
should be a dictionary with at least two keys. Write this list out to a file
using both YAML and JSON formats. The YAML file should be in the expanded form.
'''

import yaml
import json

yaml_file = 'test_list.yml'
json_file = 'test_list.json'

test_dict = {
    'Big_Ring': '53',
    'Small_Ring': '39',
    'Chain': 'KMC',
    'Model': 'Litespeed'
}

test_list = [
    'Cassette',
    11,
    23,
    test_dict,
    'SRAM RED22',
]

with open(yaml_file, "w") as f:
    f.write(yaml.dump(test_list, default_flow_style=False))

with open(json_file, "w") as f:
    json.dump(test_list, f)

