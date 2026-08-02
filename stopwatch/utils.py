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
    # sys._getframe over inspect.stack(): stack() builds a FrameInfo for
    # every frame on the stack and reads each one's source file to attach
    # context, which costs ~376us for a 23-frame stack against ~3.5us
    # here. This is a library for measuring performance, so the cost of
    # the instrument lands in the measurement. The stdlib's own logging
    # module uses sys._getframe for the same reason.
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
    # Compare on the magnitude: a negative elapsed time fails every `>=`
    # below and would otherwise be rendered in microseconds, so -1h came
    # out as '-3600000000.00us'.
    magnitude = abs(ms)
    if magnitude >= 1e3:
        return f'{ms / 1e3:.{precision}f}s'
    if magnitude >= 1:
        return f'{ms:.{precision}f}ms'
    return f'{ms * 1e3:.{precision}f}μs'
