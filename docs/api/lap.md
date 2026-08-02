# Lap

**Source code: [stopwatch/lap.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/lap.py)**

A single measured interval. You do not create these yourself: a
[Stopwatch](/api/stopwatch) creates one when it starts and one for each
[lap](/api/stopwatch#lap) block, and exposes them through
[laps](/api/stopwatch#laps).

## Supported operations

```python
repr(lap)  # <Lap running=False elapsed=1.0000>
```

## Attributes

All attributes of the `Lap` class.

### running

If the lap is running.

**Type**

- [bool](https://docs.python.org/3/library/functions.html#bool)

### elapsed

The elapsed time in seconds. While the lap is running this is measured against
the current clock, so it grows between reads until the lap is stopped.

**Type**

- [float](https://docs.python.org/3/library/functions.html#float)

## Methods

All methods of the `Lap` class.

### start

```python
def start(self) -> None:
```

Starts the lap if not running.

::: danger
It is not recommended to use this method. Instead, use the stopwatch [start](/api/stopwatch#start) method.
:::

### stop

```python
def stop(self) -> None:
```

Stops the lap, freezing the duration. Calling it on a lap that is already
stopped does nothing.

::: danger
It is not recommended to use this method. Instead, use the Stopwatch [stop](/api/stopwatch#stop) method.
:::
