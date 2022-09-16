#!/usr/bin/python3
""" task 7 base geometry module """


Geometry = __import__('7-base-geometry').BaseGeometry


class Rectangle(Geometry):
    """ The Rectangle class addition to the BaseGeometry module """
    def __init__(self, width, height):
        """ initializer for rectangle class """
        self.integer_validator("width", width)
        self.intger_validator("height", height)
        self.__width = width
        self.__height = height
