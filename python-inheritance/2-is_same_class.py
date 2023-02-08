#!/usr/bin/python3
"""This module provide a new class called MyList"""


def is_same_class(obj, a_class):
    """This module provide a new class called MyList"""
    if obj == a_class and Type(obj) == type(a_class):
        return True
    else:
        return False
