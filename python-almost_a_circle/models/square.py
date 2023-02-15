#!/usr/bin/python3
"""comment"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        This module inherits methods and behavior from
        parent class, using the super function, and initializing
        methods is necesary
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        super(__class__, self.__class__).width.__set__(self, value)

    def __str__(self):
        """using parent methods"""
        var = "[Square]"
        var1 = (f"({self.id}) {self.x}/{self.y}")
        return (f"{var} {var1} - {self.width}")

    def update(self, *args, **kwargs):
        """comment"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        for i in kwargs:
            if i == "id":
                self.id = kwargs.get("id")
            if i == "size":
                self.size = kwargs.get("size")
            if i == "x":
                self.x = kwargs.get("x")
            if i == "y":
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """this module returns class methods as dictionary"""
        _dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            }
        return _dict
