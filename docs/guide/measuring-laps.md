# Measuring laps

A lap is one measured interval. Instead of a single total, laps let you time
each iteration of a loop separately and then look at the spread across them —
the mean, the slowest one, the deviation.

## Timing each iteration

Wrap the part you want measured in [`sw.lap()`](/api/stopwatch#lap):

```python{5}
from stopwatch import Stopwatch
from time import sleep

sw = Stopwatch(autostart=False)
for delay in [0.1, 0.2, 0.3]:
    with sw.lap():
        sleep(delay)

print(f'total: {sw}')  # total: 600.59ms
for i, lap in enumerate(sw.laps):
    print(f'  lap {i}: {lap.elapsed:.3f}s')
#   lap 0: 0.100s
#   lap 1: 0.200s
#   lap 2: 0.300s
```

Everything outside the `with` block — the loop machinery, whatever else the
iteration does — stays out of the measurement.

## Leaving setup out

A stopwatch starts measuring the moment it is created, and the first `lap()`
takes over that already-running lap rather than opening a second one. That is
what keeps a stray extra lap out of your results, but it also means anything
you do between `Stopwatch()` and the first `lap()` lands in the first lap.

Pass `autostart=False` when the stopwatch should sit idle until the first lap:

```python
sw = Stopwatch(autostart=False)   # [!code focus]
load_config()                     # 0.5s, not measured
with sw.lap():
    do_work()                     # 0.1s

# autostart=False -> lap[0]=0.10s  total=0.10s
# autostart=True  -> lap[0]=0.60s  total=0.60s
```

## Statistics across laps

[`sw.statistics`](/api/statistics) summarises the laps:

```python
from stopwatch import Stopwatch
from time import sleep

sw = Stopwatch(autostart=False)
for delay in [0.1, 0.2, 0.3, 0.4, 0.5]:
    with sw.lap():
        sleep(delay)

stats = sw.statistics
print(len(stats))       # 5
print(stats.mean)       # 0.3
print(stats.minimum)    # 0.1
print(stats.median)     # 0.3
print(stats.maximum)    # 0.5
print(stats.total)      # 1.501
print(stats.stdev)      # 0.141
```

Or get the whole thing as one line with
[`sw.report()`](/api/stopwatch#report):

```python
print(sw.report())
# [Stopwatch] total=1.50s, mean=0.30s, min=0.10s, median=0.30s, max=0.50s, dev=0.14s
```

::: info
`report()` only includes the mean, min, median, max and deviation when there is
more than one lap. With a single lap there is nothing to compare, so it prints
just the total.
:::

## Nesting

Laps nest. Each `lap()` records its own interval, and the outer one still counts
all the time it spans, including the inner block:

```python
sw = Stopwatch(autostart=False)
with sw.lap():
    sleep(0.1)
    with sw.lap():
        sleep(0.2)
    sleep(0.1)

print(len(sw.laps))        # 2
print(sw.laps[0].elapsed)  # 0.4  the outer block
print(sw.laps[1].elapsed)  # 0.2  the inner block
```

This is useful for splitting a step out of a larger one — timing a database
call inside a request, for instance — without losing the total.

## Exceptions

A lap is closed when its block ends, whether it ends normally or by raising.
You do not need a `try`/`finally` of your own:

```python
sw = Stopwatch(autostart=False)
try:
    with sw.lap():
        sleep(0.1)
        raise ValueError('boom')
except ValueError:
    pass

print(sw.running)   # False
print(sw.elapsed)   # 0.1
```

## Starting and stopping by hand

`lap()` is the recommended way, but [`start()`](/api/stopwatch#start) and
[`stop()`](/api/stopwatch#stop) are there when the interval does not map to a
block:

```python
sw = Stopwatch()
sleep(1)
sw.stop()
sleep(1)          # not counted
print(sw.elapsed)  # ~1.0
sw.start()         # opens a new lap
sleep(1)
sw.stop()
print(sw.elapsed)  # ~2.0
print(len(sw.laps))  # 2
```

[`reset()`](/api/stopwatch#reset) throws the laps away and stops the stopwatch;
[`restart()`](/api/stopwatch#restart) resets and starts a fresh lap.
