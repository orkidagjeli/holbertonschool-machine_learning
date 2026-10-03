#!/usr/bin/env python3
"""Write a function that returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """ Find transpose """
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]
