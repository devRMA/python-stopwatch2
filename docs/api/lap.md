---
title: Lap
description: API reference for the Lap class — a single measured interval inside a Stopwatch.
---

# Lap

A single measured interval. You do not create these: a
[`Stopwatch`](/api/stopwatch) opens one when it starts and one for each
[`lap()`](/api/stopwatch#lap) block, and hands them to you through
[`laps`](/api/stopwatch#laps).

**Source:** [stopwatch/lap.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/lap.py)

```python
sw = Stopwatch(autostart=False)
with sw.lap():
    sleep(1)

lap = sw.laps[0]
print(lap.elapsed)  # 1.0001530810004624
print(lap.running)  # False
print(repr(lap))    # <Lap running=False elapsed=1.0002>
```

A `Lap` can itself be stopped and started again, accumulating each stretch into
its `elapsed`. `Stopwatch` never does that, though — every
[`start()`](/api/stopwatch#start) opens a new lap, so
[`stop()`](/api/stopwatch#stop) followed by `start()` gives you two entries in
[`laps`](/api/stopwatch#laps) rather than one resumed lap.

## Supported operations

```python
repr(lap)  # <Lap running=False elapsed=1.0001>
```

## Attributes

### running

Whether the lap is currently counting.

**Type:** [`bool`](https://docs.python.org/3/library/functions.html#bool)

### elapsed

The measured time in seconds. While the lap is running this is computed against
the current clock, so it grows between reads; once stopped it is frozen.

**Type:** [`float`](https://docs.python.org/3/library/functions.html#float)

## Methods

::: danger Use the Stopwatch instead
These exist because `Stopwatch` needs them. Driving a `Lap` by hand bypasses the
stopwatch's bookkeeping, so its [`laps`](/api/stopwatch#laps) and
[`elapsed`](/api/stopwatch#elapsed) stop agreeing with reality. Use
[`Stopwatch.lap()`](/api/stopwatch#lap), [`start()`](/api/stopwatch#start) and
[`stop()`](/api/stopwatch#stop).
:::

### start

```python
def start(self) -> None:
```

Starts counting.

### stop

```python
def stop(self) -> None:
```

Stops counting and freezes the duration. Calling it on a lap that is already
stopped does nothing.

## See also

- [`Stopwatch.laps`](/api/stopwatch#laps) — the list these live in.
- [Measuring laps](/guide/measuring-laps) — the guide.
