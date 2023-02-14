#!/usr/bin/python3
"""This module inherits  from base"""
from models.base import Base


class Rectangle(Base):
    """This module inherits  from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif type(height) != int:
            raise TypeError("height must be an integer")

        elif type(x) != int:
            raise TypeError("x must be an integer")
        elif type(y) != int:
            raise TypeError("y must be an integer")

        elif width <= 0:
            raise ValueError("width must be > 0")
        elif height <= 0:
            raise ValueError("height must be > 0")

        elif x < 0:
            raise ValueError("x must be >= 0")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def update(self, *args):
        lenght = len(args) - 1
        if lenght == 0:
            self.__id = args[0]
        elif lenght == 1:
            self.id = args[0]
            self.__width = args[1]
        elif lenght == 2:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif lenght == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif lenght >= 0 and lenght < 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]

    def __str__(self):
        var = "[Rectangle]"
        var1 = (f"({self.id}) {self.__x}/{self.__y}")
        return (f"{var} {var1} - {self.__width}/{self.__height}")

    def area(self):
        """this module creturns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """this fucntions prints the rectangle"""

        for q in range(self.__y):
            print("")
        for i in range(self.__height):
            for q in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
