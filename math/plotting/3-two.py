#!/usr/bin/env python3
"""Plot C-14 exponential decay with a logarithmic y-axis."""
import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """Display exponential decay using a logarithmic scale."""
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.figure(figsize=(6.4, 4.8))

    # Plot x against y as a line graph
    plt.plot(x, y)

    # Label the x-axis
    plt.xlabel('Time (years)')

    # Label the y-axis
    plt.ylabel('Fraction Remaining')

    # Set the graph title
    plt.title('Exponential Decay of C-14')

    # Set the y-axis to a logarithmic scale
    plt.yscale('log')

    # Set the x-axis range from 0 to 28650
    plt.xlim(0, 28650)

    # Display the graph
    plt.show()
