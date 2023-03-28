#!/usr/bin/python3
"""define a class"""


class Square:
    """
    A class used to represent a Square

    ...

    Attributes
    ----------
    __size : int
        the size of the square
    __position : tuple
        the position of the square

    Methods
    -------
    area():
        Returns the area of the square
    my_print():
        Prints the square with the character #
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructs all the necessary attributes for the square object.

        Parameters
        ----------
            size : int
                the size of the square (default is 0)
            position : tuple
                the position of the square (default is (0,0))
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the value of __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of __size

        Parameters
        ----------
        value : int
            the size of the square

        Raises
        ------
        TypeError
            if size is not an integer
        ValueError
            if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the value of __position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the value of __position

        Parameters
        ----------
        value : tuple
            the position of the square

        Raises
        ------
        TypeError
            if position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #

        If size is equal to 0, print an empty line
        position should be used by using space
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
