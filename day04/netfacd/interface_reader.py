#!/usr/bin/env python3

import netifaces

#print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    # print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
    try:
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) #MAC address
        print('IP: ', end="")
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) #IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message
