import statistics
from typing import Dict, List, Optional


class Statistics:
    _values: List[float]

    def __init__(self, values: Optional[List[float]] = None) -> None:
        self._values = values or []

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
        return sum(self._values)

    @property
    def variance(self) -> float:
        """`float`: Return the variance in seconds."""
        return statistics.pvariance(self._values)

    def __len__(self) -> int:
        return len(self._values)

    def __repr__(self) -> str:
        return f'<Statistics values={self._values}>'

    def to_dict(self) -> Dict[str, float]:
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
            'variance': self.variance
        }
