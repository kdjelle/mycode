#!/usr/bin/env python3
import time # This is required to include time module

## Count the number of ticks from the epoch
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks, '\n')

## Show how we can convert ticks into a useful time tuple
myTime = time.localtime(ticks) # pass ticks to localtime
print("The local time touple is:", myTime, '\n')
print("The local time touple year is:", myTime[0])
print("The local time touple month is:", myTime[1])
print("The local time touple day is:", myTime[2])
print("The local time touple hour is:", myTime[3])
print("The local time touple minute is:", myTime[4])
print("The local time touple second is:", myTime[5])
print("The local time touple week is:", myTime[6])
print("The local time touple year is:", myTime[7])
print("The local time touple daylight savings is:", myTime[8])    

bm,bd,by = input('\nEnter birthdate (mm/dd/yyyy): ').split('/')
bdate = int(by), int(bm), int(bd), myTime[3], myTime[4], myTime[5], myTime[6], myTime[7], myTime[8] 
bticks = time.mktime(bdate)
age = ticks - bticks
print('You are', int(age), 'seconds old')
print('Or', int(age/60/60/24), 'days old')
print('Or', int(age/60/60/24/365), 'years old')
