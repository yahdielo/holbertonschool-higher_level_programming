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

print(pow(2, 2))
print(pow(98, 2))
print(pow(100, 0))
print(pow(100, -2))
print(pow(-4, 5))
