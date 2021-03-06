#!/usr/bin/env python3

# function to push commands
def commandpush(devicecmd): # devicecmd==list of commands issued to machines
    for coffeetime in devicecmd.keys():
        print('\nHandshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

# function to reboot device
def devicereboot(devicer): # devicer==list of devices to reboot
    for teatime in devicer:
        print('\nConnecting to.. ' + teatime + ' REBOOTING NOW!')
        # presumably code to reboot devices goes here

### Start our script
#work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} # data that replaces data stored in file

fileobject = open("work2dofile.txt","r")
filelist = fileobject.readlines()
cmdlist = []
for x in filelist:
    if filelist[0] == x:
        key1 = x
    else:
        cmdlist.append(x)

work2do = {key1:cmdlist}

dev2reb = ["10.4.0.1","10.5.0.1","10.6.0.1"]

print("Welcome to the network device command pusher") # welcome message

## get data set
print("\nData set found") # replace with function call that reads in data from file

## run 
commandpush(work2do) # call function to push commands to devices

devicereboot(dev2reb) # call function to reboot devices
