#!/usr/bin/python3
"""define a class"""


class Square:
    """
    A class that represents a square.

    Attributes:
        - size (int): The size of each side of the square.

    Methods:
        - __init__(self, size=0): Initializes a new Square object
    """

    def __init__(self, size=0):
        """
        Initializes a new Square object with the given size.

        Parameters:
        - size (int): The size of each side of the square. Default value is 0.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
