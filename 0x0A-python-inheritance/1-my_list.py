#!/usr/bin/python3
"""
A module that prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    list extension class
    """
    def print_sorted(self):
        if issubclass(MyList, list):
            print(sorted(self))
