#!/usr/bin/python3
"""define a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""define the Rectangle class that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """initializes an instance"""
    def __init__(self, width, height):
        """raises:
        TypeError: if the width or height is not an integer
        ValueError: if width or height is not positive """

        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

        """string representation"""
        def __str__(self):
            """returns the string representation"""
            return "[Rectangle] {}/{}".format(self.__width, self.__height)

        def area(self):
            """Returns: the area of the rectangle"""
            return self.__width * self.__height
