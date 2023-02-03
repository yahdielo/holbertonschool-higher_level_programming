#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle:
    """This fucntion defines a rectangle"""
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >=0")
        if type(height) != int:
            raise TypeError("height must be a integer")
        elif height < 0:
            raise ValueError("height must be >=0")
        self.__height = height
        self.__width = width

    @property
    def heigh(self):
        return self.__height
    @property
    def width(self):
        return self.__width
    
    @heigh.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        self.__width = value
