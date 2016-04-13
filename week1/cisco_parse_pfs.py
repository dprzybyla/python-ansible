#!/usr/bin/env python
'''
Use the ciscoconfparse library to find the crypto maps that are using pfs group2
'''

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
crypto = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")

print '\n'

for i in crypto:
    print i.text
    for child in i.children:
        print child.text

print '\n'
