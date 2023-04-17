#!/usr/bin/python3
from models.base import Base
"""define a class Rectangle that inherits from Base"""


class Rectangle(Base):
    """initialize a new instance of the class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """define private instant attributes"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.width * self.height
    def display(self):
        for n in range(self.height):
            print("#" * self.width)
        print()

    """get the width of the rectangle"""
    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width
    
    """set the width of the rectangle"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
    
    """get the height of the rectangle"""
    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height
    """set the height of the rectangle"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integerr")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
    """set and get the x values of the rectangle"""
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value
    
    """set and get the y values of the Rectangle"""
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
