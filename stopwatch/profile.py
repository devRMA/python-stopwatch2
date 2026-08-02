import atexit
import functools
import inspect
from collections.abc import Callable
from typing import Any, TypeVar, cast

from colorama import Fore, Style

from .statistics import Statistics
from .stopwatch import Stopwatch
from .utils import Caller, format_elapsed_time, inspect_caller

RT = TypeVar('RT')  # return type


def _make_report(caller: Caller, name: str, statistics: Statistics) -> str:
    """
    Return a report of the stopwatch statistics.

    Parameters
    ----------
    caller : `Caller`
        The caller.
    name : `str`
        The name for report.
    statistics : `Statistics`
        The statistics object.

    Returns
    -------
    `str`
        The report string.
    """
    tag = ''.join(
        [
            Style.BRIGHT,
            f'{Fore.BLUE}[{caller.module}',
            f'{Fore.GREEN}#{name}',
            f'{Fore.BLUE}]',
            Fore.RESET,
        ]
    )
    items = ', '.join(
        [
            f'hits={len(statistics)}',
            f'mean={format_elapsed_time(statistics.mean)}',
            f'min={format_elapsed_time(statistics.minimum)}',
            f'median={format_elapsed_time(statistics.median)}',
            f'max={format_elapsed_time(statistics.maximum)}',
            f'dev={format_elapsed_time(statistics.stdev)}',
        ]
    )

    return f'{tag} {items}'


def _print_report(caller: Caller, name: str, statistics: Statistics) -> None:
    """
    Print a report of the stopwatch statistics.

    Parameters
    ----------
    caller : `Caller`
        The caller.
    name : `str`
        The name for printing.
    statistics : `Statistics`
        The statistics object.
    """
    if len(statistics) > 0:
        print(_make_report(caller, name, statistics))


def profile(
    *,
    name: str | None = None,
    report_every: int | None = 1,
) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
    """
    Decorator for profiling the function. Must be called: `@profile()`.

    Works on regular and `async def` functions. Generator functions are
    not supported -- see the note below.

    Parameters
    ----------
    name : Optional[`str`]
        The name for the statistics. Default is the name of function.
    report_every : Optional[`int`]
        Report once every this many calls, or `None` to only report when
        the process exits. Default is 1.

    Raises
    ------
    `ValueError`
        If `report_every` is smaller than 1.

    ponytail: a generator function is measured only for the time it takes
    to build the generator, not to consume it, because there is no way to
    time the consumption without changing the function's semantics.
    ponytail: every recorded call is kept, because the median needs all
    the values, and the atexit registration holds them until the process
    exits (~3MB per 100k calls). Cap it with a reservoir sample, or drop
    the median, if profiling a hot function over a long run.
    """
    if report_every is not None and report_every < 1:
        raise ValueError(
            f'report_every must be >= 1 or None, got {report_every}'
        )

    caller = inspect_caller()

    def decorator(func: Callable[..., RT]) -> Callable[..., RT]:
        stat_name = func.__name__ if name is None else name
        statistics = Statistics()

        def record(elapsed: float) -> None:
            statistics.add(elapsed)
            if (
                report_every is not None
                and len(statistics) % report_every == 0
            ):
                _print_report(caller, stat_name, statistics)

        def report_at_exit() -> None:
            # Skip when the inline report above already covered this call
            # count, which otherwise printed the same line twice.
            if report_every is None or len(statistics) % report_every != 0:
                _print_report(caller, stat_name, statistics)

        atexit.register(report_at_exit)

        if inspect.iscoroutinefunction(func):

            @functools.wraps(func)
            async def async_wrapper(*args: object, **kwargs: object) -> Any:
                stopwatch = Stopwatch()
                try:
                    return await func(*args, **kwargs)
                finally:
                    record(stopwatch.stop().elapsed)

            return cast('Callable[..., RT]', async_wrapper)

        @functools.wraps(func)
        def wrapper(*args: object, **kwargs: object) -> RT:
            stopwatch = Stopwatch()
            try:
                return func(*args, **kwargs)
            finally:
                # In a finally, so a call that raises is still recorded.
                record(stopwatch.stop().elapsed)

        return wrapper

    return decorator
