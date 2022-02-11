import statistics
from random import randint, sample
from unittest import TestCase

from stopwatch.statistics import Statistics


class StatisticsTest(TestCase):
    def setUp(self) -> None:
        self.values = sample(
            [c / randint(2, 50) for c in range(50)], randint(1, 50)
        )
        self.stats = Statistics(self.values)
        return super().setUp()

    def test_add_values(self) -> None:
        stats = Statistics()
        self.assertEqual(len(stats), 0)
        stats.add(0.1)
        self.assertEqual(len(stats), 1)
        stats = Statistics(self.values)
        self.assertEqual(len(stats), len(self.values))

    def test_repr(self) -> None:
        self.assertEqual(repr(self.stats), f'<Statistics values={self.values}>')

    def test_mean(self) -> None:
        self.assertEqual(self.stats.mean, statistics.mean(self.values))

    def test_maximum(self) -> None:
        self.assertEqual(self.stats.maximum, max(self.values))

    def test_median(self) -> None:
        self.assertEqual(self.stats.median, statistics.median(self.values))

    def test_minimum(self) -> None:
        self.assertEqual(self.stats.minimum, min(self.values))

    def test_total(self) -> None:
        self.assertEqual(self.stats.total, sum(self.values))

    def test_variance(self) -> None:
        self.assertEqual(self.stats.variance, statistics.pvariance(self.values))
