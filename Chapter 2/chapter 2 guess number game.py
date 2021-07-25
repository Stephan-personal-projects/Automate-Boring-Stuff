#This program generates a number from 1 to 20 and asks for up to 6 guesses

#import random module
import random
#assign a random integer from 1 to 20 to variable: secretNumber
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

#for loop to give user 6 guesses
for guessesTaken in range(1, 7):
    print('Take a guess.')
    #assigns user's input to variable: guess
    guess = int(input())

    #logic for when user input is less than/greater than/equal to secretNumber
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

#logic for what to display when user guesses correctly or incorrectly 6 times
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))