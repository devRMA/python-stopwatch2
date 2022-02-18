from unittest import TestCase
from unittest.mock import patch

from stopwatch.lap import Lap

from .mocks.time import TimeMock


class LapTest(TestCase):
    def setUp(self) -> None:
        self.time_mock = TimeMock()
        return super().setUp()

    def test_start(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            lap = Lap()
            lap.start()
            self.time_mock.increment(1)
            self.assertTrue(lap.running)
            self.assertEqual(lap.elapsed, 1)
            self.assertEqual(repr(lap), '<Lap running=True elapsed=1.0000>')

    def test_stop(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            lap = Lap()
            lap.start()
            self.time_mock.increment(1)
            lap.stop()
            self.time_mock.increment(1)
            self.assertFalse(lap.running)
            self.assertEqual(lap.elapsed, 1)
            self.assertEqual(repr(lap), '<Lap running=False elapsed=1.0000>')

    def test_multiples_stars(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            lap = Lap()
            for _ in range(3):
                lap.start()
                self.time_mock.increment(1)
                lap.stop()
            self.assertFalse(lap.running)
            self.assertEqual(lap.elapsed, 3.0)
            self.assertEqual(lap._fractions, [1.0, 1.0, 1.0])
            self.assertEqual(repr(lap), '<Lap running=False elapsed=3.0000>')
