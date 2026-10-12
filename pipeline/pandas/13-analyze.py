#!/usr/bin/env python3
"""Calculate descriptive statistics"""
import pandas as pd


def analyze(df):
    """Compute statistics for all columns except Timestamp"""
    return df.drop(columns=['Timestamp']).describe()
