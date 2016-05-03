#!/usr/bin/env python

# Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.

from netmiko import ConnectHandler

def main():

    # Definition of routers
    rtr1 = {
        'device_type': 'cisco_ios',
        'ip':   '50.76.53.27',
        'username': 'pyclass',
        'password': '88newclass',
    }

    rtr2 = {
        'device_type': 'cisco_ios',
        'ip':   '50.76.53.27',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 8022,
    }

    srx = {
        'device_type': 'juniper',
        'ip':   '50.76.53.27',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 9822,
    }
    
    # Create a list of all the routers.
    all_routers = [rtr1, rtr2, srx]

    # Loop through all the routers and show arp.
    for a_router in all_routers:
        net_connect = ConnectHandler(**a_router)
        output = net_connect.send_command("show arp")
        print "\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_router['device_type'])
        print output
        print ">>>>>>>>> End <<<<<<<<<"

if __name__ == "__main__":
    main()

