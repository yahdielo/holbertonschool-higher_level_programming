#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in matrix:
        for j in matrix:
            print("{:4}".format(matrix[i][j]))
        print("")
