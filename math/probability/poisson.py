#!/usr/bin/env python3
"""Poisson distribution class."""

import math


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

        numerator = (self.lambtha ** k) * math.exp(-self.lambtha)
        denominator = math.factorial(k)

        return numerator / denominator
