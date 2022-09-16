#!/usr/bin/python3
""" task 8 rectangle module """


Geometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(Geometry):
    """ rectangle class addition to the BaseGeometry module """
    def __init__(self, width, height):
        """ initializer for rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ finds area """
        return self.__width * self.__height

    def __str__(self):
        """ representation of the rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
