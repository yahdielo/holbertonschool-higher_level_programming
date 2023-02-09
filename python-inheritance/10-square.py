#!/usr/bin/python3
"""command"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square:
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")