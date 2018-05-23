#!/usr/bin/env python3
#by Kyle Jelle
#Learning while loops.

while(True):

#prompt for network protocol
   l2p = input('Submit Layer 2 network protocol: ') 

#if-test statements
   if l2p == 'eth':
      print('ethernet protocol allowed')
      break

   if l2p == 'fc':
      print('fiber channel NOT allowed')
      break

   if l2p == 'ifb':
      print('infiniband NOT allowed')
      break

   if l2p == 'otn':
      print('Optical Network allowed')
      break

   else:
      print('No idea what that technology is')
      break

#End of program
