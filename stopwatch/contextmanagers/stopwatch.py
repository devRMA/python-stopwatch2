import sys
from typing import Any, Optional

from ..stopwatch import Stopwatch
from . import Caller, format_elapsed_time, inspect_caller


# TODO : Think of a better name
# pylint: disable=invalid-name
class stopwatch:
    _message: Optional[str]
    _caller: Caller
    _stopwatch: Stopwatch

    def __init__(self, message: Optional[str] = None) -> None:
        self._message = message
        self._caller = inspect_caller()
        self._stopwatch = Stopwatch()

    def __enter__(self) -> None:
        self._stopwatch.start()

    def __exit__(self, exc_type: Any, exc_value: Any,
                 exc_traceback: Any) -> None:
        self._stopwatch.stop()
        print(self._format(self._message, self._caller,
                           self._stopwatch.elapsed),
              file=sys.stderr)

    @staticmethod
    def _format(message: Optional[str], caller: Caller, elapsed: float) -> str:
        # TODO : back with the colored print using colorama
        items = [
            f'[{caller.module}:{caller.function}:{caller.line_number}]', ' ~ ',
            format_elapsed_time(elapsed)
        ]

        if message is not None:
            items += [' - ', message]

        return ''.join(items)
