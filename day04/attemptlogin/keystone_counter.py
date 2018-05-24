#!/usr/bin/env python3
#By Kyle Jelle

#This is just a counter.
loginfail = 0

#Create file-object
keystone_file = open('/home/student/mycode/day04/attemptlogin/keystone.common.wsgi','r')

#Create list of lines from file object.
keystone_file_lines=keystone_file.readlines()

#Create for loop
for i in range(len(keystone_file_lines)):

    #If statement
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:

        #Increment the counter
        loginfail += 1 

#Print results
print('The number of failed log in attempts is ' + str(loginfail))
