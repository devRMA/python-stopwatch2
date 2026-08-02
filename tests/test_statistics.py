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
        self.assertEqual(
            repr(self.stats), f'<Statistics values={self.values}>'
        )

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
        self.assertEqual(
            self.stats.variance, statistics.pvariance(self.values)
        )

    def test_stdev(self) -> None:
        self.assertEqual(self.stats.stdev, statistics.pstdev(self.values))

    def test_does_not_alias_the_given_list(self) -> None:
        values = [1.0, 2.0]
        stats = Statistics(values)
        stats.add(3.0)
        self.assertEqual(values, [1.0, 2.0])
        values.append(99.0)
        self.assertEqual(len(stats), 3)

    def test_total_is_a_float_when_empty(self) -> None:
        self.assertIsInstance(Statistics().total, float)

    def test_to_dict(self) -> None:
        self.assertEqual(
            self.stats.to_dict(),
            {
                'mean': statistics.mean(self.values),
                'maximum': max(self.values),
                'median': statistics.median(self.values),
                'minimum': min(self.values),
                'total': sum(self.values),
                'variance': statistics.pvariance(self.values),
            },
        )
