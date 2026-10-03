#!/usr/bin/env python3
""" Write a function that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """Add 2 arrays"""
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
