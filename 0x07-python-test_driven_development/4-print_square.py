#!/usr/bin/python3
"""
    Project0x05: Test Driven Development
    Task 3: Print Square
"""


def print_square(size):
    """
        This module prints a square with a '#' character
        of any positive integer size.
    """
    if type(size) not in int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
