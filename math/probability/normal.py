#!/usr/bin/env python3
"""Normal distribution class."""


class Normal:
    """Represents a normal distribution."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize the normal distribution."""

        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")

            self.mean = float(mean)
            self.stddev = float(stddev)

        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.mean = float(sum(data) / len(data))

            variance = sum(
                (x - self.mean) ** 2 for x in data
            ) / len(data)

            self.stddev = float(variance ** 0.5)

    def z_score(self, x):
        """Calculate the z-score of a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculate the x-value of a given z-score."""
        return self.mean + (z * self.stddev)

    def erf(self, x):
        """Calculate the error function."""
        pi = 3.1415926536
        total = 0.0

        for n in range(100):
            total += ((-1) ** n * x ** (2 * n + 1)) / (
                self.factorial(n) * (2 * n + 1)
            )

        return (2 / (pi ** 0.5)) * total

    def factorial(self, n):
        """Calculate the factorial of a number."""
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def cdf(self, x):
        """Calculate the CDF of a given x-value."""
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))
        return 0.5 * (1 + self.erf(z))
