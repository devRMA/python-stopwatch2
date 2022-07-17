# Utils

**Source code: [stopwatch/utils.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/utils.py)**

## format_elapsed_time

```python
def format_elapsed_time(elapsed: float, precision: int = 2) -> str:
```

Format the elapsed time in seconds to a human readable string.

**Parameters**

- `elapsed`: The elapsed time in seconds.
  - Type: [float](https://docs.python.org/3/library/functions.html#float)
- `precision`: The number of decimal places to use.
  - Type: [float](https://docs.python.org/3/library/functions.html#float)
  - Default: 2

**Returns**

- The formatted elapsed time.

**Return type**

- [str](https://docs.python.org/3/library/stdtypes.html#str)

::: details Example

```python
from stopwatch import format_elapsed_time

print(format_elapsed_time(1, 2))  # 1.00s
print(format_elapsed_time(1, 4))  # 1.0000s
print(format_elapsed_time(1, 0))  # 1s
print(format_elapsed_time(0.1, 0))  # 100ms
print(format_elapsed_time(0.001, 0))  # 1ms
print(format_elapsed_time(0.0001, 0))  # 100μs
print(format_elapsed_time(0.000001, 0))  # 1μs
```

:::
