#!/usr/bin/python3
""" task 1 my_list module"""


class MyList(list):
    """
    Class that extends the list and sorts
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
