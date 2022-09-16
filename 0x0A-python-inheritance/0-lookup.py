#!/usr/bin/python3
"""task 0 module"""


def lookup(obj):
    """
    function that returns the list of available attributes
    and methods of an object
    """
    list_of_atts_and_meths = list(dir(obj))
    return list_of_atts_and_meths
