#!/usr/bin/env python

# Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the 'show interfaces' 
# output to obtain the 'inOctets' and 'outOctets' fields for each of the interfaces on the 
# switch. Accomplish this using Arista's pyeapi.
#
# The following information is stored in .eapi.conf.
#
# [connection:pynet-sw2]
# username: eapi
# password: 7maxwell7
# host: 50.76.53.27
# port: 8343
# transport: https

import pyeapi
from pprint import pprint

def main():

    # Use pyeapi to login to the switch.
    pynet_sw2 = pyeapi.connect_to("pynet-sw2")

    # Use pyeapi to issue the 'show interfsces' command.
    interfaces = pynet_sw2.enable("show interfaces")   

    # The output is in a dictionary called 'result'.
    interfaces = interfaces[0]['result']

    # Get the dictionary called 'interfaces' from the result.
    interfaces = interfaces['interfaces']
    #pprint(interfaces)

    # InOctets and OutOctets are in another dictionary 'interfaceCounters'.
    data_stats = {} # Empty dictionary.
    for interface, int_value in interfaces.items():
        int_counter = int_value.get('interfaceCounters', {})
        data_stats[interface] = (int_counter.get('inOctets'), int_counter.get('outOctets'))

    # Print output data
    print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")
    for intf, octets in data_stats.items():
        print "{:20} {:<20} {:<20}".format(intf, octets[0], octets[1])

    print

if __name__ == "__main__":
    main()

