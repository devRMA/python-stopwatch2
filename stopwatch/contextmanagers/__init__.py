import inspect
from typing import NamedTuple


class Caller(NamedTuple):
    module: str
    function: str
    line_number: int


def inspect_caller(offset: int = 0) -> Caller:
    stack = inspect.stack()[2 + offset]
    module = inspect.getmodule(stack.frame)
    return Caller(module=module.__name__ if module else '<unknown>',
                  function=stack.function,
                  line_number=stack.lineno)


def format_elapsed_time(elapsed: float) -> str:
    """
    Format the elapsed time in seconds to a human readable string.

    Parameters
    ----------
    elapsed : `float`
        The elapsed time in seconds.

    Returns
    -------
    `str`
        The formatted elapsed time.
    """
    ms = elapsed * 1000
    if ms >= 1e3:
        return f'{ms / 1e3:.2f}s'
    if ms >= 1:
        return f'{ms:.2f}ms'
    return f'{ms * 1e3:.2f}μs'
