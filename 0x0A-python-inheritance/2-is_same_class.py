#!/usr/bin/python3
""" Task 2 is same class module """


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of
    the specified class ; otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
