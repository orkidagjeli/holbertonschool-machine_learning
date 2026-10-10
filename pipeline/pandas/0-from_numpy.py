#!/usr/bin/env python3
"""Write a function  that creates a pd.DataFrame from a np.ndarray"""


def from_numpy(array):
    """creates a pd.DataFrame from a np.ndarray"""
    columns = [chr(65 + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=columns)
