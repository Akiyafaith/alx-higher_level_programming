#!/usr/bin/python3
"""define a class"""


class Square:
    """
    A class that represents a square.

    Attributes:
        - size (int): The size of each side of the square.

    Methods:
        - __init__(self, size): Initializes a new Square object
    """

    def __init__(self, size):
        """
        Initializes a new Square object with the given size.

        Parameters:
        - size (int): The size of each side of the square.
        """
        self.__size = size
