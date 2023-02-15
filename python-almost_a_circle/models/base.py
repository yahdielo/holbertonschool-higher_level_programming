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

    @staticmethod
    def to_json_string(list_dictionaries):
        """comment"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """comment"""

        filename = f"{cls.__name__}.json"
        with open(filename, "w") as f:                
            new_list = []
            if list_objs:
                for i in list_objs:
                    new_list.append(i.to_dictionary())
            f.write(cls.to_json_string(new_list))
