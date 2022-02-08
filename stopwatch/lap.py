import time
from typing import List


class Lap:
    running: bool
    _start: float
    _fractions: List[float]

    def __init__(self) -> None:
        self.running = False
        self._start = 0.0
        self._fractions = []

    def __repr__(self) -> str:
        return f'<Lap running={self.running} elapsed={self.elapsed:.4f}>'

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
