# This is a game where you guess a number.
import random

guessesTaken = 0 #In Python's naming system, preference in naming variables is given to use of the underscore as a separator instead of camel case.

print('Hello! What be yer name mate?')
myName = input()  #see comment on line 4.

number = random.randint(1,20)  # you could also use randrange instead of randint.
print('Well, '+ myName+ ', I be thinking of a number between 1 and 20. What be yer guess? Better make it right or yer be gone overboard.')

for guessesTaken in range(6):
    print('Take a guess.') 
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1) #Here, the computer starts counting from 0-5 not from 1-6. Given this, you have to write, guessesTaken + 1, so that each time you take a guess, the computer adds one and does not count from 0. 
    print('Good job, ' + myName + '! Yer  guessed my number in ' + guessesTaken + ' guesses! Good job yer scurvy dog.')

if guess != number:
    number = str(number)
    print('Nope. The number I had in mind was ' + number + '.')
