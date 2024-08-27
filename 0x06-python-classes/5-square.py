#!/usr/bin/python3
"""
No module is to be imported
"""


class Square():
    """
    An empty class that defines a square
    """
    def __init__(self, size=0):
        """
        private insatnce attribute: size
        """
        self.__size = size

    @property
    def size(self):
        """
        To retrieve private instance attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        to set private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            for _ in range(self.__size):
                print("#", end="")
            print()
