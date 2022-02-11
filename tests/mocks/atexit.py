from typing import Any, Callable


class AtexitMock:
    @staticmethod
    def register(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
