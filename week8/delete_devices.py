#!/usr/bin/env python

# Remove the two objects created in the previous exercise from the database.

from net_system.models import NetworkDevice
import django

def main():
    django.setup()

    test_device1 = NetworkDevice.objects.get(device_name='test-device1')
    test_device1.delete()

    test_device2 = NetworkDevice.objects.get(device_name='test-device22')
    test_device2.delete()    

    # Verify devices that currently exist
    print
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device
    print

if __name__ == "__main__":
    main()
