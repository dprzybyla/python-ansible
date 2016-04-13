#!/usr/bin/env python
'''
Using ciscoconfparse find the crypto maps that are not using AES (based-on the
transform set name). Print these entries and their corresponding transform set
name.
'''

import re
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")
crypto = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")

print "\nCrypto maps not using AES:"

for i in crypto:
    print "  " + i.text
    for child in i.children:
        if 'transform' in child.text:
            match = re.search(r"set transform-set (.*)$", child.text)
            encryption = match.group(1)
    print
    print "Transform-set: " + encryption

print '\n'
