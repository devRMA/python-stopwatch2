---
title: Profiling a function
description: Measure every call to a function with the profile decorator, including async def, with periodic statistics reports.
---

# Profiling a function

Use the [profile](/api/decorators#profile) decorator to measure every call to a
function. By default it prints a running report on each call, so you watch the
numbers settle as the function is exercised.

```python{5}
from stopwatch import profile
from time import sleep


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

Reporting on every call gets noisy for a function called often. Pass
`report_every` to report periodically, or `None` to report only once when the
process exits:

```python
@profile(report_every=100)
def hot_path() -> None:
    ...

@profile(report_every=None)
def quiet() -> None:
    ...
```

`async def` functions work too, and are measured across the `await` rather than
just the creation of the coroutine:

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

A call that raises is still recorded, so a function that starts failing does not
quietly vanish from the report.

::: tip
Need to measure part of a function rather than the whole thing? Use
[laps](/guide/measuring-laps) instead.
:::
