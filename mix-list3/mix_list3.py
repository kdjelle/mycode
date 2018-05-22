#!/usr/bin/env python3

#4. Create a simple list.
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)

#8. Printing only second item
print(list1[1])

#11. Add item to list.
list1.extend(['juniper'])
print(list1)

#14. Add a list within our list.
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)

#17. Return the value of item 5 in list1.
print(list1[4])

#20. Printing the first IP address.
print(list1[4][0])
