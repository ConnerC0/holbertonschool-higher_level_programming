#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print("Last digit of" + number + "is" + number[-1:] + "and is greater than 5")
elif number < 6:
    print("Last digit of" + number + "is" + number[-1:] + "and is less than 6 and not 0")
else number == 0:
    print("Last digit of" + number + "is" + number[-1:] + "and is 0")
