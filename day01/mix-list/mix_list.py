#!/usr/bin/env python3
#Written by Kyle Jelle
#Experimenting with lists!

#7. This is my list!
my_list = [ "192.168.0.5", 5060, "UP" ]

# 8, 9, 10. The following are things we do with the list.
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )

#16. This is a new list added later.
New_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#17. This is the final output.
print ('When I ssh into IP addresses ' + New_list[3] + ' or ' + New_list[4] + ' I am unable to ping ports ' + str(New_list[0]) + ', ' + New_list[1] + ', or ' + str(New_list[2]) + '.')
