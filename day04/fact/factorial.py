#!/usr/bin/env python3

# Number entry input
x = int(input("Enter a number: "))

# Initialize a variable
f = 1

# for loop up to x
for i in range(1, x+1):

    # the math
    f = f * i

# Printing the results
print(str(x) + '! = ' + str(f))
