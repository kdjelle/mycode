#!/usr/bin/env python3

#My function that opens a file, writes arguments, and closes.
def newtfile(string1, string2, string3):
    vfo = open("source.txt","a") #vivian file object
    print(string1, string2, string3, file = vfo)
    vfo.close()

choice = " "
while(choice.lower() != "q"):
    x = input("Gimme a string: ")
    y = input("Gimme string 2: ")
    z = input("Gimme string 3: ")
    choice = input("q to quit")
    newtfile(x, y, z)
