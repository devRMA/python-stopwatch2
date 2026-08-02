---
title: Utils
description: API reference for format_elapsed_time — turn a duration in seconds into a readable string with the right unit.
---

# Utils

**Source:** [stopwatch/utils.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/utils.py)

## format_elapsed_time

Turns a duration in seconds into a readable string, picking the unit from the
size of the value. This is what [`str(sw)`](/api/stopwatch#supported-operations)
and every report use, exported so you can format your own numbers the same way.

```python
def format_elapsed_time(elapsed: float, precision: int = 2) -> str:
```

```python
from stopwatch import format_elapsed_time

print(format_elapsed_time(1.5))       # 1.50s
print(format_elapsed_time(0.0801))    # 80.10ms
print(format_elapsed_time(0.0000013)) # 1.30μs
```

| Range | Unit |
|---|---|
| 1s and above | `s` |
| 1ms up to 1s | `ms` |
| below 1ms | `μs` |

### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `elapsed` | [`float`](https://docs.python.org/3/library/functions.html#float) | — | The duration, in seconds. |
| `precision` | [`int`](https://docs.python.org/3/library/functions.html#int) | `2` | Decimal places. |

**Returns** [`str`](https://docs.python.org/3/library/stdtypes.html#str)

### Precision

```python
from stopwatch import format_elapsed_time

print(format_elapsed_time(1, 2))         # 1.00s
print(format_elapsed_time(1, 4))         # 1.0000s
print(format_elapsed_time(1, 0))         # 1s
print(format_elapsed_time(0.1, 0))       # 100ms
print(format_elapsed_time(0.001, 0))     # 1ms
print(format_elapsed_time(0.0001, 0))    # 100μs
print(format_elapsed_time(0.000001, 0))  # 1μs
```

### Negative and zero

The unit comes from the magnitude, so a negative duration keeps the unit its
size deserves rather than collapsing into microseconds.

```python
from stopwatch import format_elapsed_time

print(format_elapsed_time(-1))         # -1.00s
print(format_elapsed_time(-0.1))       # -100.00ms
print(format_elapsed_time(-0.000001))  # -1.00μs
print(format_elapsed_time(0))          # 0.00μs
```

### Formatting statistics

Every [`Statistics`](/api/statistics) value is in seconds, so this is how you
make one readable:

```python
from stopwatch import Statistics, format_elapsed_time

stats = Statistics([0.1, 0.2, 0.3, 0.4, 0.5])

print(format_elapsed_time(stats.mean))   # 300.00ms
print(format_elapsed_time(stats.stdev))  # 141.42ms
```

## See also

- [`Statistics`](/api/statistics) — the values you will want to format.
- [`Stopwatch.precision`](/api/stopwatch#precision) — the same setting, applied
  to a stopwatch's own output.
