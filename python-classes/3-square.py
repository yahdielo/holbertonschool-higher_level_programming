#!/usr/bin/python3
"""this module write a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """class square has to be an int area(self) returns the current square area"""
    def __init__(self, size=0):
         """class square has to be an int area(self) returns the current square area"""
         if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        
    def area(self):
        return self.__size * self.__size
