#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print("{} is a negative".format(number))
if number > 0:
    print("{} is a positive".format(number))
if number == 0:
    print("{} is zero".format(number))
