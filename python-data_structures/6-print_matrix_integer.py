#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    lenght = len(matrix)
    for i in matrix:
        for j in i:
            if j < lenght:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
        print("")
