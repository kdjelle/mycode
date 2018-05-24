#!/usr/bin/env python3
#By Kyle Jelle

#This is just a counter.
loginfail = 0

#And another counter.
loginsuccess = 0

#Create file-object
keystone_file = open('/home/student/mycode/day04/attemptlogin/keystone.common.wsgi','r')

#Create list of lines from file object.
keystone_file_lines=keystone_file.readlines()

#Create for loop
for i in range(len(keystone_file_lines)):

    #If statement for failure
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:

        #Increment the fail counter
        loginfail += 1

        #Add IP address to ipfail list
        

    #If statement for success
    elif "-] Authorization failed" in keystone_file_lines[i]:

        #Increment the success counter
        loginsuccess += 1

#Print results
print('The number of failed log in attempts is ' + str(loginfail))
print('The number of successful log in attempts is ' + str(loginsuccess))
print('The following IP addresses were associated with failed login attempts')
print(ipfail)
