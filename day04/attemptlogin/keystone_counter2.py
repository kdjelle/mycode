#!/usr/bin/env python3
#By Kyle Jelle

loginfail = 0                                                                            #This is just a counter.
loginsuccess = 0                                                                         #And another counter.
ipfail = []                                                                              #And this is the IP address list
keystone_file = open('/home/student/mycode/day04/attemptlogin/keystone.common.wsgi','r') #Create file-object

keystone_file_lines = keystone_file.readlines()                                          #Create list of lines from file object.

for i in range(len(keystone_file_lines)):                                                #Create for loop
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:                      #If statement for failure
        loginfail += 1                                                                   #Increment the fail counter
        ipfail.append(keystone_file_lines[i].split(' ')[-1])                             #Add IP address to ipfail list

    elif "-] Authorization failed" in keystone_file_lines[i]:                            #If statement for success
        loginsuccess += 1                                                                #Increment the success counter

print('The number of failed log in attempts is ' + str(loginfail))                       #Print results
print('The number of successful log in attempts is ' + str(loginsuccess))
print('The following IP addresses were associated with failed login attempts')
print(ipfail)
