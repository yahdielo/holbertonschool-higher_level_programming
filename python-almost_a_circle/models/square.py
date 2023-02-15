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
