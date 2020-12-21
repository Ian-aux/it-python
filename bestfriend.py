#!/usr/bin/python3

print('+---------------------+')
print('|  Best Friend Maker  |')
print('|    By Ian Pierce    |')
print('+---------------------+')
print()

while True:
    print("Hi. I'm the computer.")
    name = input("What's your name? ")
    print(f"Hi, {name}! What's your favorite color?")
    favorite_color = input("What's your favorite color? ")
    print(f"No way! My favorite color is also {favorite_color}!")
    favorite_movie = input("What's your favorite movie? ")
    print(f"What!?! My favorite movie is also {favorite_movie}!")
    favorite_game = input("What's your favorite game? ")
    print(f"Get out of here! My favorite game is {favorite_game}, too!")
    print("We like the same things! We should be best friends!")
    print('')
    
    response = input("Would you like to go again? (Y/n) ")
    while response.lower() not in ["n", "no", "nope", "y", "yes", "yep"]:
        response = input("Would you like to go again? (Y/n) ")
    if response.lower() in["n", "no", "nope"]:
        break