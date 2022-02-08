from time import sleep
from unittest import TestCase

from stopwatch import Stopwatch


# TODO : Make more tests
class StopwatchTest(TestCase):
    def test_stopwatch(self) -> None:
        with Stopwatch('lorem') as sw:
            sleep(0.1)
        self.assertGreater(sw.elapsed, 0.0)
        self.assertLess(sw.elapsed, 0.2)
        self.assertEqual(len(sw.laps), 1)
        self.assertFalse(sw.running)
        self.assertTrue(
            all([str(sw).startswith('100'),
                 str(sw).endswith('ms')])
        )
        self.assertTrue(
            all(
                [
                    repr(sw).startswith('<Stopwatch name=lorem elapsed='),
                    repr(sw).endswith('>')
                ]
            )
        )
