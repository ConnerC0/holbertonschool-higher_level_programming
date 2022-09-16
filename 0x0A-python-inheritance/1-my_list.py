#!/usr/bin/python3
"""
A module that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    list extension class
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
