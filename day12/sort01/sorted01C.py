#!/usr/bin/env python3

origlist = open('list.txt', 'r')
newlist = origlist.readlines()
finalist = sorted(newlist)
f = open('final_list.txt', 'w')
f.write(str(finalist))
f.close()
