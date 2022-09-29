#!/usr/bin/python3
""" module that inherits from base """
from models.base import Base


class Rectangle(Base):
    """ rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization of rectangle class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for width value """
        return self.__width

    @property
    def height(self):
        """ getter for height value """
        return self.__height

    @property
    def x(self):
        """ getter for x value """
        return self.__x

    @property
    def y(self):
        """ getter for y value """
        return self.__y

    @width.setter
    def width(self, value):
        """ sets the value for the width of rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """ setter for x value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ setter for y value """
        if type(value) is not int:
            raise TyperError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @height.setter
    def height(self, value):
        """ sets the value for the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
