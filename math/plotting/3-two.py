#!/usr/bin/env python3
"""Plot the exponential decay of radioactive elements."""
import numpy as np
import matplotlib.pyplot as plt


def two():
    """Plot C-14 and Ra-266 decay over time."""
    # Use the time values specified by the exercise
    x = np.arange(0, 20001, 1000)

    # Calculate the fraction remaining for each element
    # Replace these formulas with the exact exercise formulas if provided
    y1 = np.exp((np.log(0.5) / 5730) * x)
    y2 = np.exp((np.log(0.5) / 1600) * x)

    # Create the figure
    plt.figure(figsize=(6.4, 4.8))

    # Plot C-14 as a red dotted line
    plt.plot(x, y1, 'r:', label='C-14')

    # Plot Ra-266 as a green solid line
    plt.plot(x, y2, 'g-', label='Ra-266')

    # Add labels and title
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of Radioactive Elements')

    # Set the axis limits
    plt.xlim(0, 20000)
    plt.ylim(0, 1)

    # Add the legend
    plt.legend(loc='upper right')

    # Display the plot
    plt.show()
