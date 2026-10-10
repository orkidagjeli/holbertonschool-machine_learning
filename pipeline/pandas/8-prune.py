#!/usr/bin/env python3
"""Remove rows where Close has NaN values"""


def prune(df):
    """Returns the DataFrame without rows where Close is NaN"""
    return df.dropna(subset=['Close'])
