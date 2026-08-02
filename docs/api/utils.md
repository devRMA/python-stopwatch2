# Utils

**Source code: [stopwatch/utils.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/utils.py)**

## format_elapsed_time

```python
def format_elapsed_time(elapsed: float, precision: int = 2) -> str:
```

Format the elapsed time in seconds to a human readable string.

The unit is picked from the magnitude of the value: seconds at 1s and above,
milliseconds down to 1ms, and microseconds below that.

**Parameters**

- `elapsed`: The elapsed time in seconds.
  - Type: [float](https://docs.python.org/3/library/functions.html#float)
- `precision`: The number of decimal places to use.
  - Type: [int](https://docs.python.org/3/library/functions.html#int)
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

<br>

Negative values keep the unit of their magnitude:

```python
from stopwatch import format_elapsed_time

print(format_elapsed_time(-1))         # -1.00s
print(format_elapsed_time(-0.1))       # -100.00ms
print(format_elapsed_time(-0.000001))  # -1.00μs
print(format_elapsed_time(0))          # 0.00μs
```

:::
