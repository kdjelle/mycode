#!/usr/bin/env python3
from blessings import Terminal
t = Terminal()
print(t.clear())

def yellow_np():
   print(t.bold_black_on_yellow('Print yellow text'))

def yellow_wp(p):
   print(t.bold_black_on_yellow(p))

def trx(p):
    x = t.width - len(p)
    return int(x)

def top_right(p):
    with t.location(trx(p), 0):
        yellow_wp(p)

top_right("I want this in the top right!")
