#!/usr/bin/env python3
"""Convert the last 10 rows of High and Close to a NumPy array"""
import pandas as pd


def array(df):
    """Returns the last 10 rows of High and Close as a NumPy array"""
    return df[['High', 'Close']].tail(10).to_numpy()
