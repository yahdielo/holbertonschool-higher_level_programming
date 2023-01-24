#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    res = []

    lenght_a = len(tuple_a)
    lenght_b = len(tuple_b)
    #diference_of_lenght = 0
    for i in range(lenght_a):
        if lenght_a > lenght_b:
            lenght_a = lenght_a - 1
            tuple_a = list.pop([lenght_a])
            res.append(tuple_a[i] + tuple_b[i])
        else:
            res.append(tuple_a[i] + tuple_b[i])
    res = tuple(res)

    return res
