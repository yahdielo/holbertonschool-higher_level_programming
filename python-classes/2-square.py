#!/usr/bin/python3
""" Write an empty class Square that defines a square"""


class square:
    """ Write an empty class Square that defines a square"""

    def __init_(self, size=0):
        if type(size) != int:
            TypeError: size must be a integer
        if size < 0:
            ValueError: size must be >= 0
            