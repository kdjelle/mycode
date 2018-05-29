#!/usr/bin/env python3
#By Kyle Jelle

outFile = open('admin.rc', 'a')                                   #Open file admin.rc for writing

print('What is the OS_AUTH_URL?')                                 #OS_AUTH_URL prompt
osAUTH = input()                                                  #OS_AUTH_URL input
print('export OS_AUTH_URL=' + osAUTH, file=outFile)               #OS_AUTH_URL write to admin.rc

print('export OS_IDENTITY_API_VERSION=3', file=outFile)           #Write OS_IDENTITY_API_VERSION=3 out to admin.rc

print('What is the OS_PROJECT_NAME?')                             #OS_PROJECT_NAME prompt
osPROJ = input()                                                  #OS_PROJECT_NAME input
print('export OS_PROJECT_NAME=' + osPROJ, file=outFile)           #OS_PROJECT_NAME write to admin.rc

print('What is the OS_PROJECT_DOMAIN_NAME?')                      #OS_PROJECT_DOMAIN_NAME prompt
osPROJDOM = input()                                               #OS_PROJECT_DOMAIN_NAME input
print('export OS_PROJECT_DOMAIN_NAME=' + osPROJDOM, file=outFile) #OS_PROJECT_DOMAIN_NAME write to admin.rc

print('What is the OS_USERNAME?')                                 #OS_USERNAME prompt
osUSER = input()                                                  #OS_USERNAME input
print('export OS_USERNAME=' + osUSER, file=outFile)               #OS_USERNAME write to admin.rc

print('What is the OS_USER_DOMAIN_NAME?')                         #OS_USER_DOMAIN_NAME prompt
osUSERDOM = input()                                               #OS_USER_DOMAIN_NAME input
print('export OS_USER_DOMAIN_NAME=' + osUSERDOM, file=outFile)    #OS_USER_DOMAIN_NAME write to admin.rc

print('What is the OS_PASSWORD?')                                 #OS_PASSWORD prompt
osPASS = input()                                                  #OS_PASSWORD input
print('export OS_PASSWORD=' + osPASS, file=outFile)               #OS_PASSWORD write to admin.rc

outFile.close()                                                   #Close admin.rc
