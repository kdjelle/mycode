#!/usr/bin/env python3
from blessings import Terminal
t = Terminal()
print(t.clear())

def yellow_wp(p):
   print(t.bold_black_on_yellow(p))

def trx(p):
    x = t.width - len(p)
    return int(x)

def top_right(p):
    with t.location(trx(p), 0):
        yellow_wp(p)

def prompt(p):
    with t.location(0,t.height-2):
       print(t.reverse(p))
    with t.location(len(p) + 1,t.height-2):
       orders = input()
    return orders

top_right("I want this in the top right!")

orders = prompt("Prompt on bottom left:")
