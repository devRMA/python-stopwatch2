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
            self.time_mock.increment(0.1)
            self.assertTrue(lap.running)
            self.assertEqual(lap.elapsed, 0.1)
            self.assertEqual(repr(lap), '<Lap running=True elapsed=0.1000>')

    def test_stop(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            lap = Lap()
            lap.start()
            self.time_mock.increment(0.1)
            lap.stop()
            self.time_mock.increment(0.1)
            self.assertFalse(lap.running)
            self.assertEqual(lap.elapsed, 0.1)
            self.assertEqual(repr(lap), '<Lap running=False elapsed=0.1000>')
