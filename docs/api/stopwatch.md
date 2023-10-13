# Stopwatch

**Source code: [stopwatch/stopwatch.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/stopwatch.py)**

## Initialization

```python
def __init__(
    self,
    name: Optional[str] = None,
    print_report: bool = False,
    precision: int = 2
) -> None:
```

**Parameters**

- `name`: The name of the stopwatch, used for reporting.
  - Type: Optional[[str](https://docs.python.org/3/library/stdtypes.html#str)]
- `print_report`: This parameter is used to print elapsed time at the end of [with statement](https://www.geeksforgeeks.org/with-statement-in-python/).
  - Type: [bool](https://docs.python.org/3/library/functions.html#bool)
  - Default: False
- `precision`: The number of decimal places to use.
  - Type: [int](https://docs.python.org/3/library/functions.html#int)

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

:::

## Attributes

All attributes of the `Stopwatch` class.

### name

The name of the stopwatch. Can be set during initialization.

**Type**

- Optional[[str](https://docs.python.org/3/library/stdtypes.html#str)]

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

- List[[Lap](/api/lap)]

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

True if the stopwatch is running, False if stopped.

**Type**

- [bool](https://docs.python.org/3/library/functions.html#bool)

::: details Example

```python
sw = Stopwatch()
print(sw.running)  # True
sw.stop()
print(sw.running)  # False
```

:::

### statistics

The statistics of the stopwatch.

**Type**

- Statistics

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

Starts the stopwatch if not running.

::: info
This method is called automatically when the stopwatch is created.
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

Context manager for create a new [lap](/api/lap).

::: details Example

```python
with Stopwatch() as sw:
    for i in range(5):
        with sw.lap(): // [!code focus]
            sleep(i / 10)
print(f'{sw}')  # 1.00s
print(len(sw.laps))  # 5
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
# [Stopwatch] total=1.0s, mean=0.2s, min=0.0s, median=0.2s, max=0.4s, dev=0.1s
```

:::
