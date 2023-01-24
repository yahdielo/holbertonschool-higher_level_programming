#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    res = []

    lenght_a = len(tuple_a)
    lenght_b = len(tuple_b)
    diference_lenght = 0
    for i in range(lenght_a):
        if lenght_a > lenght_b:
            diference_lenght = lenght_a - lenght_b
            lenght1 = lenght1 - diference_lenght
            res.append(tuple_a[i] + tuple_b[i])
        if lenght_a < lenght_b:
            deference_lenght = lenght_b - lenght_a
            lenght_b = lenght_b - diference_lenght
            res.append(tuple_a[i] + tuple_b[i])
        else:
            res.append(tuple_a[i] + tuple_b[i])
    res = tuple(res)

    return res
