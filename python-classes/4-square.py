#!/usr/bin/python3


class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    

    #getter property
    @property
    def size(self):
        return self.__size
    
    #property setter
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = valuewish

    def area(self):
        return self.__size * self.__size
