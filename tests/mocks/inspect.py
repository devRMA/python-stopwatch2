from dataclasses import dataclass
from typing import List


@dataclass
class StackMock:
    frame: str
    function: str
    lineno: int


class InspectMock:
    @staticmethod
    def stack() -> List[StackMock]:
        return [
            StackMock(frame='frame', function='function', lineno=2)
            for _ in range(3)
        ]
