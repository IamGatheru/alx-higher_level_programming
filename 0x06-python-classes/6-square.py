#!/usr/bin/python3
"""
No module is to be imported
"""


class Square():
    """
    An empty class that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        private instance attribute: size

        Args:
        size(int): Size of the square (default is 0).
        position (tuple): Position of the square (default is (0,0)).
        """
        self.__size = size
        self.position = position

    @property
    def size(self):
        """
        To retrieve private instance attribute
        """
        return self.__size

    @property
    def position(self):
        """
        Retrieve the size of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square

        Args:
            value (tuple): Position tuple to set.

        Raises:
            TypeError: If value is not a tuple or contains non-integer values.
            ValueError: If any coordinate in value is less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(v, int)
                   for v in value) or value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
