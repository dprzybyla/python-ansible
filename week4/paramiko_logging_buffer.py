#!/usr/bin/env python

# Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2.

import paramiko
import time

def main():
    ip_addr = '50.76.53.27'
    ssh_port = 8022
    username = 'pyclass'
    password = '88newclass'

    # Create instance of SSHClient.
    remote_conn_pre=paramiko.SSHClient()

    # Automatically add untrusted hosts.
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Initiate SSH connection.
    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=ssh_port)
    
    # Use invoke_shell to establish an interactive session.
    remote_conn = remote_conn_pre.invoke_shell()

    # Set timeout.
    remote_conn.settimeout(6.0)

    # Turn off paging, enter configuration mode.
    remote_conn.send("terminal length 0\n")
    remote_conn.send("configure terminal\n")

    # Change the logging buffer.
    remote_conn.send("logging buffered 64000\n")

    # Wait for the command to complete.
    time.sleep(2)
   
    # Show the output of the command.
    output = remote_conn.recv(65535)
    print output

if __name__ == "__main__":
    main()

