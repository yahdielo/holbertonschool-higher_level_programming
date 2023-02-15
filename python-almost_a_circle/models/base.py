#!/usr/bin/python3
"""
This module if id is not None, assign the public instance attribute id
with this argument value
 - you can assume id is an integer and you don’t need to test
the type of it
 """
import json


class Base:
    '''class atribute'''
    __nb_objects = 0

    '''class method'''
    def __init__(self, id=None):
        # id is a method attribute
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
