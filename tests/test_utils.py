import inspect
from unittest import TestCase

from stopwatch import utils


class UtilsTest(TestCase):
    def test_format_elapsed_time(self) -> None:
        self.assertEqual(utils.format_elapsed_time(1, 2), '1.00s')
        self.assertEqual(utils.format_elapsed_time(1, 4), '1.0000s')
        self.assertEqual(utils.format_elapsed_time(1, 0), '1s')
        self.assertEqual(utils.format_elapsed_time(0.1, 0), '100ms')
        self.assertEqual(utils.format_elapsed_time(0.001, 0), '1ms')
        self.assertEqual(utils.format_elapsed_time(0.0001, 0), '100μs')
        self.assertEqual(utils.format_elapsed_time(0.000001, 0), '1μs')

    def test_format_elapsed_time_picks_unit_by_magnitude(self) -> None:
        # Negative values used to fail every `>=` and fall through to the
        # microsecond branch, so -1h came out as '-3600000000.00μs'.
        self.assertEqual(utils.format_elapsed_time(-3600, 2), '-3600.00s')
        self.assertEqual(utils.format_elapsed_time(-1, 2), '-1.00s')
        self.assertEqual(utils.format_elapsed_time(-0.1, 2), '-100.00ms')
        self.assertEqual(utils.format_elapsed_time(-0.000001, 2), '-1.00μs')
        self.assertEqual(utils.format_elapsed_time(0, 2), '0.00μs')

    def test_inspect_caller_describes_two_frames_up(self) -> None:
        def helper() -> utils.Caller:
            return utils.inspect_caller()

        frame = inspect.currentframe()
        assert frame is not None
        expected_line = frame.f_lineno + 1
        caller = helper()

        self.assertEqual(caller.module, __name__)
        self.assertEqual(
            caller.function, 'test_inspect_caller_describes_two_frames_up'
        )
        self.assertEqual(caller.line_number, expected_line)

    def test_inspect_caller_offset_skips_extra_frames(self) -> None:
        def inner() -> utils.Caller:
            return utils.inspect_caller(offset=1)

        def outer() -> utils.Caller:
            return inner()

        # offset=1 skips `outer`, landing on this test method instead.
        self.assertEqual(
            outer().function, 'test_inspect_caller_offset_skips_extra_frames'
        )
