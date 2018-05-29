#!/usr/bin/env python3
#by Kyle Jelle
import csv                                                        #import CSV library
f = open('csv_users.txt', 'r')                                    #open csv_users.txt
i = 0                                                             #set i equal to zero for use as counter
for row in csv.reader(f):                                         #open the for loop
    i = i + 1                                                     #increment i by 1
    filename = 'admin.rc%d'%(i,)                                  #set filename with variable i
    rcfile = open(filename, 'w')                                  #open the file we're writing to
    print('export OS_AUTH_URL=' + row[0], file=rcfile)            #print OS_AUTH_URL to rcfile
    print('export OS_IDENTITY_API_VERSION=3', file=rcfile)        #print OS_IDENTITY_API_VERSION to rcfile
    print('export OS_PROJECT_NAME=' + row[1], file=rcfile)        #print OS_PROJECT_NAME to rcfile
    print('export OS_PROJECT_DOMAIN_NAME=' + row[2], file=rcfile) #print OS_PROJECT_DOMAIN_NAME to rcfile
    print('export OS_USERNAME=' + row[3], file=rcfile)            #print OS_USERNAME to rcfile
    print('export OS_USER_DOMAIN_NAME=' + row[4], file=rcfile)    #print OS_USER_DOMAIN_NAME to rcfile
    print('export OS_PASSWORD=' + row[5], file=rcfile)            #print OS_PASSWORD to rcfile
    rcfile.close()                                                #close working rcfile
