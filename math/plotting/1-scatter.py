#!/usr/bin/env python3
"""Plot men's height versus weight as a scatter plot."""
import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """Display men's height and weight using magenta points."""
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))

    # Plot height against weight using magenta points
    plt.scatter(x, y, c='m')

    # Label the x-axis
    plt.xlabel('Height (in)')

    # Label the y-axis
    plt.ylabel('Weight (lbs)')

    # Set the graph title
    plt.title("Men's Height vs Weight")

    # Display the scatter plot
    plt.show()
