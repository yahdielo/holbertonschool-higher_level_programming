#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    res = []

    lenght_a = len(tuple_a)
    lenght_b = len(tuple_b)
    #diference_of_lenght = 0
    for i in range(2):
        if lenght_b < 2:
            new_tuple_b = list(tuple_b)
            new_tuple_b.append(0)
            tuple_b = tuple(new_tuple_b)
            res.append(tuple_a[i] + tuple_b[i])
        if lenght_a < 2:
            new_tuple_a = list(tuple_a)
            new_tuple_a.append(0)
            tuple_a = tuple(new_tuple_a)
            res.append(tuple_a[i] + tuple_b[i])
        else:
            res.append(tuple_a[i] + tuple_b[i])
    res = tuple(res)

    return res
