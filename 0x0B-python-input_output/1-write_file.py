#!/usr/bin/python3
""" task 1 write a file """


def write_file(filename="", text=""):
    """ write a string to a file """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
