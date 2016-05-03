#!/usr/bin/env python

# Use Netmiko to change the logging buffer size and to disable console logging 
# from a file on both pynet-rtr1 and pynet-rtr2.

from netmiko import ConnectHandler

def main():

    # Definition of rtr2.
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

    # Create a list of all the routers.
    all_routers = [rtr1, rtr2]

    # Loop through all the routers and show arp.
    for a_router in all_routers:
        net_connect = ConnectHandler(**a_router)

        # Check current logging buffer size.
        print "\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_router['device_type'])
        output = net_connect.send_command("show run | inc logging")
        print "Initial logging config: "
        print output
        print

        # Enter config mode, change logging buffer and console logging from file,
        #  exit config mode.
        output = net_connect.config_mode()
        output = net_connect.send_config_from_file(config_file='config_file.txt')
        output = net_connect.exit_config_mode()

        # Check logging buffer size again.
        output = net_connect.send_command("show run | inc logging")
        print "Final logging config: "
        print output
        print ">>>>>>>>> End <<<<<<<<<\n"

if __name__ == "__main__":
    main()

