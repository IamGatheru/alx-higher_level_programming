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
        try:
            size = int(size)
            self.__size = size
        except TypeError:
            print("size must be an integer")
        try:
            size >= 0
            self.__size = size
        except ValueError:
            ("size must be >= 0")
