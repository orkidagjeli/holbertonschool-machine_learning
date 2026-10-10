#!/usr/bin/env python3
"""Rename the Timestamp column and convert it to datetime"""
import pandas as pd


def rename(df):
    """Renames Timestamp to Datetime and selects Datetime and Close"""
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df[Datetime], unit='s')
    df = df[['Datetime', 'Close']]
    return df
