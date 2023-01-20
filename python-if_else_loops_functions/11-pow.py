#!/usr/bin/python3


def pow(a, b):

    for i in  "b":
        
        if a < 0:
            power = a * a
        elif b == 0:
            power = 1
        elif b < 0:
            power = 1 / (a * a)
        else:
            power = a * a

    return power
