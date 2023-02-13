#!/usr/bin/python3


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
