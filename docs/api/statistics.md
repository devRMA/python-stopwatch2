# Statistics

**Source code: [stopwatch/statistics.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/statistics.py)**

[[toc]]

Supported Operations

```python
len(x)  # get the length of the values
```

## Initialization

```python
def __init__(self, values: Optional[List[float]] = None) -> None:
```

- `values`: The list of values to be used for the statistics.
  - Type: Optional[List[[float](https://docs.python.org/3/library/functions.html#float)]]
  - Default: None

## Attributes

All attributes of the `Statistics` class.

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

## Methods

All methods of the `Statistics` class.

### add

```py
def add(self, value: float) -> None:
```

Add a value to the list of values.

**Parameters**

- `value`: The value to be added.
  - Type: [float](https://docs.python.org/3/library/functions.html#float)

### to_dict

```py
def to_dict(self) -> Dict[str, float]:
```

Get a dictionary with all statistics.

**Return**

- Dict[[str](https://docs.python.org/3/library/stdtypes.html#str), [float](https://docs.python.org/3/library/functions.html#float)]

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
