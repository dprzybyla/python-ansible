#!/usr/bin/env python
'''
Write a Python program using ciscoconfparse that parses the 'cisco_ipsec.txt'
config file. Note, this config file is not fully valid (i.e. parts of the
configuration are missing).
The script should find all of the crypto map entries in the file (lines that
begin with 'crypto map CRYPTO') and print out the children of each crypto map.
'''

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
print '\n'
print cisco_cfg
print '\n'

crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")
print crypto
print '\n'

for i in crypto:
    print i.text
    for child in i.children:
        print child.text

print '\n'
