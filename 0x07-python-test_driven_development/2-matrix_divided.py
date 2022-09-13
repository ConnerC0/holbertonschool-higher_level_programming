#!/usr/bin/python3
"""
    Project0x05: Test Driven Development
    Task 1: Divide a matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""
    err = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    if type(matrix) is not list:
        raise TypeError(err)
    if type(div) not in [int, float]:
        raise TypeError(err3)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    resultMatrix = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(err2)
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(err)
        resultMatrix.append(list(map(lambda n: round(n/div, 2), row)))
    return resultMatrix
