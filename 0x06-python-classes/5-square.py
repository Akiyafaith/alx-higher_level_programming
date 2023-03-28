#!/usr/bin/python3
"""define a class"""


class Square:
    """
    Represents a square.

    Attributes:
        size (int): The size of the square.

    Methods:
        area(): Returns the current square area.
        my_print(): Prints the square with the character #.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
