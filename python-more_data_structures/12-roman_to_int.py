#!/usr/bin/python3


def roman_to_int(roman_string):

    roman_numbers = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

    number = 0
    _number = 0

    if len(roman_string) == 1:
        number = roman_numbers.get(roman_string)
        return number
    
    else:
        for i in reversed(roman_string): 
            number += roman_numbers.get(i) 
        return number
