#!/usr/bin/env python

# Use  sses Netmiko to execute 'show version' on each device in the database. 
# Calculate the amount of time required to do this. What is the difference in time 
# between executing 'show version' sequentially versus using processes?

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
from multiprocessing import Process, current_process
import django

def show_version(a_device):
    creds = a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type, ip=a_device.ip_address,
                                 username=creds.username, password=creds.password,
                                 port=a_device.port, secret='')        
    print
    print '#' * 80
    print remote_conn.send_command_expect("show version")
    print '#' * 80
    print

def main():
    django.setup()
    
    start_time = datetime.now()
    devices = NetworkDevice.objects.all()

    procs = []
    for a_device in devices:
        my_proc = Process(target=show_version, args=(a_device,))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        print a_proc
        a_proc.join()

    elapsed_time = datetime.now() - start_time
    print "Elapsed time: {}".format(elapsed_time)

if __name__ == "__main__":
    main()
