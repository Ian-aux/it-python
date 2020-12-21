#!/usr/bin/python3

print('+---------------------+')
print('|  Best Friend Maker  |')
print('|    By Ian Pierce    |')
print('+---------------------+')
print('')

name = input('What is your name? ')

print('')
num = 42
print("I'm thinking of a number between 0 and 100. Can you guess it?")
guess = input("What is your guess? ")
guess = float(guess)
while guess != num:
    if guess < num:
        print("Sorry, too low. Guess again.")
    elif guess > num:
        print("Sorry, too high. Guess again.")
    guess = input("What is your guess? ")
    guess = float(guess)

print(f"Congratulations {name}! You guessed the number!")