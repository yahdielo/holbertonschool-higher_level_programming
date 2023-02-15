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
        self.__x = x
        self.__y = y
        self.__id = id
        self.__size = size
        
    #using parent methods
    def __str__(self):
        var = "[Rectangle]"
        var1 = (f"({id}) {self.__x}/{self.__y}")
        return (f"{var} {var1} - {self.__size}")
