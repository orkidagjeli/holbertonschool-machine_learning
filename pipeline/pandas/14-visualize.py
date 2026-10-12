#!/usr/bin/env python3
"""Visualize Bitcoin data using daily intervals."""

import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file


def visualize(df):
    """Clean, transform, and aggregate Bitcoin data by day."""
    # Remove the Weighted_Price column
    df = df.drop(columns=['Weighted_Price'])

    # Rename Timestamp to Date
    df = df.rename(columns={'Timestamp': 'Date'})

    # Convert Unix timestamps to datetime values
    df['Date'] = pd.to_datetime(df['Date'], unit='s')

    # Set Date as the index
    df = df.set_index('Date')

    # Fill missing Close values with the previous available value
    df['Close'] = df['Close'].ffill()

    # Fill missing High, Low, and Open values with Close
    for col in ['High', 'Low', 'Open']:
        df[col] = df[col].fillna(df['Close'])

    # Fill missing volume values with zero
    df[['Volume_(BTC)', 'Volume_(Currency)']] = df[
        ['Volume_(BTC)', 'Volume_(Currency)']
    ].fillna(0)

    # Keep data from 2017 onward
    df = df.loc['2017':]

    # Aggregate the data into daily intervals
    df = df.resample('D').agg({
        'High': 'max',
        'Low': 'min',
        'Open': 'mean',
        'Close': 'mean',
        'Volume_(BTC)': 'sum',
        'Volume_(Currency)': 'sum'
    })

    # Return the transformed DataFrame
    return df


if __name__ == '__main__':
    df = from_file(
        'coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ','
    )

    # Transform the data
    df = visualize(df)

    # Plot the daily data
    df.plot()
    plt.show()

    # Display the transformed DataFrame
    print(df)
