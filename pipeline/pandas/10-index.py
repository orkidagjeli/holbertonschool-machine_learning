#!/usr/bin/env python3
"""Set the Timestamp column as the DataFrame index"""


def index(df):
    """Set Timestamp as the index"""
    return df.set_index('Timestamp')
