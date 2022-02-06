from unittest import TestCase
from time import sleep
from stopwatch import Stopwatch


# TODO : Make more tests
class StopwatchTest(TestCase):

    def test_stopwatch(self):
        with Stopwatch() as sw:
            sleep(0.1)
        self.assertGreater(sw.elapsed, 0.0)
        self.assertLess(sw.elapsed, 0.2)
        self.assertTrue(str(sw).startswith('100') and str(sw).endswith('ms'))
