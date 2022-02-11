from unittest import TestCase
from unittest.mock import MagicMock, patch

from stopwatch import Statistics
from stopwatch.profile import _make_report, _print_report, profile
from stopwatch.utils import Caller
from tests.mocks.atexit import AtexitMock
import sys

from .mocks.time import TimeMock


class ProfileTest(TestCase):
    def setUp(self) -> None:
        self.time_mock = TimeMock()
        self.caller = Caller(
            module='<unknown>', function='function', line_number=0
        )
        return super().setUp()

    def test_make_report(self) -> None:
        report = _make_report(
            self.caller, 'name', Statistics([float(c) for c in range(1, 11)])
        )
        assert '[<unknown>#name]' in report
        assert 'hits=10' in report
        assert 'mean=5.50s' in report
        assert 'min=1.00s' in report
        assert 'median=5.50s' in report
        assert 'max=10.00s' in report

    @patch('builtins.print')
    def test_print_report_with_data(self, print_mock: MagicMock) -> None:
        stats_with_data = Statistics([float(c) for c in range(5)])
        _print_report(self.caller, 'name', stats_with_data)
        print_mock.assert_called_once()
        print_mock.assert_called_with(
            _make_report(self.caller, 'name', stats_with_data)
        )

    @patch('builtins.print')
    def test_print_report_without_data(self, print_mock: MagicMock) -> None:
        stats_without_data = Statistics()
        _print_report(self.caller, 'name', stats_without_data)
        print_mock.assert_not_called()

    @patch('builtins.print')
    def test_profile_no_call(self, print_mock: MagicMock) -> None:
        func = MagicMock(__name__='function_name')
        profile()(func)
        func.assert_not_called()
        print_mock.assert_not_called()

    @patch('builtins.print')
    def test_profile_with_call(self, print_mock: MagicMock) -> None:
        with patch('atexit.register', AtexitMock.register):
            with patch('time.perf_counter', self.time_mock.perf_counter):
                func = MagicMock(__name__='function_name')
                decorated_func = profile()(func)
                self.time_mock.increment(0.1)
                decorated_func()
        func.assert_called_once()
        print_mock.assert_called_once()

    @patch('builtins.print')
    def test_profile_with_name(
        self, print_mock: MagicMock
    ) -> None:
        with patch('atexit.register', AtexitMock.register):
            with patch('time.perf_counter', self.time_mock.perf_counter):
                func = MagicMock(__name__='function_name')
                decorated_func = profile(name='lorem')(func)
                self.time_mock.increment(0.1)
                decorated_func()
        func.assert_called_once()
        print_mock.assert_called_once()
        self.assertIn('lorem', print_mock.call_args[0][0])

    @patch('builtins.print')
    def test_profile_with_report_every(self, print_mock: MagicMock) -> None:
        with patch('atexit.register', AtexitMock.register):
            with patch('time.perf_counter', self.time_mock.perf_counter):
                func = MagicMock(__name__='function_name')
                decorated_func = profile(report_every=2)(func)
                self.time_mock.increment(0.1)
                decorated_func()
                self.time_mock.increment(0.1)
                decorated_func()
                self.time_mock.increment(0.1)
                decorated_func()
                self.time_mock.increment(0.1)
                decorated_func()
        self.assertEqual(func.call_count, 4)
        self.assertEqual(print_mock.call_count, 2)

    @patch('builtins.print')
    def test_profile_with_report_every_none(
        self, print_mock: MagicMock
    ) -> None:
        with patch('atexit.register', AtexitMock.register):
            with patch('time.perf_counter', self.time_mock.perf_counter):
                func = MagicMock(__name__='function_name')
                decorated_func = profile(report_every=None)(func)
                self.time_mock.increment(0.1)
                decorated_func()
                self.time_mock.increment(0.1)
                decorated_func()
                self.time_mock.increment(0.1)
                decorated_func()
                self.time_mock.increment(0.1)
                decorated_func()
        self.assertEqual(func.call_count, 4)
        print_mock.assert_not_called()
