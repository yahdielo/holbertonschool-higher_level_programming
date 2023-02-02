#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, "hole"]
]
print(matrix_divided(matrix, 1.2))
print(matrix)
print("-" * 20)
#print(matrix_divided(matrix1, 3))
#print(matrix1)