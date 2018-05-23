#!/usr/bin/env python3
message = 'Wow! You '
print('What is your numerical score?')
connection = float(input())
if connection >= 90:
    message = message + 'got an A! You will go far.'
elif connection >= 80:
    message = message + 'got a B. That is pretty good.'
elif connection >= 70:
    message = message + 'got a C. That is stunningly average.'
elif connection >= 60:
    message = message + 'got a D. Hey, you passed, right?.'
else:
    message = message + 'suck.'
print(message)
