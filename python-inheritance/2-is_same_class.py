#!/usr/bin/python3
"""This module provide a new class called MyList"""


def is_same_class(obj, a_class):
    """This module provide a new class called MyList"""
    if obj == a_class:
        return True
    if type(obj) == type(a_class):
        return True
    else:
        return False
