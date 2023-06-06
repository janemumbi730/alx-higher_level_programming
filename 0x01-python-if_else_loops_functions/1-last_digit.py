#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number
while (digit > 10 and number > 0):
    digit %= 10
while (digit < -10 and number < 0):
    digit %= -10

if (digit > 5):
    print(f"Last digit of {number:d} is {digit:d} and is greater than 5")

elif (digit == 0):
    print(f"Last digit of {number:d} is {digit:d} and is 0")

else:
    print(f"Last digit of {number:d} is {digit:d}", end=' ')
    print(f"and is less than 6 and not 0")
