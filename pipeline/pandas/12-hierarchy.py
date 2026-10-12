#!/usr/bin/env python3
"""Rearrange and concatenate Bitstamp and Coinbase dataframes"""
import pandas as pd

index = __import__('10-index').index


def hierarchy(df1, df2):
    """Concatenate and rearrange the Bitstamp and Coinbase dataframes"""
    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]

    return pd.concat(
        [df2, df1],
        keys=['bitstamp', 'coinbase']
    ).swaplevel().sort_index()
