from unittest import TestCase
from unittest.mock import patch

from stopwatch import utils

from .mocks.inspect import InspectMock


class UtilsTest(TestCase):
    def test_format_elapsed_time(self) -> None:
        self.assertEqual(utils.format_elapsed_time(1, 2), '1.00s')
        self.assertEqual(utils.format_elapsed_time(1, 4), '1.0000s')
        self.assertEqual(utils.format_elapsed_time(1, 0), '1s')
        self.assertEqual(utils.format_elapsed_time(0.1, 0), '100ms')
        self.assertEqual(utils.format_elapsed_time(0.001, 0), '1ms')
        self.assertEqual(utils.format_elapsed_time(0.0001, 0), '100μs')
        self.assertEqual(utils.format_elapsed_time(0.000001, 0), '1μs')

    def test_inspect_caller(self) -> None:
        with patch('inspect.stack', InspectMock.stack):
            caller = utils.inspect_caller()
        self.assertEqual(caller.module, '<unknown>')
        self.assertEqual(caller.function, 'function')
        self.assertEqual(caller.line_number, 2)
