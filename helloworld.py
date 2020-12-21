#!/usr/bin/python3

print('+---------------+')
print('|  HELLO WORLD  |')
print('| By Ian Pierce |')
print('+---------------+')
print()

name = input('What is your name? ')
age = input('What is your age? ')
if age.isnumeric():
    age = int(age)
    print(f'Hello {name} You are {age} years old')
    print(f'Next year, you will be {age+1} years old')
else:
    print("You didn't type a valid number.")