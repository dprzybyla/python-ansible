#!/usr/bin/env python

# Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.

import pexpect
import time

def main():
    ip_addr = '50.76.53.27'
    ssh_port = 8022
    username = 'pyclass'
    password = '88newclass'

    # Login via ssh. Add flag so we can proceed if target absent from 'known_hosts'.
    ssh_conn = pexpect.spawn('ssh -o "StrictHostKeyChecking no" -l {} {} -p {}'.format(username, ip_addr, ssh_port))
    ssh_conn.timeout = 3
    
    # Enter the password.
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    
    # Look for the prompt.
    ssh_conn.expect('pynet-rtr2#')

    # Issue the command then wait for the prompt.
    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('pynet-rtr2#')

    # Print the output generated before the prompt.
    print ssh_conn.before

if __name__ == "__main__":
    main()

