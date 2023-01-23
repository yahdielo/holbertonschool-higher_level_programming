#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        lenght = len(i)
        for j in i:
            if j < lenght:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
        print("")
