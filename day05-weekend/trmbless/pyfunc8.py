#!/usr/bin/env python3
from blessings import Terminal
t = Terminal()
print(t.clear())

def blue_wp(p):
   print(t.bold_blue(p))

def lx(p):
    x = t.width - len(p)-1
    return int(x)

def ly(p):
    lines = len(p) / t.width
    y = t.height - int(lines)
    return int(y)

def answer(p):
    with t.location(int(lx(p)/2), int(ly(p)/2)-2): 
        print(t.bold_blue(p))

orders = ""
while orders != 'q': 
    orders = input("What should I say? (q to quit): ")
    print(t.clear())
    answer(orders)

answer("That's all.")
