#!/usr/bin/env python3
"""Plot the exponential decay of two radioactive elements."""
import numpy as np
import matplotlib.pyplot as plt


def two():
    """Plot C-14 and Ra-266 decay over time."""
    x = np.arange(0, 20001, 1000)

    # Calculate the decay of Carbon-14
    c14 = np.exp((np.log(0.5) / 5730) * x)

    # Calculate the decay of Ra-266
    ra266 = np.exp((np.log(0.5) / 1600) * x)

    # Create the figure
    plt.figure(figsize=(6.4, 4.8))

    # Plot C-14 as a red dotted line
    plt.plot(x, c14, 'r:', label='C-14')

    # Plot Ra-266 as a green solid line
    plt.plot(x, ra266, 'g-', label='Ra-266')

    # Add axis labels and title
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of Radioactive Elements')

    # Set axis limits
    plt.xlim(0, 20000)
    plt.ylim(0, 1)

    # Display the legend in the upper right
    plt.legend(loc='upper right')

    # Display the plot
    plt.show()
