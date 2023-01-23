#!/usr/bin/python3


def new_in_list(my_list, idx, element):

    new_list = my_list

    if idx < 0:
        return new_list

    lenght = len(my_list) - 1

    if idx > lenght:
        return new_list

    new_list[idx] = element

    return new_list, my_list
