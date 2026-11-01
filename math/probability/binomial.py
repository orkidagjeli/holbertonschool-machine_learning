#!/usr/bin/env python3
"""Binomial distribution class."""


class Binomial:
    """Represents a binomial distribution."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize the binomial distribution."""
        if data is None:
            self.n = int(n)
            self.p = float(p)

            if self.n <= 0:
                raise ValueError("n must be a positive value")

            if self.p <= 0 or self.p >= 1:
                raise ValueError(
                    "p must be greater than 0 and less than 1"
                )
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)

            self.p = 1 - variance / mean
            self.n = round(mean / self.p)
            self.p = mean / self.n
