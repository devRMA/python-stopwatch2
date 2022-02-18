# Decorators

**Source code: [stopwatch/profile.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/profile.py)**

[[toc]]

## profile

This decorator is used to profiling the execution time of a function.

**Parameters**

- `name`: The name used for the statistics.
  - Type: [str](https://docs.python.org/3/library/stdtypes.html#str)
  - Default: Name of decorated function
- report_every: The number of times to report the statistics. If None is passed, the report will only be printed at the end of the execution.
  - Type: Optional[[int](https://docs.python.org/3/library/functions.html#int)]
  - Default: 1

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
# [__main__#My function] hits=5, mean=300.35ms, min=100.14ms, median=300.35ms, max=500.55ms, dev=141.56ms
```

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

:::
