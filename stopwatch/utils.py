import sys
from typing import NamedTuple


class Caller(NamedTuple):
    module: str
    function: str
    line_number: int


def inspect_caller(offset: int = 0) -> Caller:
    """
    Describe the frame two levels above this call.

    Parameters
    ----------
    offset : `int`
        Extra frames to skip, for callers that add a level of their own.

    Returns
    -------
    `Caller`
        The module name, function name and line number of that frame.
    """
    frame = sys._getframe(2 + offset)
    return Caller(
        module=frame.f_globals.get('__name__', '<unknown>'),
        function=frame.f_code.co_name,
        line_number=frame.f_lineno,
    )


def format_elapsed_time(elapsed: float, precision: int = 2) -> str:
    """
    Format the elapsed time in seconds to a human readable string.

    Parameters
    ----------
    elapsed : `float`
        The elapsed time in seconds.
    precision : `int`
        The number of decimal places to use, defaults to 2.

    Returns
    -------
    `str`
        The formatted elapsed time.
    """
    ms = elapsed * 1e3
    magnitude = abs(ms)
    if magnitude >= 1e3:
        return f'{ms / 1e3:.{precision}f}s'
    if magnitude >= 1:
        return f'{ms:.{precision}f}ms'
    return f'{ms * 1e3:.{precision}f}μs'
