 #!/usr/bin/python3


def matrix_divided(matrix, div):
    _matrix1 = []
    _matrix2 = []
    num = 0
    idx = 0

    print(f"{len(matrix[0])}")
    print(f"{len(matrix[1])}")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must be the same size")

    for j in matrix:
        for i in j:
            num = i / div
            if idx == 0:
                _matrix1.append(round(num, 2))
            elif idx == 1:
                _matrix2.append(round(num, 2))
        idx += 1
    matrix = [_matrix1, _matrix2]
    return  matrix