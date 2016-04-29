#!/usr/bin/env python

# Using SNMPv3 create a script that detects router configuration changes.

from snmp_helper import snmp_get_oid_v3,snmp_extract
from decimal import Decimal
import pickle
import email_helper

ip_addr = '50.76.53.27'
snmp_port_rtr2 = 8061
user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'
runningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
runningLastSaved = '1.3.6.1.4.1.9.9.43.1.1.2.0'  
startupLastChanged = '1.3.6.1.4.1.9.9.43.1.1.3.0'
sysUptime = '1.3.6.1.2.1.1.3.0'

recipient = 'przybyla9@yahoo.com'
subject = 'Running Config Has Changed!'
sender = 'dprzybyl@ringling.edu'

def main():
    snmp_device = (ip_addr, snmp_port_rtr2)
    snmp_user = (user, auth_key, encrypt_key)

    # Check whether time file already exists.
    try:
        with open('time.pkl') as file:
            pass
    except:
        # If time file does not exist, create first time entry.
        snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=runningLastChanged)
        output = snmp_extract(snmp_data)
        # Store time in a pickle file.
        d = open("time.pkl", "wb")
        pickle.dump(output, d)
        d.close()

    # Get last time stored.
    d = open("time.pkl", "rb")
    last_time = pickle.load(d)
    print "Last time: " + last_time

    # Check time of last running config change.
    snmp_data = snmp_get_oid_v3(snmp_device, snmp_user, oid=runningLastChanged)
    output = snmp_extract(snmp_data)
    print "New time: " + output

    # If time of last change greater than stored time, 
    # store the new change time and send email.
    if output > last_time:
        s = float(output)
        t = Decimal(s/100.0)
        time = round(t,2)
        print "Time is now Greater: " + str(time)
        
        # Store time of latest change in a pickle file.
        d = open("time.pkl", "wb")
        pickle.dump(output, d)
        d.close()
        print "New stored value: " + output

        # Send me an email with the time of last change.
        message = "Running config changed at: " + str(time) + "sec"
        email_helper.send_mail(recipient, subject, message, sender)
    else:
        print "Running config has not changed."

if __name__ == "__main__":
    main()
