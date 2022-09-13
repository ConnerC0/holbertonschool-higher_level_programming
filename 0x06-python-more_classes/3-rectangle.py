#!/usr/bin/python3
"""
The class of a rectangle that does nothing
"""


class Rectangle:
    """The rectangle class"""
    def __init__(self, width=0, height=0):
        """initialization of rectangle class"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """private instance of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns a rectangle in string format"""
        RectangleString = ""
        if self.__width is not 0 and self.__height is not 0:
            RectangleString += "\n".join("#" * self.__width for
                                         j in range(self.__height))
        return RectangleString

    def __repr__(self):
        """returns a string representation of a rectangle"""
        wid = str(eval('self.width'))
        hie = str(eval('self.height'))
        return "Rectangle({}, {})".format(wid, hie)
