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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2
