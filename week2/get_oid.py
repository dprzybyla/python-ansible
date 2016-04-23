#!/usr/bin/env python

# Write a script that connects to both routers (pynet-rtr1 and pynet-rtr2) 
# and prints out both the MIB2 sysName and sysDescr.

from snmp_helper import snmp_get_oid,snmp_extract

ip_addr = '50.76.53.27'
SNMP_PORT_RTR1 = 7961
SNMP_PORT_RTR2 = 8061
COMMUNITY_STRING = 'galileo'
SYSDESC = '1.3.6.1.2.1.1.1.0'
SYSNAME = '1.3.6.1.2.1.1.5.0'

def get_oid(ip_addr, COMMUNITY_STRING, SNMP_PORT, OID):
    a_device = (ip_addr, COMMUNITY_STRING, SNMP_PORT_RTR1)
    snmp_data = snmp_get_oid(a_device, oid=OID)
    output = snmp_extract(snmp_data)
    return output

def main():
    output = get_oid(ip_addr, COMMUNITY_STRING, SNMP_PORT_RTR1, SYSDESC) 
    print
    print "ROUTER 1 DESCRIPTION"
    print output

    output = get_oid(ip_addr, COMMUNITY_STRING, SNMP_PORT_RTR1, SYSNAME)
    print
    print "ROUTER 1 NAME"
    print output    

    output = get_oid(ip_addr, COMMUNITY_STRING, SNMP_PORT_RTR2, SYSDESC)
    print '\n'
    print "ROUTER 2 DESCRIPTION"
    print output

    output = get_oid(ip_addr, COMMUNITY_STRING, SNMP_PORT_RTR2, SYSNAME)
    print
    print "ROUTER 2 NAME"
    print output
    print

if __name__ == "__main__":
    main()

