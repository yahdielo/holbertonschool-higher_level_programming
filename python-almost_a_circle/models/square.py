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

    def __str__(self):
        """using parent methods"""
        var = "[Square]"
        var1 = (f"({self.id}) {self.x}/{self.y}")
        return (f"{var} {var1} - {self.width}")
