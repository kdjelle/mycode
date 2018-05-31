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

def prompt_location():
    return t.location(0,t.height-2)

def response_location(p):
    return t.location(len(p) + 1,t.height-2)

def prompt(p):
    with prompt_location():
       print(t.reverse(p))
    with response_location(p):
       orders = input()
    return orders   

top_right("I want this in the top right!")

orders = prompt("Prompt on bottom left:")
