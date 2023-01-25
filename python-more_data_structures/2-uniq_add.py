#!/usr/bin/python3


def uniq_add(my_list=[]):

    unique = set(my_list)
    add_unique = 0

    for i in unique:
        add_unique += i
    return add_unique
