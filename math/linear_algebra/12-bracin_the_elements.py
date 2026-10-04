#!/usr/bin/env python3
"""Write a function that performs element-wise addition, subtraction,
   multiplication, and division"""


def np_elementwise(mat1, mat2):
    """element-wise addition, subtraction,multiplication, and division"""
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
