#!/usr/bin/python3

"""define a class"""


class Rectangle:
    """initialize an instance of the rectangle"""
    def __init__(self, width=0, height=0):
        """width: is the width of the rectangle.
            height: is the height of the rectangle.
        """
        self.width = width
        self.height = height

    """retrieves the width"""
    def width(self):
        """returns: the width"""
        return self.__width
    """set the width"""
    def width(self, value):
        """TypeError: if the value is not an integer"""
        """ValueError: if the value is less than 0."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value
    """property that retrives height"""
    def height(self):
        """return:the height"""
        return self.__height
    """set the height"""
    def height(self, value):
        """TypeError: if the height is not an integer"""
        """ValueError: if the height is not greater than 0"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
