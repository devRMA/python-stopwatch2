from collections.abc import Callable
from typing import Any


class AtexitMock:
    @staticmethod
    def register(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
