#!/usr/bin/python3


def roman_to_int(roman_string):

    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500, "M": 1000}

    if isinstance(roman_string, str) is False or roman_string is None:
        return 0

    number_sum = 0
    reverse_numbers = reversed(roman_string)
    reverse_list = []
    _numberold = 0

    if len(roman_string) == 1:
        number_sum = roman_numbers.get(roman_string)
        return number_sum

    else:
        for i in reverse_numbers:
            reverse_list.append(roman_numbers.get(i))

        for i in reverse_list:
            if i < _numberold:
                number_sum -= i
            else:
                number_sum += i
            _numberold = i
    return number_sum
