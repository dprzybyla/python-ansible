#!/usr/bin/env python

# Use Netmiko to change the logging buffer size on pynet-rtr2.

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
    
    # Check current logging buffer size.
    output = net_connect.send_command("show run | inc buffered")
    print
    print "Initial logging buffer size: " + output

    # Enter config mode, change logging buffer size, exit config mode.
    output = net_connect.config_mode()
    output = net_connect.send_command("logging buffer 64000")
    output = net_connect.exit_config_mode()

    # Check logging buffer size again.
    output = net_connect.send_command("show run | inc buffered")
    print "Final logging buffer size: " + output
    print

if __name__ == "__main__":
    main()

