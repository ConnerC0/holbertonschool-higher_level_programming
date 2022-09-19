#!/usr/bin/python3
""" task 5 save object to a file """


import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file, using a JSON representation """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
