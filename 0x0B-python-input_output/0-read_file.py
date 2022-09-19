#!/usr/bin/python3
""" task 0 Read File """


def read_file(filename=""):
    """ method to read a file """
    with open(filename, encoding="utf=8") as myFile:
        print(myFile.read())
