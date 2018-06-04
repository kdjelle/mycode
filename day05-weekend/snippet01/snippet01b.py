#!/usr/bin/env python3
def evalIP(eIPv4):
    sIPv4 = eIPv4.split(".")
    aIPv4 = int(sIPv4[3])+10
    if aIPv4 > 255:
        return False
    else:
        return True
print("I'm a program that that reserves a block of IP addresses, 10 at a time!")
iIPv4 = input("Submit IPv4 address: ")
op = evalIP(iIPv4)
print(op)
