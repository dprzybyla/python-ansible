#!/usr/bin/env python

# Use PExpect to change the logging buffer size (logging buffered <size>) on 
# pynet-rtr2. Verify this change by examining the output of 'show run'.

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

    # Enter configuration mode. There is a new prompt and we have to escape parentheses.
    ssh_conn.sendline('config t')
    ssh_conn.expect('\(config\)#')

    # Change logging buffer size.
    ssh_conn.sendline('logging buffered 64000')
    ssh_conn.expect('\(config\)#')

    # Exit configuration mode.
    ssh_conn.sendline('exit')
    ssh_conn.expect('pynet-rtr2#')

    # Eliminate paging.
    ssh_conn.sendline('terminal length 0')
    ssh_conn.expect('pynet-rtr2#')

    # Show running config.
    ssh_conn.sendline('sh run')
    ssh_conn.expect('pynet-rtr2#')

    # Print the output generated before the prompt.
    print ssh_conn.before

if __name__ == "__main__":
    main()

