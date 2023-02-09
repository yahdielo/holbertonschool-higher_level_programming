#!/usr/bin/python3
"""this fucntions checks if objec is a instance of the parent class"""


def inherits_from(obj, a_class):
    """this fucntions checks if objec is a instance of the parent class"""
    return isinstance(obj, a_class) and type(obj) != a_class
