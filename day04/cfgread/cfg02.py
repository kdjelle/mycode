#!/usr/bin/env python3

## filename input
xfile = input('Enter filename:')

## create file object in "r"ead mode
configfile = open(xfile, 'r')

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no '\n'
print(configlist)

## display how many lines are in the file vlanconfig.cfg
print(len(configlist))

## Always close your file
configfile.close()
