#!/usr/bin/env python3
#NAPALM Challenge step 1, pulling current config from switches

#imports
from blessings import Terminal
import csv
from napalm import get_network_driver
from subprocess import call

#presets
t = Terminal()
targs = []

#functions
def lx(p): #calculate center width
    x = t.width - len(p)-1
    return int(x)
def title(p): #position title
    with t.location(int(lx(p)/2),1):
        print(t.bold_blue(p))
def csvf(cfile): #read file
    dfile = open(cfile)
    dline = csv.reader(dfile)
    for d in dline:
        targs.append(d)
    dfile.close()
def retrieve(r): #open device, read configs and create files
    dev = targs[targs.index(r)][0]
    os = targs[targs.index(r)][1]
    ip = targs[targs.index(r)][2]
    user = targs[targs.index(r)][3]
    passwd = targs[targs.index(r)][4]
    driver = get_network_driver(os)
    device = driver(ip,user,passwd)
    device.open()
    config = device.get_config()
    running_config = config['running']
    f = open((str(dev) + '.run'), 'w')
    f.write(running_config)
    f.close()
    device.close()
def mainloop(i): #main loop reduced to function for re-use
    csvf(i)
    for t in targs:
        retrieve(t)

#start
print(t.clear())
title('ConfigPuller 0.1')
print('\n\nHow to use: Enter the name of a comma separated value file containing the name, operating system, IP address, user name, and password of each device you need to pull from, and this program will produce a config file for each machine.')
try: #
    ifile = input('\nEnter name of csv file here: ')
    mainloop(ifile)
except:
    ifile = input('\nSorry that didn\'t work Try again: ')
    mainloop(ifile)
finally:    
    print('')
    call(['ls', '-l'])
