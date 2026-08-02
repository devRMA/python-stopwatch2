---
title: profile decorator
description: API reference for the profile decorator — measure every call to a function, including async def, with periodic statistics reports.
---

# Decorators

**Source:** [stopwatch/profile.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/profile.py)

## profile

Measures every call to a function and prints the statistics as they build up.
Reach for it when you want to know what a function costs across a whole run,
rather than timing one specific block.

```python
def profile(
    *,
    name: str | None = None,
    report_every: int | None = 1,
) -> Callable[[Callable[..., RT]], Callable[..., RT]]:
```

```python
from time import sleep
from stopwatch import profile


@profile()
def parse(n: int) -> None:
    sleep(n / 100)


for n in (8, 12, 10):
    parse(n)

# [__main__#parse] hits=1, mean=80.13ms, min=80.13ms, median=80.13ms, max=80.13ms, dev=0.00μs
# [__main__#parse] hits=2, mean=100.19ms, min=80.13ms, median=100.19ms, max=120.24ms, dev=20.06ms
# [__main__#parse] hits=3, mean=100.16ms, min=80.13ms, median=100.11ms, max=120.24ms, dev=16.38ms
```

The prefix is `[module#name]`, and `hits` is the number of calls so far.

### Parameters

Both are keyword-only, so a misspelled name fails loudly instead of being
quietly ignored.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `name` | `str \| None` | `None` | Label for the report. Defaults to the function's own name. |
| `report_every` | `int \| None` | `1` | Print a report every N calls. `None` prints only once, when the process exits. |

**Raises** [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError)
if `report_every` is below 1:

```python
profile(report_every=0)
# ValueError: report_every must be >= 1 or None, got 0
```

::: warning It has to be called
Write `@profile()`, not `@profile`. Without the parentheses you get
`TypeError: profile() takes 0 positional arguments but 1 was given`.
:::

### Reporting less often

Reporting on every call gets noisy for a function called thousands of times.

```python
from time import sleep
from stopwatch import profile


@profile(report_every=2)
def every_two(t: float) -> None:
    sleep(t)


@profile(report_every=None)
def only_at_exit(t: float) -> None:
    sleep(t)


for t in [0.1, 0.2, 0.3, 0.4, 0.5]:
    every_two(t)
    only_at_exit(t)
print('end')

# [__main__#every_two] hits=2, mean=150.12ms, min=100.14ms, median=150.12ms, max=200.10ms, dev=49.98ms
# [__main__#every_two] hits=4, mean=250.12ms, min=100.14ms, median=250.11ms, max=400.10ms, dev=111.80ms
# end
# [__main__#only_at_exit] hits=5, mean=300.10ms, min=100.12ms, median=300.08ms, max=500.10ms, dev=141.41ms
# [__main__#every_two] hits=5, mean=300.12ms, min=100.14ms, median=300.13ms, max=500.13ms, dev=141.42ms
```

The last two lines are printed as the process exits. `every_two` gets one
because its fifth call was not covered by a periodic report; with the default
`report_every=1`, every call is already reported and nothing is left to print at
exit.

### async def

Coroutine functions are measured across the `await`, not just the moment the
coroutine is created.

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

### Calls that raise

Still recorded, so a function that starts failing does not quietly disappear
from the report — which matters, because those are usually the calls worth
looking at.

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

### Limitations

::: warning Generator functions
A generator function is measured only for the time it takes to *build* the
generator, which is almost nothing — not for consuming it. Timing the
consumption would change what the function does. Wrap the loop that consumes it
in a [`lap()`](/api/stopwatch#lap) instead:

```python
sw = Stopwatch(autostart=False)
with sw.lap():
    for row in rows():
        handle(row)
```
:::

::: info Memory
Every recorded duration is kept, because the median needs all of them, and the
exit report holds them until the process ends — roughly 3 MB per 100 000 calls
per decorated function. Fine for a script or a test run; for a hot path in a
long-lived process, prefer a [`lap()`](/api/stopwatch#lap) you control.
:::

## See also

- [Profiling a function](/guide/profiling-function) — the guide.
- [`Stopwatch.lap()`](/api/stopwatch#lap) — measuring a block instead of a whole
  function.
- [`Statistics`](/api/statistics) — the numbers behind the report.
