#!/usr/bin/python3
"""This module provide a new class called MyList"""


class MyList(list):
    """Defines a new class MyList that inherits from list"""
    def print_sorted(self):
        new_list = []
        for i in self:
            new_list.append(i)
        new_list.sort()
        print(new_list)

