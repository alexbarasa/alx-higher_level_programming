#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
remainder = number % 10
if (number < 0):
    print(f"Last digit of {number} is {-remainder} and is less than 6 and not 0")
else:
    if (number % 10 == 0):
        print(f"Last digit of {number} is {remainder} and is 0")
    elif (number % 10 > 5):
        print(f"Last digit of {number} is {remainder} and is greater than 5")
    else:
        print(f"Last digit of {number} is {remainder} and is less than 6 and not 0")
