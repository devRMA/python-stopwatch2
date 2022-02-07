from __future__ import annotations

import math
import time
from contextlib import contextmanager
from typing import Any, Iterator, List, Optional

from .contextmanagers import format_elapsed_time
from .statistics import Statistics


class Lap:
    running: bool
    _start: float
    _fractions: List[float]

    def __init__(self) -> None:
        self.running = False
        self._start = 0.0
        self._fractions = []

    def __repr__(self) -> str:
        return f'Lap(running={self.running}, elapsed={self.elapsed:.4f})'

    @property
    def elapsed(self) -> float:
        """`float`: Return the elapsed time in seconds."""
        return ((time.perf_counter() -
                 self._start) if self.running else 0.0) + sum(self._fractions)

    def start(self) -> None:
        """
        Start the lap timer.
        """
        self.running = True
        self._start = time.perf_counter()

    def stop(self) -> None:
        """
        Stop the lap timer.
        """
        self._fractions.append(time.perf_counter() - self._start)
        self._start = 0.0
        self.running = False


class Stopwatch:
    name: Optional[str] = None
    _laps: List[Lap] = []
    _current_lap: Optional[Lap] = None

    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name
        self.restart()

    def __enter__(self) -> Stopwatch:
        return self.restart()

    def __exit__(self, exc_type: Any, exc_value: Any,
                 exc_traceback: Any) -> None:
        self.stop()

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
