# Stopwatch

**Source code: [stopwatch/stopwatch.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/stopwatch.py)**

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

**Parameters**

- `name`: The name of the stopwatch, used for reporting.
  - Type: [str](https://docs.python.org/3/library/stdtypes.html#str) | None
  - Default: None
- `print_report`: This parameter is used to print elapsed time at the end of [with statement](https://www.geeksforgeeks.org/with-statement-in-python/). The report is prefixed with `[module:function:line]`, pointing at where the stopwatch was created.
  - Type: [bool](https://docs.python.org/3/library/functions.html#bool)
  - Default: False
- `precision`: The number of decimal places to use.
  - Type: [int](https://docs.python.org/3/library/functions.html#int)
  - Default: 2
- `autostart`: Whether to start measuring immediately. Pass `False` to measure only the blocks wrapped in [lap](#lap).
  - Type: [bool](https://docs.python.org/3/library/functions.html#bool)
  - Default: True

::: details Example

```python
with Stopwatch('my stopwatch') as sw:
    sleep(3)
print(sw.report())
# [Stopwatch#my stopwatch] total=3.00s
```

<br>

```python
with Stopwatch('my custom message', True):
    sleep(3)
# [__main__:<module>:1] ~ 3.00s - my custom message
```

<br>

```python
with Stopwatch(print_report=True):
    sleep(3)
# [__main__:<module>:1] ~ 3.00s
```

<br>

```python
with Stopwatch(precision=3) as sw:
    sleep(3)
print(str(sw))  # 3.000s
sw.precision = 0
print(str(sw))  # 3s
```

<br>

```python
sw = Stopwatch(autostart=False)
sleep(0.5)              # setup work, not measured
with sw.lap():
    sleep(0.1)
print(sw.laps[0].elapsed)  # 0.1

# With the default autostart=True, the same code bills the 0.5s
# to the first lap:
sw = Stopwatch()
sleep(0.5)
with sw.lap():
    sleep(0.1)
print(sw.laps[0].elapsed)  # 0.6
```

:::

## Supported operations

```python
str(sw)   # the elapsed time, formatted -> '2.00s'
repr(sw)  # <Stopwatch name=None elapsed=2.0031827000002522>
```

## Attributes

All attributes of the `Stopwatch` class.

### name

The name of the stopwatch. Can be set during initialization.

**Type**

- [str](https://docs.python.org/3/library/stdtypes.html#str) | None

::: details Example

```python
with Stopwatch('sw1') as sw:
    ...
print(sw.name)  # sw1
```

:::

### precision

The number of decimal places to use. Can be set during initialization.

**Type**

- [int](https://docs.python.org/3/library/functions.html#int)
- Default:
  - 2

::: details Example

```python
with Stopwatch(precision=1) as sw:
    sleep(1)
print(str(sw))  # 1.0s
```

:::

### laps

The list of all stopwatch laps.

**Type**

- list[[Lap](/api/lap)]

::: details Example

```python
with Stopwatch() as sw:
    with sw.lap():
        sleep(1)
    with sw.lap():
        sleep(2)
print(len(sw.laps))  # 2
print(sw.laps[0].elapsed)  # 1.0
print(sw.laps[-1].elapsed)  # 2.0
```

:::

### elapsed

The elapsed time in seconds (sum of the elapsed time of all [laps](#laps)).

**Type**

- [float](https://docs.python.org/3/library/functions.html#float)

::: details Example

```python
with Stopwatch(precision=1) as sw:
    sleep(1)
print(sw.elapsed)  # 1.0
```

:::

### running

True while any lap is running, False when every lap is stopped. This includes
the lap opened by a [lap](#lap) block, so it is True inside one.

**Type**

- [bool](https://docs.python.org/3/library/functions.html#bool)

::: details Example

```python
sw = Stopwatch()
print(sw.running)  # True
sw.stop()
print(sw.running)  # False

print(Stopwatch(autostart=False).running)  # False
```

:::

### statistics

The statistics of the stopwatch.

**Type**

- [Statistics](/api/statistics)

::: details Example

```python
with Stopwatch() as sw:
    for c in range(1, 6):
        with sw.lap():
            sleep(c / 10)
print(sw.statistics.maximum)  # 0.5
print(sw.statistics.minimum)  # 0.1
print(sw.statistics.mean)  # 0.3
```

:::

## Methods

All methods of the `Stopwatch` class.

### start

```python
def start(self) -> Stopwatch:
```

Starts the stopwatch if not running. Calling it on a stopwatch that is already
running does nothing.

::: info
This method is called automatically when the stopwatch is created, unless you
pass [autostart=False](#initialization).
:::

**Returns**

- The self instance.

**Return type**

- [Stopwatch](#stopwatch)

### stop

```python
def stop(self) -> Stopwatch:
```

Stops the stopwatch, freezing the duration.

::: info
This method is called automatically when you are using [with statement](https://www.geeksforgeeks.org/with-statement-in-python/).
:::

**Returns**

- The self instance.

**Return type**

- [Stopwatch](#stopwatch)

::: details Example

```python
sw = Stopwatch()
sleep(2)
sw.stop()
print(sw.elapsed)  # 2.0
sleep(1)
print(sw.elapsed)  # 2.0
sw.start()
sleep(1)
sw.stop()
print(sw.elapsed)  # 3.0
print(f'Time elapsed: {sw}')  # Time elapsed: 3.00s
```

<br>

```python
with Stopwatch() as sw:
    print(sw.running)  # True
print(sw.running)  # False
```

:::

### lap

```python
@contextmanager
def lap(self) -> Iterator[None]:
```

Context manager that records the block it wraps as its own [lap](/api/lap).

The lap is always closed when the block ends, including when the block raises,
so an exception cannot leave a lap running and skew every later reading.

Nesting works: each `lap()` records a distinct lap, and the outer block keeps
its own time.

::: warning
A stopwatch starts measuring as soon as it is created, and the first `lap()`
takes over that lap instead of opening a second one — otherwise the time
already on the clock would show up as an extra lap. That means any work between
`Stopwatch()` and the first `lap()` is billed to the first lap. Use
[autostart=False](#initialization) when you only want the `lap()` blocks
measured.
:::

::: details Example

```python
with Stopwatch() as sw:
    for i in range(5):
        with sw.lap(): # [!code focus]
            sleep(i / 10)
print(f'{sw}')  # 1.00s
print(len(sw.laps))  # 5
```

<br>

Nested laps, each keeping its own time:

```python
sw = Stopwatch(autostart=False)
with sw.lap():
    sleep(0.1)
    with sw.lap():
        sleep(0.2)
    sleep(0.1)
print(len(sw.laps))         # 2
print(sw.laps[0].elapsed)   # 0.4  (the outer block, including the inner one)
print(sw.laps[1].elapsed)   # 0.2  (the inner block)
```

<br>

The lap is closed even when the block raises:

```python
sw = Stopwatch(autostart=False)
try:
    with sw.lap():
        sleep(0.1)
        raise ValueError('boom')
except ValueError:
    pass
sleep(0.3)
print(sw.running)   # False
print(sw.elapsed)   # 0.1  -- does not keep growing
```

:::

### reset

```python
def reset(self) -> Stopwatch:
```

Resets the Stopwatch to 0 duration and stops it.

**Returns**

- The self instance.

**Return type**

- [Stopwatch](#stopwatch)

::: details Example

```python
with Stopwatch() as sw:
    sleep(1)
sw.reset()
sleep(1)
print(sw.elapsed)  # 0.0
```

:::

### restart

```python
def restart(self) -> Stopwatch:
```

Reset and start the stopwatch.

**Returns**

- The self instance.

**Return type**

- [Stopwatch](#stopwatch)

::: details Example

```python
sw = Stopwatch()
sleep(1)
print(str(sw))  # 1.00s
sw.restart()
sleep(1)
print(str(sw))  # 1.00s
```

:::

### report

```python
def report(self) -> str:
```

Return a report of the stopwatch statistics.

**Returns**

- The string with the report.

**Return type**

- [str](https://docs.python.org/3/library/stdtypes.html#str)

::: details Example

```python
with Stopwatch() as sw:
    for i in range(5):
        with sw.lap():
            sleep(i / 10)
print(sw.report())
# [Stopwatch] total=1.00s, mean=0.20s, min=0.00s, median=0.20s, max=0.40s, dev=0.14s
```

::: info
The number of decimal places follows [precision](#precision). The mean, min,
median, max and deviation are only included when there is more than one lap.
:::

:::
