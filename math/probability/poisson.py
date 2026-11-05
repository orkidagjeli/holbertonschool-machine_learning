#!/usr/bin/env python3
"""Poisson distribution class."""


class Poisson:
    """Represents a poisson distribution."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize the Poisson distribution."""

        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Calculate the value of the PMF for a given k."""

        k = int(k)

        if k < 0:
            return 0

        e = 2.7182818285

        # Calculate e^(-lambtha)
        exp_value = e ** (-self.lambtha)

        # Calculate lambtha^k
        numerator = self.lambtha ** k

        # Calculate k! (factorial)
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

    return (exp_value * numerator) / factorial
