from pytest_mock import MockerFixture

from stopwatch import utils

from .mocks.inspect import InspectMock


def describe_format_elapsed_time() -> None:
    def without_precision() -> None:
        assert utils.format_elapsed_time(0) == '0.00μs'
        assert utils.format_elapsed_time(1) == '1.00s'
        assert utils.format_elapsed_time(0.01) == '10.00ms'
        assert utils.format_elapsed_time(0.001) == '1.00ms'
        assert utils.format_elapsed_time(0.0001) == '100.00μs'

    def with_precision() -> None:
        assert utils.format_elapsed_time(0, 1) == '0.0μs'
        assert utils.format_elapsed_time(1, 3) == '1.000s'
        assert utils.format_elapsed_time(0.01, 5) == '10.00000ms'
        assert utils.format_elapsed_time(0.001, 0) == '1ms'
        assert utils.format_elapsed_time(0.0001, 2) == '100.00μs'


def describe_inspect_caller() -> None:
    def returns_caller_information(mocker: MockerFixture) -> None:
        mocker.patch('inspect.stack', InspectMock.stack)
        caller = utils.inspect_caller()
        assert caller.module == '<unknown>'
        assert caller.function == 'function'
        assert caller.line_number == 2
