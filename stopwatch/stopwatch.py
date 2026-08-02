from __future__ import annotations

import math
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

from colorama import Fore, Style

from .lap import Lap
from .statistics import Statistics
from .utils import Caller, format_elapsed_time, inspect_caller


class Stopwatch:
    def __init__(
        self,
        name: str | None = None,
        print_report: bool = False,
        precision: int = 2,
        autostart: bool = True,
    ) -> None:
        """
        Parameters
        ----------
        name : Optional[`str`]
            The name shown in the reports.
        print_report : `bool`
            Print a report when leaving a `with` block. Default is False.
        precision : `int`
            The number of decimal places in the reports. Default is 2.
        autostart : `bool`
            Start measuring right away. Default is True. Pass False to
            measure only the blocks wrapped in `lap()`, leaving the time
            before the first one out.
        """
        self.name = name
        self.precision = precision
        self.laps: list[Lap] = []
        self._current_lap: Lap | None = None
        self._print_report = print_report
        self._caller: Caller | None = (
            inspect_caller() if print_report else None
        )
        if autostart:
            self.start()

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
        return any(lap.running for lap in self.laps)

    @property
    def statistics(self) -> Statistics:
        """`Statistics`: The statistics from stopwatch."""
        return Statistics(values=[lap.elapsed for lap in self.laps])

    @contextmanager
    def lap(self) -> Iterator[None]:
        """
        Context manager that records the block it wraps as its own lap.

        Each call records a distinct lap, so nesting works and the lap is
        always closed even if the block raises.

        A stopwatch is already running once constructed, and the first lap
        takes over that lap rather than opening a second one, so any time
        between `Stopwatch()` and the first `lap()` belongs to it. Build it
        with `autostart=False` to leave that time out.
        """
        lap = self._take_running_lap() or self._open_lap()
        try:
            yield
        finally:
            lap.stop()

    def _open_lap(self) -> Lap:
        lap = Lap()
        self.laps.append(lap)
        lap.start()
        return lap

    def _take_running_lap(self) -> Lap | None:
        lap = self._current_lap
        self._current_lap = None
        return lap if lap is not None and lap.running else None

    def start(self) -> Stopwatch:
        """
        Starts the stopwatch.

        Returns
        -------
        `Stopwatch`
            The started stopwatch instance.
        """
        if not self.running:
            self._current_lap = self._open_lap()
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
                    f'dev={math.sqrt(statistics.variance):.{self.precision}f}s',
                ]
            )

        return '[Stopwatch{tag}] {statistics}'.format(
            tag=f'#{self.name}' if self.name is not None else '',
            statistics=', '.join(items),
        )

    def _format(self) -> str:
        caller = self._caller
        if self._print_report and caller is not None:
            items = [
                Style.BRIGHT,
                Fore.BLUE,
                f'[{caller.module}:{caller.function}:{caller.line_number}]',
                Style.RESET_ALL,
                ' ~ ',
                Style.BRIGHT,
                Fore.MAGENTA,
                format_elapsed_time(self.elapsed, self.precision),
                Style.RESET_ALL,
            ]

            if self.name is not None:
                items += [' - ', self.name]

            return ''.join(items)
        return ''
