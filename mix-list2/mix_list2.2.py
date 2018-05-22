#!/usr/bin/env python3
#By Kyle Jelle
#This is still Lab09

#19. Apparently we're starting over with mostly new code.
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
proto.append('dns') # this line will add 'dns' to the end of our list
protoa.append('dns') # this line will add 'dns' to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print (proto)
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
print (protoa)

#23. Demonstration of python.org method
proto.remove('http')
print (proto)
