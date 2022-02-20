import atexit
import functools
import math
from typing import Any, Callable, TypeVar

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
            Style.BRIGHT, f'{Fore.BLUE}[{caller.module}',
            f'{Fore.GREEN}#{name}', f'{Fore.BLUE}]', Fore.RESET
        ]
    )
    items = ', '.join(
        [
            f'hits={len(statistics)}',
            f'mean={format_elapsed_time(statistics.mean)}',
            f'min={format_elapsed_time(statistics.minimum)}',
            f'median={format_elapsed_time(statistics.median)}',
            f'max={format_elapsed_time(statistics.maximum)}',
            f'dev={format_elapsed_time(math.sqrt(statistics.variance))}'
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


def profile(**kwargs: Any) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
    """
    Decorator for profiling the function.

    Parameters
    ----------
    name : Optional[`str`]
        The name for the statistics. Default is the name of function.
    report_every : Optional[`int`]
        The number of times to report the statistics. Default is 1.
    """
    caller = inspect_caller()

    def decorator(func: Callable[..., RT]) -> Callable[..., RT]:
        name: str = kwargs.get('name', func.__name__)
        report_every: int = kwargs.get('report_every', 1)
        should_report = report_every is not None

        statistics = Statistics()
        atexit.register(_print_report, caller, name, statistics)

        @functools.wraps(func)
        def wrapper(*args: object, **kwargs: object) -> RT:
            with Stopwatch() as stopwatch:
                result = func(*args, **kwargs)

            statistics.add(stopwatch.elapsed)
            if should_report and (len(statistics) % report_every) == 0:
                _print_report(caller, name, statistics)

            return result

        return wrapper

    return decorator
