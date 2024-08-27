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
    def size(self) -> int:
        """
        To retrieve private instance attribute
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
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

        def area(self) -> int:
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other: "Square") -> bool:
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other: "Square") -> bool:
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other: "Square") -> bool:
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other: "Square") -> bool:
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other: "Square") -> bool:
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other: "Square") -> bool:
        """Define the >= comparison to a Square."""
        return self.area() >= other.area()
