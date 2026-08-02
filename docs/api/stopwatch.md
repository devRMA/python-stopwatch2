---
title: Stopwatch
description: API reference for the Stopwatch class — laps, elapsed time, statistics, reports, and the autostart option.
---

# Stopwatch

Measures elapsed time, as a whole or split into [laps](/api/lap). It starts
counting the moment you create it and can stop itself at the end of a `with`
block.

**Source:** [stopwatch/stopwatch.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/stopwatch.py)

```python
from stopwatch import Stopwatch
```

## At a glance

| What | Members |
|---|---|
| **Create** | [`Stopwatch(name, print_report, precision, autostart)`](#initialization) |
| **Read** | [`elapsed`](#elapsed) · [`running`](#running) · [`laps`](#laps) · [`statistics`](#statistics) · [`str(sw)`](#supported-operations) |
| **Measure** | [`lap()`](#lap) · [`start()`](#start) · [`stop()`](#stop) · [`reset()`](#reset) · [`restart()`](#restart) |
| **Report** | [`report()`](#report) |

## Initialization

```python
def __init__(
    self,
    name: str | None = None,
    print_report: bool = False,
    precision: int = 2,
    autostart: bool = True,
) -> None:
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `name` | `str \| None` | `None` | Label shown in the reports, to tell several stopwatches apart. |
| `print_report` | `bool` | `False` | Print the elapsed time when a `with` block ends. The line is prefixed with `[module:function:line]`, pointing at where the stopwatch was created. |
| `precision` | `int` | `2` | Decimal places used when formatting. Can be changed later. |
| `autostart` | `bool` | `True` | Start counting immediately. Pass `False` to measure only the blocks wrapped in [`lap()`](#lap). |

A stopwatch is already running once created, so the simplest use is create,
work, stop:

```python
from stopwatch import Stopwatch
from time import sleep

sw = Stopwatch()
sleep(2)
sw.stop()
print(sw)  # 2.00s
```

Give it a name and let it report itself:

```python
from stopwatch import Stopwatch
from time import sleep

with Stopwatch('build', print_report=True):
    sleep(1.2)

# [__main__:<module>:4] ~ 1.20s - build
```

The `4` is the line the stopwatch was created on, which is how you tell several
reports in one file apart.

`precision` applies to everything formatted, and is not fixed at creation:

```python
with Stopwatch(precision=3) as sw:
    sleep(0.5)

print(sw)          # 500.118ms
sw.precision = 0
print(sw)          # 500ms
```

## Supported operations

```python
str(sw)   # '2.00s'                 formatted, honours precision
repr(sw)  # <Stopwatch name=None elapsed=0.5001178499987873>
```

`str()` is what f-strings use, so `f'took {sw}'` gives `took 2.00s`, while
[`elapsed`](#elapsed) gives you the raw float.

## Attributes

### name

Label used in the reports. `None` when unnamed. Can be set at any time.

**Type:** `str | None`

```python
with Stopwatch('sw1') as sw:
    ...

print(sw.name)  # sw1
```

### precision

Number of decimal places used when formatting. Defaults to `2`.

**Type:** [`int`](https://docs.python.org/3/library/functions.html#int)

```python
with Stopwatch(precision=1) as sw:
    sleep(1)

print(sw)  # 1.0s
```

### laps

Every lap recorded so far, in order. A stopwatch that has never been started is
empty.

**Type:** `list[`[`Lap`](/api/lap)`]`

```python
sw = Stopwatch(autostart=False)
with sw.lap():
    sleep(1)
with sw.lap():
    sleep(2)

print(len(sw.laps))         # 2
print(sw.laps[0].elapsed)   # 1.0
print(sw.laps[-1].elapsed)  # 2.0
```

### elapsed

Total time in seconds: the sum of every lap. Read it while the stopwatch is
running and it reflects the clock at that moment, so it grows between reads.

**Type:** [`float`](https://docs.python.org/3/library/functions.html#float)

```python
with Stopwatch() as sw:
    sleep(1)

print(sw.elapsed)  # 1.000208768000448
print(sw)          # 1.00s
```

### running

`True` while any lap is running. This includes the lap opened by a
[`lap()`](#lap) block, so it is `True` inside one.

**Type:** [`bool`](https://docs.python.org/3/library/functions.html#bool)

```python
sw = Stopwatch()
print(sw.running)                          # True
sw.stop()
print(sw.running)                          # False

print(Stopwatch(autostart=False).running)  # False
```

### statistics

A [`Statistics`](/api/statistics) over the lap durations, rebuilt each time you
read it.

**Type:** [`Statistics`](/api/statistics)

```python
sw = Stopwatch(autostart=False)
for c in range(1, 6):
    with sw.lap():
        sleep(c / 10)

stats = sw.statistics
print(len(stats))        # 5
print(stats.mean)        # 0.3
print(stats.minimum)     # 0.1
print(stats.maximum)     # 0.5
print(stats.stdev)       # 0.1414213562373095
```

## Methods

### lap

```python
@contextmanager
def lap(self) -> Iterator[None]:
```

Records the block it wraps as its own [lap](/api/lap). This is the main way to
measure: one lap per iteration, per step, per request.

The lap is closed when the block ends, **including when the block raises**, so a
failure cannot leave a lap running and skew every later reading. Nesting works
too — each call records a distinct lap and the outer one still counts the time it
spans.

```python
sw = Stopwatch(autostart=False)
for i in range(5):
    with sw.lap():  # [!code focus]
        sleep(i / 10)

print(sw)            # 1.00s
print(len(sw.laps))  # 5
```

Nested, each keeping its own time:

```python
sw = Stopwatch(autostart=False)
with sw.lap():
    sleep(0.1)
    with sw.lap():
        sleep(0.2)
    sleep(0.1)

print(len(sw.laps))        # 2
print(sw.laps[0].elapsed)  # 0.4  the outer block, inner one included
print(sw.laps[1].elapsed)  # 0.2  the inner block
```

Closed even when the block raises:

```python
sw = Stopwatch(autostart=False)
try:
    with sw.lap():
        sleep(0.1)
        raise ValueError('boom')
except ValueError:
    pass

sleep(0.3)
print(sw.running)  # False
print(sw.elapsed)  # 0.1   does not keep growing
```

::: warning The first lap and `autostart`
A stopwatch starts counting when it is created, and the first `lap()` takes over
that already-running lap rather than opening a second one — otherwise the time
already on the clock would show up as a phantom extra lap. The consequence is
that work done between `Stopwatch()` and the first `lap()` lands in the first
lap. Build it with `autostart=False` when you only want the `lap()` blocks
measured.
:::

### start

```python
def start(self) -> Stopwatch:
```

Starts the stopwatch by opening a new lap. Does nothing if it is already
running. Called for you at creation, unless you pass
[`autostart=False`](#initialization).

**Returns** the same instance, so it chains.

### stop

```python
def stop(self) -> Stopwatch:
```

Stops the current lap, freezing the duration. Called for you when a `with` block
ends.

**Returns** the same instance.

```python
sw = Stopwatch()
sleep(2)
sw.stop()
print(sw.elapsed)    # 2.0
sleep(1)             # not counted
print(sw.elapsed)    # 2.0
sw.start()           # opens a second lap
sleep(1)
sw.stop()
print(sw.elapsed)    # 3.0
print(len(sw.laps))  # 2
```

### reset

```python
def reset(self) -> Stopwatch:
```

Stops the stopwatch and throws every lap away, back to zero.

**Returns** the same instance.

```python
with Stopwatch() as sw:
    sleep(0.2)

print(sw.elapsed)    # 0.2
sw.reset()
print(sw.elapsed)    # 0.0
print(len(sw.laps))  # 0
print(sw.running)    # False
```

### restart

```python
def restart(self) -> Stopwatch:
```

[`reset()`](#reset) followed by [`start()`](#start): back to zero and counting
again. This is what entering a `with` block does.

**Returns** the same instance.

```python
sw = Stopwatch()
sleep(0.2)
print(sw)            # 200.15ms
sw.restart()
sleep(0.2)
sw.stop()
print(sw)            # 200.10ms
print(len(sw.laps))  # 1
```

### report

```python
def report(self) -> str:
```

A one-line summary of the laps, using [`precision`](#precision) for every
number. With a single lap there is nothing to compare, so only the total is
included.

**Returns** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

```python
sw = Stopwatch(autostart=False)
for i in range(5):
    with sw.lap():
        sleep(i / 10)

print(sw.report())
# [Stopwatch] total=1.00s, mean=0.20s, min=0.00s, median=0.20s, max=0.40s, dev=0.14s
```

One lap, named:

```python
sw = Stopwatch('etl')
sleep(0.3)
sw.stop()

print(sw.report())
# [Stopwatch#etl] total=0.30s
```

## See also

- [Measuring laps](/guide/measuring-laps) — the guide, with the reasoning behind
  laps.
- [`Lap`](/api/lap) — what each entry of [`laps`](#laps) is.
- [`Statistics`](/api/statistics) — what [`statistics`](#statistics) returns.
- [`profile`](/api/decorators#profile) — the same measurements, per function
  call.
