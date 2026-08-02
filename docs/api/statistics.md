# Statistics

**Source code: [stopwatch/statistics.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/statistics.py)**

## Supported operations

```python
len(x)   # the number of values
repr(x)  # <Statistics values=[0.1, 0.2, 0.3]>
```

## Initialization

```python
def __init__(self, values: list[float] | None = None) -> None:
```

- `values`: The list of values to be used for the statistics.
  - Type: [list](https://docs.python.org/3/library/stdtypes.html#list)[[float](https://docs.python.org/3/library/functions.html#float)] | None
  - Default: None

::: info
The list is copied, so later changes to the list you pass in do not affect the
statistics. Use [add](#add) to append more values.
:::

## Attributes

All attributes of the `Statistics` class.

::: warning
`mean`, `median`, `variance` and `stdev` raise
[StatisticsError](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError)
when there are no values, and `maximum` and `minimum` raise `ValueError`. Only
`total` is defined for an empty `Statistics`, where it is `0.0`. Check `len()`
first if the values may be empty.
:::

### mean

The mean value in seconds.

**Type**

- [float](https://docs.python.org/3/library/functions.html#float)

::: details Example

```python
from stopwatch import Stopwatch
from random import randint
from time import sleep

with Stopwatch() as sw:
    for _ in range(1, 6):
        with sw.lap():
            sleep(randint(1, 10) / 10)
print(sw.statistics.mean)  # 0.5
```

:::

### maximum

The maximum value in seconds.

**Type**

- [float](https://docs.python.org/3/library/functions.html#float)

::: details Example

```python
from stopwatch import Stopwatch
from random import randint
from time import sleep

with Stopwatch() as sw:
    for _ in range(1, 6):
        with sw.lap():
            sleep(randint(1, 10) / 10)
print(sw.statistics.maximum)  # 0.9
```

:::

### median

The median value in seconds.

**Type**

- [float](https://docs.python.org/3/library/functions.html#float)

::: details Example

```python
from stopwatch import Stopwatch
from random import randint
from time import sleep

with Stopwatch() as sw:
    for _ in range(1, 6):
        with sw.lap():
            sleep(randint(1, 10) / 10)
print(sw.statistics.median)  # 0.5
```

:::

### minimum

The minimum value in seconds.

**Type**

- [float](https://docs.python.org/3/library/functions.html#float)

::: details Example

```python
from stopwatch import Stopwatch
from random import randint
from time import sleep

with Stopwatch() as sw:
    for _ in range(1, 6):
        with sw.lap():
            sleep(randint(1, 10) / 10)
print(sw.statistics.minimum)  # 0.1
```

:::

### total

The total value in seconds.

**Type**

- [float](https://docs.python.org/3/library/functions.html#float)

::: details Example

```python
from stopwatch import Stopwatch
from random import randint
from time import sleep

with Stopwatch() as sw:
    for _ in range(1, 6):
        with sw.lap():
            sleep(randint(1, 10) / 10)
print(sw.statistics.total)  # 2.5
```

:::

### variance

The variance value in seconds.

**Type**

- [float](https://docs.python.org/3/library/functions.html#float)

::: details Example

```python
from stopwatch import Stopwatch
from random import randint
from time import sleep

with Stopwatch() as sw:
    for _ in range(1, 6):
        with sw.lap():
            sleep(randint(1, 10) / 10)
print(sw.statistics.variance)  # 0.09
```

:::

### stdev

The population standard deviation in seconds, that is, the square root of
[variance](#variance). This is the `dev` field of the
[report](/api/stopwatch#report).

**Type**

- [float](https://docs.python.org/3/library/functions.html#float)

::: details Example

```python
from stopwatch import Statistics

stats = Statistics([0.1, 0.2, 0.3, 0.4, 0.5])
print(stats.variance)  # 0.02
print(stats.stdev)     # 0.1414213562373095
```

:::

## Methods

All methods of the `Statistics` class.

### add

```python
def add(self, value: float) -> None:
```

Add a value to the list of values.

**Parameters**

- `value`: The value to be added.
  - Type: [float](https://docs.python.org/3/library/functions.html#float)

### to_dict

```python
def to_dict(self) -> dict[str, float]:
```

Get a dictionary with all statistics.

::: info
[stdev](#stdev) is not included, to keep the keys stable for anything already
consuming this dictionary. Read it from the attribute when you need it.
:::

**Returns**

- The dictionary with all statistics.

**Return type**

- [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [float](https://docs.python.org/3/library/functions.html#float)]

::: details Example

```python
from stopwatch import Stopwatch
from random import randint
from time import sleep

with Stopwatch() as sw:
    for _ in range(1, 6):
        with sw.lap():
            sleep(randint(1, 10) / 10)
print(sw.statistics.to_dict())
# {'mean': 0.5, 'maximum': 0.9, 'median': 0.5, 'minimum': 0.1, 'total': 2.5, 'variance': 0.09}
```

:::
