from __future__ import annotations

import math
from contextlib import contextmanager
from typing import Any, Iterator, List, Optional

from colorama import Fore, Style

from .lap import Lap
from .statistics import Statistics
from .utils import Caller, format_elapsed_time, inspect_caller


class Stopwatch:
    name: Optional[str] = None
    precision: int = 2
    laps: List[Lap] = []
    _caller: Optional[Caller] = None
    _current_lap: Optional[Lap] = None
    _print_report: bool = False

    def __init__(
        self,
        name: Optional[str] = None,
        print_report: bool = False,
        precision: int = 2
    ) -> None:
        self.name = name
        self.precision = precision
        if print_report:
            self._print_report = print_report
            self._caller = inspect_caller()
        self.restart()

    def __enter__(self) -> Stopwatch:
        return self.restart()

    def __exit__(
        self, exc_type: Any, exc_value: Any, exc_traceback: Any
    ) -> None:
        self.stop()
        if self._print_report:
            print(self._format())

    def __str__(self) -> str:
        return format_elapsed_time(self.elapsed, self.precision)

    def __repr__(self) -> str:
        return f'<Stopwatch name={self.name} elapsed={self.elapsed}>'

    @property
    def elapsed(self) -> float:
        """`float`: The elapsed time in seconds."""
        return float(sum(lap.elapsed for lap in self.laps))

    @property
    def running(self) -> bool:
        """`bool`: True if the stopwatch is running, False if stopped."""
        return self._current_lap is not None and self._current_lap.running

    @property
    def statistics(self) -> Statistics:
        """`Statistics`: The statistics from stopwatch."""
        return Statistics(values=[lap.elapsed for lap in self.laps])

    @contextmanager
    def lap(self) -> Iterator[None]:
        """
        Context manager for add a new lap.
        """
        # calling start twice consecutively -> use stack to solve this problem
        self.start()
        yield
        self.stop()

    def start(self) -> Stopwatch:
        """
        Starts the stopwatch.

        Returns
        -------
        `Stopwatch`
            The started stopwatch instance.
        """
        if not self.running:
            self.laps.append(Lap())
            self._current_lap = self.laps[-1]
            self._current_lap.start()
        return self

    def stop(self) -> Stopwatch:
        """
        Stops the stopwatch, freezing the duration.

        Returns
        -------
        `Stopwatch`
            The stopped stopwatch instance.
        """
        if self._current_lap is not None:
            self._current_lap.stop()
            self._current_lap = None
        return self

    def reset(self) -> Stopwatch:
        """
        Resets the Stopwatch to 0 duration.

        Returns
        -------
        `Stopwatch`
            The resetted stopwatch instance.
        """
        self.stop()
        self.laps = []
        return self

    def restart(self) -> Stopwatch:
        """
        Reset and start the stopwatch.

        Returns
        -------
        `Stopwatch`
            The restarted stopwatch instance.
        """
        return self.reset().start()

    def report(self) -> str:
        """
        Return a report of the stopwatch statistics.

        Returns
        -------
        `str`
            The report.
        """
        statistics = self.statistics

        items = [f'total={statistics.total:.{self.precision}f}s']
        if len(statistics) > 1:
            items.extend(
                [
                    f'mean={statistics.mean:.{self.precision}f}s',
                    f'min={statistics.minimum:.{self.precision}f}s',
                    f'median={statistics.median:.{self.precision}f}s',
                    f'max={statistics.maximum:.{self.precision}f}s',
                    f'dev={math.sqrt(statistics.variance):.{self.precision}f}s'
                ]
            )

        return '[Stopwatch{tag}] {statistics}'.format(
            tag=f'#{self.name}' if self.name is not None else '',
            statistics=', '.join(items)
        )

    def _format(self) -> str:
        caller = self._caller
        if self._print_report and caller is not None:
            items = [
                Style.BRIGHT, Fore.BLUE,
                f'[{caller.module}:{caller.function}:{caller.line_number}]',
                Style.RESET_ALL, ' ~ ', Style.BRIGHT, Fore.MAGENTA,
                format_elapsed_time(self.elapsed,
                                    self.precision), Style.RESET_ALL
            ]

            if self.name is not None:
                items += [' - ', self.name]

            return ''.join(items)
        return ''
