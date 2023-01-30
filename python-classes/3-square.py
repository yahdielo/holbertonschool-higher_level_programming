#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 2-square.py)"""


class Square:

    def __init__(self, size=0):
        """ Return area of a square to know full"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        
    def area(self):
        return self.__size * self.__size
