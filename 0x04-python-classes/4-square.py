#!/usr/bin/python3

"""Printing squares"""


class Square:
    def __init__(self, size=0):
        """initialize size"""
        self.__size = size

    @property
    def size(self):
        """Property"""
        return self.__size

    @size.setter
    def size(self, value):
        """class variable size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """find area"""
        return self.__size ** 2

    def myprint(self):
        """Print square"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print('')
        else:
            print('')
