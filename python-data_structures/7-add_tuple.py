#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    res = []

    lenght_a = len(tuple_a)
    lenght_b = len(tuple_b)
    diference_of_lenght = 0
    for i in range(lenght_a):
        if lenght_a > lenght_b:
            diference_of_lenght = lenght_a - lenght_b
            res.append(tuple_a[i:-diference_of_lenght] + tuple_b[i])
        else:
            res.append(tuple_a[i] + tuple_b[i])
    res = tuple(res)

    return res
