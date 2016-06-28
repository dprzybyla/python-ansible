#!/usr/bin/env python

# Set the vendor field of each NetworkDevice to the appropriate vendor. 
# Save this field to the database.

import django
from net_system.models import NetworkDevice

def main():
    django.setup()
    net_devices = NetworkDevice.objects.all()

    for a_device in net_devices:
        if 'arista' in a_device.device_type:
            a_device.vendor = 'Arista'
        elif 'cisco' in a_device.device_type:
            a_device.vendor = 'Cisco'
        elif 'juniper' in a_device.device_type:
            a_device.vendor = 'Juniper'
        a_device.save()

    for a_device in net_devices:
        print a_device, a_device.vendor

if __name__ == "__main__":
    main()

