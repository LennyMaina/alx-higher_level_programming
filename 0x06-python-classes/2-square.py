#!/usr/bin/python3
"""Declare a square"""


class Square:
    """Represent a square"""


    def __init__(self, size=0):
        """Initialize a square


            Args:
                size: size of Square


        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
