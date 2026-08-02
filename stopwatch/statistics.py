import statistics


class Statistics:
    _values: list[float]

    def __init__(self, values: list[float] | None = None) -> None:
        # Copy: `values or []` aliased the caller's list, so add() mutated
        # it and later edits to it silently changed the statistics -- but
        # only for a non-empty list, since an empty one is falsy and got
        # replaced. Same behaviour either way now.
        self._values = list(values) if values else []

    def add(self, value: float) -> None:
        """
        Add a new value in seconds to get the statistics.

        Parameters
        ----------
        value : `float`
            The value to add in seconds.
        """
        self._values.append(value)

    @property
    def mean(self) -> float:
        """`float`: Return the mean value in seconds."""
        return statistics.mean(self._values)

    @property
    def maximum(self) -> float:
        """`float`: Return the maximum value in seconds."""
        return max(self._values)

    @property
    def median(self) -> float:
        """`float`: Return the median value in seconds."""
        return statistics.median(self._values)

    @property
    def minimum(self) -> float:
        """`float`: Return the minimum value in seconds."""
        return min(self._values)

    @property
    def total(self) -> float:
        """`float`: Return the total value in seconds."""
        # sum([]) is int 0, and the annotation promises a float.
        return float(sum(self._values))

    @property
    def variance(self) -> float:
        """`float`: Return the variance in seconds."""
        return statistics.pvariance(self._values)

    @property
    def stdev(self) -> float:
        """`float`: Return the population standard deviation in seconds."""
        return statistics.pstdev(self._values)

    def __len__(self) -> int:
        return len(self._values)

    def __repr__(self) -> str:
        return f'<Statistics values={self._values}>'

    def to_dict(self) -> dict[str, float]:
        """
        Return a dictionary with all properties from statistics

        Returns
        -------
        Dict[`str`, `float`]
            The dictionary
        """
        return {
            'mean': self.mean,
            'maximum': self.maximum,
            'median': self.median,
            'minimum': self.minimum,
            'total': self.total,
            'variance': self.variance,
        }
