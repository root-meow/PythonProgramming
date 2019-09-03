#This is a new version of the guess.py game.

import random
guessesTaken = 0

print('What be yer name mate?')
myName=input()

number=random.randrange(1,50)     #the .randint part calls a specific function in the random module.
print('Well, '+ myName +', I am thinking of a number, you have six tries to get it correct!')

for guessesTaken in range(6):
    print('Make yer guess')
    guess=input()
    guess=int(guess)
   
    if not 0 <= guess <= 50:  #This is the only part that has been added. It informs the player when they go outside the range.
        print('Our range is from 0 to 50')

    if guess > 50:
        print('The guessing range goes only to 50 and starts from 00')

    if guess < 0:
        print('The range starts from 0 to 50')

      

    if guess< number:
        print('You have guessed too low')
    if guess > number:
        print('You have guessed higher than my number!')
     
    if guess == number:
        break

if guess == number:
    guessesTaken= str(guessesTaken+1)
    print('Good job! Well done yer scurvy dog. You got it in '+guessesTaken+' I would have thrown you overboard if you did not get it correct')

if guess != number:
    number = str(number)
    print('Well, you have ter be thrown overboard, so that yer be sleepn with the fishes. The simple number be '+number+' be gone with that knowledge. Splash!')

