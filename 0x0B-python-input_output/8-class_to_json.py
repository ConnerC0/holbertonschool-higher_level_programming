#!/usr/bin/python3
""" task 8 class to JSON """


def class_to_json(obj):
    """ method that returns the dict description with simple data structure """
    return vars(obj)
