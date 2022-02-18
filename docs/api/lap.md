# Lap

**Source code: [stopwatch/lap.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/lap.py)**

[[toc]]

## Attributes

All attributes of the Lap class.

### running

If the lap is running.

- Type:
  - [bool](https://docs.python.org/3/library/functions.html#bool)

### elapsed

The elapsed time in seconds.

- Type:
  - [float](https://docs.python.org/3/library/functions.html#float)

## Methods

All methods of the Lap class.

### start

```py
def start(self) -> None:
```

Starts the lap if not running.

::: warning
It is not recommended to use this method. Instead, use the stopwatch [start](/api/stopwatch#start) method.
:::

### stop

```py
def stop(self) -> None:
```

Stops the lap, freezing the duration.

::: warning
It is not recommended to use this method. Instead, use the Stopwatch [stop](/api/stopwatch#stop) method.
:::
