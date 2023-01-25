#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    def squared(_list=[]):

        new_list = []

        for i in _list:
            new_list.append(i**2)
        return new_list

    result = map(squared, matrix)

    return list(result)
