#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        lenght = len(i)
        for j in i:
            count += 1
            if j < lenght:
                print("{:d}".format(j), end=" ")
            elif count == lenght:
                print("{:d}".format(j), end="")
        print("")
