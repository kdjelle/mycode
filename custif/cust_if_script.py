#!/usr/bin/env python3
message = 'Wow! You '
print('What is your numerical score?')
grade = float(input())
if grade >= 90:
    message = message + 'got an A! You will go far.'
elif grade >= 80:
    message = message + 'got a B. That is pretty good.'
elif grade >= 70:
    message = message + 'got a C. That is stunningly average.'
elif grade >= 60:
    message = message + 'got a D. Hey, you passed, right?.'
else:
    message = message + 'suck.'
print(message)
