#!/usr/bin/env python

# Use Netmiko to connect to each of the devices in the database. 
# Execute 'show version' on each device. Calculate the amount of 
# time required to do this. Note, your results will be more reliable 
# if you use Netmiko's send_command_expect() method. 

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django

def main():
    django.setup()
    
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    for a_device in devices:
        creds = a_device.credentials
        remote_conn = ConnectHandler(device_type=a_device.device_type, ip=a_device.ip_address,
                                 username=creds.username, password=creds.password,
                                 port=a_device.port, secret='')        
        print
        print '#' * 80
        print remote_conn.send_command_expect("show version")
        print '#' * 80
        print

    elapsed_time = datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)

if __name__ == "__main__":
    main()
