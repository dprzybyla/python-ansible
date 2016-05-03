#!/usr/bin/env python

# Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to verify your state.

from netmiko import ConnectHandler

def main():

    # Definition of rtr2.
    rtr2 = {
        'device_type': 'cisco_ios',
        'ip':   '50.76.53.27',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 8022,
    }    

    # Log into router.
    net_connect = ConnectHandler(**rtr2)

    # Enter configuration mode.
    output = net_connect.config_mode()

    # Verify whether we are in configuration mode.
    output = net_connect.check_config_mode()
    print
    print "Are we in config mode?"
    print output
    print

if __name__ == "__main__":
    main()

