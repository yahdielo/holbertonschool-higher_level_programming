#!/usr/bin/python3
""" Write an empty class Square that defines a square"""


class Square:
    """ Write a class Square that defines a square by: (based on 1-square.py)"""
    def __init_(self, size=0):
        if type(size) != int:
            TypeError: size must be a integer
        elif size < 0:
            ValueError: size must be >= 0
        else:
            self.__size = size
