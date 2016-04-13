#!/usr/bin/env python
'''
Write a Python program that reads both the YAML file and the JSON file created
in exercise6 and pretty prints the data structure that is returned.
'''

import yaml
import json

from pprint import pprint

yaml_file = 'test_list.yml'
json_file = 'test_list.json'


with open(yaml_file) as f:
    new_ylist = yaml.load(f)

with open(json_file) as f:
    new_jlist = json.load(f)

print "---YAML---"
pprint(new_ylist, width=1)
print '\n'
print "---JSON---"
pprint(new_jlist, width=1)
print '\n'

