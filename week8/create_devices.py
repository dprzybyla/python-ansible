#!/usr/bin/env python

# Create two new test NetworkDevices in the database. Use both direct object 
# creation and the .get_or_create() method to create the devices.

from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    test_device1 = NetworkDevice(
        device_name='test-device1',
        device_type='cisco_ios',
        ip_address='184.105.247.77',
        port=22,
    )
    test_device1.save()

    test_device2 = NetworkDevice.objects.get_or_create(
        device_name='test-device22',
        device_type='cisco_ios',
        ip_address='184.105.247.78',
        port=22,
    )
    
    # Verify devices that currently exist
    print
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device
    print

if __name__ == "__main__":
    main()
