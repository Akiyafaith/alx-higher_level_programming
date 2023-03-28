#!/usr/bin/python3
"""define a class"""


class Square:
    """
    A class that represents a square.

    Attributes:
        - size (int): The size of each side of the square.

    Methods:
        - __init__(self, size=0): Initializes a new Square object
        - area(self):Calculates and returns the area of the square.
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
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
        - The size of the square (int).
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        - value (int): The new size of each side of the square.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - The area of the square (int).
        """
        return self.__size ** 2
