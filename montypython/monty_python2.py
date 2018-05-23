#!/usr/bin/env python3
#by Kyle Jelle
#counter to control our while loop
round = 0
#our loop
while(True):
#counter variable increment
    round = round + 1
#getting the question on the screen
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
#user input for answer
    answer = input()
#if statement for correct answer
    if (answer.lower() == 'brian'):
        print('Correct')
        break
#super secret answer statement
    if (answer.lower() == 'shrubbery'):
        print('You gave the super secret answer!')
        break
#elif statement for complete failure
    elif(round==3):
        print('Sorry, the answer was Brian.')
        break
#else statement for all other conditions
    else:
        print('Sorry! Try again!')
