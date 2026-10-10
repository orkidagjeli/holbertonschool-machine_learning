#!/usr/bin/env python3
"""Select specific columns and every 60th row"""


def slice(df):
    """Returns selected columns with every 60th row"""
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
