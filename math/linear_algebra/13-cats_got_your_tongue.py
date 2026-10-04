#!/usr/bin/env python3
"""Write a function that concatenates two matrices along a specific axis"""


def np_cat(mat1, mat2, axis=0):
    """Concatinate two matrices"""
    return np.concatenates((mat1, mat2), axis=axis)
