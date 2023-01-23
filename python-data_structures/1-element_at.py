#!/usr/bin/python3


def element_at(my_list, idx):

    if idx < 0:
        return None

    lenght = len(my_list)

    if idx > lenght:
        return None

    print("{:d}".format(my_list(idx)))
