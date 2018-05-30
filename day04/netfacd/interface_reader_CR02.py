#!/usr/bin/env python3
import netifaces #import function
i2 = '' #clear i2
print('MAC Address finder:\n-------------------') #print program name
print('Available interfaces:\n') #print list title
for i1 in netifaces.interfaces(): print('  ' + i1)  #list adapters
while i2 != 'q': #while loop to keep the program running
    i2 = input('\nPlease enter interface name(q to quit): ') #input adapter name
    try: #what we want to happen
        if i2 !='q': #if statement to avoid quitting
            print('The MAC address of ' + i2 + ' is ', end='') #print intro
            print(netifaces.ifaddresses(i2)[netifaces.AF_LINK][0]['addr']) #print MAC address
        else: #else statement to quit
            print('\nGood-bye!\n') #farewell
            break #end program
    except: print('not available. Are you sure you typed that right?') #print an error message
