#!/usr/bin/python3
"""Square size validator """


class Square:
    """attributes: size (:obj:'int', optional): size of square
    TypeError: if 'size' is not 'int'
    ValueError: if 'size' is less than '0'
    """
    def __init__(self, size=0):
        """__init__ initializes the size value of the square."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
