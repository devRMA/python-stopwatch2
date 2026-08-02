# Decorators

**Source code: [stopwatch/profile.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/profile.py)**

## profile

This decorator is used to profiling the execution time of a function.

```python
def profile(
    *,
    name: str | None = None,
    report_every: int | None = 1,
) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
```

**Parameters**

Both are keyword-only, so a misspelled name is an error instead of being
silently ignored.

- `name`: The name used for the statistics.
  - Type: [str](https://docs.python.org/3/library/stdtypes.html#str) | None
  - Default: Name of decorated function
- `report_every`: Report once every this many calls. If None is passed, the report will only be printed at the end of the execution.
  - Type: [int](https://docs.python.org/3/library/functions.html#int) | None
  - Default: 1

**Raises**

- [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError): if `report_every` is smaller than 1.

::: info
The decorator must be called, so write `@profile()` and not `@profile`.
:::

::: warning
A generator function is measured only for the time it takes to build the
generator, not to consume it, because timing the consumption would change what
the function does. Wrap the loop that consumes it in a
[lap](/api/stopwatch#lap) instead.
:::

::: details Example

```python
from time import sleep
from stopwatch import profile

@profile(name='My function')
def wait_for(time: float) -> None:
    sleep(time)

for time in [0.1, 0.2, 0.3, 0.4, 0.5]:
    wait_for(time)
print('end')

# [__main__#My function] hits=1, mean=100.14ms, min=100.14ms, median=100.14ms, max=100.14ms, dev=0.00μs
# [__main__#My function] hits=2, mean=150.20ms, min=100.14ms, median=150.20ms, max=200.26ms, dev=50.06ms
# [__main__#My function] hits=3, mean=200.25ms, min=100.14ms, median=200.26ms, max=300.35ms, dev=81.74ms
# [__main__#My function] hits=4, mean=250.30ms, min=100.14ms, median=250.30ms, max=400.44ms, dev=111.92ms
# [__main__#My function] hits=5, mean=300.35ms, min=100.14ms, median=300.35ms, max=500.55ms, dev=141.56ms
# end
```

::: info
With the default `report_every=1` every call is reported, so nothing is left to
print when the process exits. The exit report only fires when the last calls
were not covered by an inline report, as in the `report_every=2` example below.
:::

<br>

```python
from time import sleep
from stopwatch import profile

@profile(report_every=2)
def report_every2(time: float) -> None:
    sleep(time)

@profile(report_every=None)
def no_report(time: float) -> None:
    sleep(time)

for time in [0.1, 0.2, 0.3, 0.4, 0.5]:
    report_every2(time)
    no_report(time)
print('end')

# [__main__#report_every2] hits=2, mean=150.20ms, min=100.15ms, median=150.20ms, max=200.25ms, dev=50.05ms
# [__main__#report_every2] hits=4, mean=250.30ms, min=100.15ms, median=250.30ms, max=400.46ms, dev=111.92ms
# end
# [__main__#no_report] hits=5, mean=300.36ms, min=100.15ms, median=300.36ms, max=500.58ms, dev=141.57ms
# [__main__#report_every2] hits=5, mean=300.43ms, min=100.15ms, median=300.36ms, max=500.94ms, dev=141.68ms
```

<br>

`async def` functions are measured across the `await`, not just the creation of
the coroutine:

```python
import asyncio
from stopwatch import profile

@profile(name='fetch')
async def fetch() -> str:
    await asyncio.sleep(0.2)
    return 'ok'

asyncio.run(fetch())

# [__main__#fetch] hits=1, mean=200.47ms, min=200.47ms, median=200.47ms, max=200.47ms, dev=0.00μs
```

<br>

A call that raises is still recorded, so a function that fails does not
disappear from the report:

```python
from time import sleep
from stopwatch import profile

@profile(name='flaky')
def flaky() -> None:
    sleep(0.1)
    raise RuntimeError('nope')

for _ in range(2):
    try:
        flaky()
    except RuntimeError:
        pass

# [__main__#flaky] hits=1, mean=100.13ms, min=100.13ms, median=100.13ms, max=100.13ms, dev=0.00μs
# [__main__#flaky] hits=2, mean=100.12ms, min=100.11ms, median=100.12ms, max=100.13ms, dev=8.48μs
```

:::
