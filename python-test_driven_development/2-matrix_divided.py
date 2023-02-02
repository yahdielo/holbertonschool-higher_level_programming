 #!/usr/bin/python3


def matrix_divided(matrix, div):
    _matrix1 = []
    _matrix2 = []
    num = 0
    idx = 0

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must be the same size")
    for _list in matrix:
        if type(matrix) != list and type(_list) != list:
            raise TypeError("matrix must be a matrix (list of list) of integers/floats")
        for i in _list:
            if type(i) != int or type(i) != float:
                raise TypeError("matrix must be a matrix (list of list) of integers/floats")

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