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
        """Approximate the error function."""
        sign = 1 if x >= 0 else -1
        x = abs(x)

        a1 = 0.254829592
        a2 = -0.284496736
        a3 = 1.421413741
        a4 = -1.453152027
        a5 = 1.061405429
        p = 0.3275911

        t = 1 / (1 + p * x)

        y = 1 - (
            (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1)
            * t * (2.7182818285 ** (-x * x))
        )

        return sign * y

    def cdf(self, x):
        """Calculate the CDF of a given x-value."""
        z = (x - self.mean) / (self.stddev * (2 ** 0.5))
        return 0.5 * (1 + self.erf(z))
