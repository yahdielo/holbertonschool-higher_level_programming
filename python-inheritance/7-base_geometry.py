#!/usr/bin/python3
"""this fucntions checks if objec is a instance of the parent class"""


class BaseGeometry:
    """this fucntions checks if objec is a instance of the parent class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
