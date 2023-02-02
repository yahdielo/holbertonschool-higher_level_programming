pycode#!/usr/bin/python3
""" This module supplys add_integer function,
if value if float, it will be cast to integer and added,
if value are not int, type error will execute"""


def add_integer(a=10, b=98):
    """Fucntion that adds two integers
    a (int): fisrt value
    b (int): second value"""
    if type(a) == float and type(b) == float:
        a = int(a)
        b = int(b)
    elif type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
