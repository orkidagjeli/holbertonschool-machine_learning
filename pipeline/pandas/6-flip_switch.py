#!/usr/bin/env python3
"""Sort a DataFrame in reverse chronological order and transpose it"""


def flip_switch(df):
    """Returns the sorted and transposed DataFrame"""
    df = df.sort_index(ascending=False)
    return df.transpose()
