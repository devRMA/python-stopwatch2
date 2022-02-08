from __future__ import annotations

import math
from contextlib import contextmanager
from typing import Any, Iterator, List, Optional

from .lap import Lap
from .statistics import Statistics
from .utils import format_elapsed_time, Caller, inspect_caller


class Stopwatch:
    name: Optional[str] = None
    _caller: Optional[Caller] = None
    _laps: List[Lap] = []
    _current_lap: Optional[Lap] = None
    _print_report: bool = False

    def __init__(self,
                 name: Optional[str] = None,
                 print_report: bool = False) -> None:
        self.name = name
        if print_report:
            self.print_report = print_report
            self._caller = inspect_caller()
        self.restart()

    def __enter__(self) -> Stopwatch:
        return self.restart()

    def __exit__(self, exc_type: Any, exc_value: Any,
                 exc_traceback: Any) -> None:
        self.stop()
        if self.print_report:
            print(self._format())

    def __str__(self) -> str:
        return format_elapsed_time(self.elapsed)

    def __repr__(self) -> str:
        return f'Stopwatch(name={self.name}, elapsed={self.elapsed})'

    @property
    def laps(self) -> List[float]:
        """List[`float`]: The list of duration of laps."""
        return [lap.elapsed for lap in self._laps]

    @property
    def elapsed(self) -> float:
        """`float`: The elapsed time in seconds."""
        return float(sum(self.laps))

    @property
    def running(self) -> bool:
        """`bool`: True if the stopwatch is running, False if stopped."""
        return self._current_lap is not None and self._current_lap.running

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
            self._laps.append(Lap())
            self._current_lap = self._laps[-1]
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
        self._laps = []
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
        statistics = Statistics(values=self.laps)

        items = [f'total={statistics.total:.4f}s']
        if len(statistics) > 1:
            items.extend([
                f'mean={statistics.mean:.4f}s',
                f'min={statistics.minimum:.4f}s',
                f'median={statistics.median:.4f}s',
                f'max={statistics.maximum:.4f}s',
                f'dev={math.sqrt(statistics.variance):.4f}s'
            ])

        return '[Stopwatch{tag}] {statistics}'.format(
            tag=f'#{self.name}' if self.name is not None else '',
            statistics=', '.join(items))

    def _format(self) -> str:
        caller = self._caller
        # TODO : back with the colored print using colorama
        if self.print_report and caller is not None:
            items = [
                f'[{caller.module}:{caller.function}:{caller.line_number}]',
                ' ~ ',
                format_elapsed_time(self.elapsed)
            ]

            if self.name is not None:
                items += [' - ', self.name]

            return ''.join(items)
        return ''
