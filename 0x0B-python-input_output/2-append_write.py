#!/usr/bin/python3
""" task 2 append to a file """


def append_write(filename="", text=""):
    """ a method that appends to a file """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
