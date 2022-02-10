from pytest import fixture
from pytest_mock import MockerFixture

from stopwatch import Stopwatch

from .mocks.time import TimeMock


def describe_stopwatch() -> None:
    @fixture
    def time_mock() -> TimeMock:
        return TimeMock()

    def describe_start() -> None:
        def with_stop(mocker: MockerFixture, time_mock: TimeMock) -> None:
            mocker.patch('time.perf_counter', time_mock.perf_counter)
            sw = Stopwatch(print_report=True)
            time_mock.increment(1)
            sw.stop()
            assert sw.elapsed == 1
            assert str(sw) == '1.00s'
            assert repr(sw) == '<Stopwatch name=None elapsed=1.0>'
            assert len(sw.laps) == 1
            assert not sw.running
            assert sw.name is None

        def with_statement(mocker: MockerFixture, time_mock: TimeMock) -> None:
            mocker.patch('time.perf_counter', time_mock.perf_counter)
            sw = Stopwatch(print_report=True)
            time_mock.increment(1)
            sw.stop()
            assert sw.elapsed == 1
            assert str(sw) == '1.00s'
            assert repr(sw) == '<Stopwatch name=None elapsed=1.0>'
            assert len(sw.laps) == 1
            assert not sw.running
            assert sw.name is None

    def with_name(mocker: MockerFixture, time_mock: TimeMock) -> None:
        mocker.patch('time.perf_counter', time_mock.perf_counter)
        with Stopwatch(name='lorem') as sw:
            time_mock.increment(0.1)
        assert sw.name is not None
        assert sw.name == 'lorem'

    def with_precision(mocker: MockerFixture, time_mock: TimeMock) -> None:
        mocker.patch('time.perf_counter', time_mock.perf_counter)
        with Stopwatch(precision=5) as sw:
            time_mock.increment(0.123456789)
        assert str(sw) == '123.45679ms'
        sw.precision = 3
        assert str(sw) == '123.457ms'

    def describe_print_report() -> None:
        def calls_print(mocker: MockerFixture, time_mock: TimeMock) -> None:
            mocker.patch('time.perf_counter', time_mock.perf_counter)
            print_mock = mocker.patch('builtins.print')
            with Stopwatch(print_report=True) as sw:
                time_mock.increment(0.1)
            print_mock.assert_called_once()
            print_mock.assert_called_with(sw._format())

        def does_not_call_print(
            mocker: MockerFixture, time_mock: TimeMock
        ) -> None:
            mocker.patch('time.perf_counter', time_mock.perf_counter)
            print_mock = mocker.patch('builtins.print')
            with Stopwatch(print_report=False):
                time_mock.increment(0.1)
            print_mock.assert_not_called()

        def with_name(mocker: MockerFixture, time_mock: TimeMock) -> None:
            mocker.patch('time.perf_counter', time_mock.perf_counter)
            mocker.patch('builtins.print')
            with Stopwatch(name='lorem', print_report=True) as sw:
                time_mock.increment(0.1)
            assert sw._format().endswith('lorem')
            sw._print_report = False
            assert sw._format() == ''

    def reset_laps_and_duration(
        mocker: MockerFixture, time_mock: TimeMock
    ) -> None:
        mocker.patch('time.perf_counter', time_mock.perf_counter)
        with Stopwatch() as sw:
            time_mock.increment(1.0)
        assert sw.elapsed == 1.0
        assert len(sw.laps) == 1
        sw.reset()
        assert sw.elapsed == 0.0
        assert len(sw.laps) == 0

    def add_new_laps(mocker: MockerFixture, time_mock: TimeMock) -> None:
        mocker.patch('time.perf_counter', time_mock.perf_counter)
        with Stopwatch() as sw:
            for i in range(5):
                with sw.lap():
                    time_mock.increment(i)
        assert sw.elapsed == 10
        assert len(sw.laps) == 5
        assert sw.laps == [i for i in range(5)]

    def describe_report() -> None:
        def without_laps(mocker: MockerFixture, time_mock: TimeMock) -> None:
            mocker.patch('time.perf_counter', time_mock.perf_counter)
            with Stopwatch('sw1') as sw1:
                time_mock.increment(1)
            with Stopwatch() as sw2:
                time_mock.increment(1)
            with Stopwatch(precision=4) as sw3:
                time_mock.increment(1)
            assert sw1.report() == '[Stopwatch#sw1] total=1.00s'
            assert sw2.report() == '[Stopwatch] total=1.00s'
            assert sw3.report() == '[Stopwatch] total=1.0000s'

        def with_laps(mocker: MockerFixture, time_mock: TimeMock) -> None:
            mocker.patch('time.perf_counter', time_mock.perf_counter)
            with Stopwatch() as sw:
                for i in range(5):
                    with sw.lap():
                        time_mock.increment(i)
            assert sw.report() == '[Stopwatch] total=10.00s, mean=2.00s, ' + \
                'min=0.00s, median=2.00s, max=4.00s, dev=1.41s'
