#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        for j in matrix:
            print("{:d}".format(ord(matrix[i][j])))
        print("")
