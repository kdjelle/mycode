#!/usr/bin/env python3
lorem = open('testfile.txt', 'r')
loremr = lorem.read().split(" ")
lorem.close()
print("\t".join(loremr))
