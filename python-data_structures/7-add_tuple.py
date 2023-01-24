#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    res = []

    lenght1 = len(tuple_a)
    length2 = len(tuple_b)

    for i in range(lenght1):
        if lenght1 < lenght2:
            lenght1 = lenght1 - 1
            res.append(tuple_a[i] + tuple_b[i])
    res = tuple(res)

    return res
