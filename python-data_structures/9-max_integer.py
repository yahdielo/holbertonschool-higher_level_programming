#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list == None:
        return None

    my_list.sort()

    return my_list[-1]

