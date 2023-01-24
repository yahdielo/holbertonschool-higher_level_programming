#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    res = []

    lenght_a = len(tuple_a)
    lenght_b = len(tuple_b)
    diference_lenght = 0
    for i in range(lenght_a):
            res.append(tuple_a[i] + tuple_b[i])
    res = tuple(res)

    return res
