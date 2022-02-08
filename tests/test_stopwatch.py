from unittest import TestCase
from unittest.mock import MagicMock, patch

from stopwatch import Stopwatch

from .mocks.time import MockTime


class StopwatchTest(TestCase):
    def setUp(self) -> None:
        self.time_mock = MockTime()
        return super().setUp()

    def test_stopwatch_basic_usage(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            sw = Stopwatch()
            self.time_mock.increment(0.1)  # simulate time passing
            sw.stop()
        self.assertEqual(sw.elapsed, 0.1)
        self.assertEqual(len(sw.laps), 1)
        self.assertFalse(sw.running)
        self.assertEqual(str(sw), '100.00ms')
        self.assertEqual(repr(sw), '<Stopwatch name=None elapsed=0.1>')
        self.assertIsNone(sw.name)

    def test_stopwatch_with_statement(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            with Stopwatch() as sw:
                self.time_mock.increment(0.1)
                self.assertTrue(sw.running)
        self.assertEqual(sw.elapsed, 0.1)
        self.assertEqual(len(sw.laps), 1)
        self.assertFalse(sw.running)
        self.assertEqual(str(sw), '100.00ms')
        self.assertEqual(repr(sw), '<Stopwatch name=None elapsed=0.1>')
        self.assertIsNone(sw.name)

    def test_stopwatch_with_name(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            with Stopwatch(name='lorem') as sw:
                self.time_mock.increment(0.1)
        self.assertIsNotNone(sw.name)
        self.assertEqual(sw.name, 'lorem')

    def test_stopwatch_precision(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            with Stopwatch(precision=5) as sw:
                self.time_mock.increment(0.123456789)
        self.assertEqual(str(sw), '123.45679ms')

    @patch('builtins.print')
    def test_stopwatch_print_report(self, print_mock: MagicMock) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            with Stopwatch(print_report=True) as sw:
                self.time_mock.increment(0.1)
        print_mock.assert_called_once()
        print_mock.assert_called_with(sw._format())

    def test_stopwatch_reset(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            with Stopwatch() as sw:
                self.time_mock.increment(0.1)
        self.assertEqual(sw.elapsed, 0.1)
        self.assertEqual(len(sw.laps), 1)
        sw.reset()
        self.assertEqual(sw.elapsed, 0.0)
        self.assertEqual(len(sw.laps), 0)

    def test_stopwatch_restart(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            with Stopwatch() as sw:
                self.time_mock.increment(0.1)
            self.assertEqual(sw.elapsed, 0.1)
            self.assertEqual(len(sw.laps), 1)
            sw.restart()
            self.time_mock.increment(0.1)
            sw.stop()
            self.assertEqual(sw.elapsed, 0.1)
            self.assertEqual(len(sw.laps), 1)

    def test_stopwatch_lap(self) -> None:
        with patch('time.perf_counter', self.time_mock.perf_counter):
            with Stopwatch() as sw:
                for i in range(5):
                    with sw.lap():
                        self.time_mock.increment(i)
        self.assertEqual(sw.elapsed, 10)
        self.assertEqual(len(sw.laps), 5)
        self.assertEqual(sw.laps, [i for i in range(5)])
