#!/usr/bin/python3
"""
    Project0x05: Test Driven Development
    Task 2: Say My Name
"""


def say_my_name(first_name, last_name=""):
    """
        Prints out given names from arg 1 and arg 2
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)
