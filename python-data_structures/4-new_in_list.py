#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    new_list = list(my_list)
    lenght = len(my_list) - 1

    if idx > lenght or idx < 0:
        return new_list

    new_list[idx] = element

    return new_list
