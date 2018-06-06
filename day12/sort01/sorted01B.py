#!/usr/bin/env python3

origlist = open('list.txt', 'r')
newlist = origlist.readlines()
finalist = sorted(newlist)
print(finalist)
