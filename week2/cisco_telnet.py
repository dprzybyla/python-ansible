#!/usr/bin/env python

# Write a script that connects using telnet to the pynet-rtr1 router.
# Execute the 'show ip int brief' command on the router and return the output.

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 5

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
   
    time.sleep(1) 
    output = remote_conn.read_very_eager()

    remote_conn.write("show ip int brief" + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output

    remote_conn.close()

if __name__ == "__main__":
    main()

