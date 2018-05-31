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

yellow_wp("I want this to print in YELLOW")

x = trx("I want this to print in YELLOW")
print(x)
