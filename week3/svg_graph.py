#!/usr/bin/env python

'''
Using SNMPv3 create two SVG image files.  

The first image file should graph the input and output octets on interface FA4 on pynet-rtr1 every five minutes for an hour.  Use the pygal library to create the SVG graph file. Note, you should be doing a subtraction here (i.e. the input/output octets transmitted during this five minute interval).  

The second SVG graph file should be the same as the first except graph the unicast packets received and transmitted.
'''

from snmp_helper import snmp_get_oid_v3,snmp_extract
import pygal
import time

ip_addr = '50.76.53.27'
snmp_port_rtr1 = 7961
user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

ifDescr_fa4 = '1.3.6.1.2.1.2.2.1.2.5'
ifInOctets_fa4 = '1.3.6.1.2.1.2.2.1.10.5'
ifInUcastPkts_fa4 = '1.3.6.1.2.1.2.2.1.11.5'
ifOutOctets_fa4 = '1.3.6.1.2.1.2.2.1.16.5'
ifOutUcastPkts_fa4 = '1.3.6.1.2.1.2.2.1.17.5'

def get_snmp (device, user, OID):
    snmp_data = snmp_get_oid_v3(device, user, oid=OID)
    output = snmp_extract(snmp_data)
    return output

def main():
    # Tuples used for counting loops.
    count12 = range(12)
    count13 = range(13)

    # Tuples that store data over an hour.
    in_octets = range(13)
    out_octets = range(13)
    in_unicast = range(13)
    out_unicast = range(13)

    # Tuples that store calculations from the data.
    in_octets_calc = range(12)
    out_octets_calc = range(12)
    in_unicast_calc = range(12)
    out_unicast_calc = range(12)

    # SNMP tuples.
    snmp_device = (ip_addr, snmp_port_rtr1)
    snmp_user = (user, auth_key, encrypt_key)

    # Collect data every five minutes for an hour.
    for i in count13:
        output = get_snmp(snmp_device, snmp_user, ifInOctets_fa4)
        in_octets[i] = output
        output = get_snmp(snmp_device, snmp_user, ifOutOctets_fa4)
        out_octets[i] = output
        output = get_snmp(snmp_device, snmp_user, ifInUcastPkts_fa4)
        in_unicast[i] = output
        output = get_snmp(snmp_device, snmp_user, ifOutUcastPkts_fa4)
        out_unicast[i] = output
        time.sleep(300)

    # Calculate octets and packets for each five minute interval.
    for i in count12:
        in_octets_calc[i] = float(in_octets[i+1]) - float(in_octets[i])
        out_octets_calc[i] = float(out_octets[i+1]) - float(out_octets[i])
        in_unicast_calc[i] = float(in_unicast[i+1]) - float(in_unicast[i])
        out_unicast_calc[i] = float(out_unicast[i+1]) - float(out_unicast[i])
    
    # Create the octet graph.
    octet_graph = pygal.Line()
    octet_graph.title = 'Input/Output Octets'
    octet_graph.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
    octet_graph.add('InOctets', in_octets_calc)
    octet_graph.add('OutOctets', out_octets_calc)
    octet_graph.render_to_file('octet_graph.svg')

    # Create the unicast packet graph.
    packet_graph = pygal.Line()
    packet_graph.title = 'Input/Output Unicast Packets'
    packet_graph.x_labels = ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60']
    packet_graph.add('InUnicast', in_unicast_calc)
    packet_graph.add('OutUnicast', out_unicast_calc)
    packet_graph.render_to_file('packet_graph.svg')
 
if __name__ == "__main__":
    main()
