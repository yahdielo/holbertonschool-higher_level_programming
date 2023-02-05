#!/usr/bin/python3
"""Write a class that describes a rectangle"""


class Rectangle:
    """This fucntion defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = Rectangle.print_symbol

    @property
    def heigh(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @heigh.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        _str = ""
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                if i != 0:
                    _str += "\n"
                for j in range(self.__width):
                    _str += str(self.print_symbol)
        return _str

    def __repr__(self):
        self.number_of_instances += 1
        _str = ""
        _str += str(self.__width) + ", " + str(self.__height)
        return "Rectangle(" + _str + ")"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        return cls(size,size)