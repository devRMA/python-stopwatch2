---
title: Statistics
description: API reference for the Statistics class — mean, median, min, max, total, variance and standard deviation over a set of measurements.
---

# Statistics

Summarises a set of durations. You usually get one from
[`Stopwatch.statistics`](/api/stopwatch#statistics) rather than building it
yourself, but it works standalone on any list of numbers.

**Source:** [stopwatch/statistics.py](https://github.com/devRMA/python-stopwatch2/blob/main/stopwatch/statistics.py)

```python
from stopwatch import Statistics
```

## At a glance

| What | Members |
|---|---|
| **Create** | [`Statistics(values)`](#initialization) · [`add(value)`](#add) |
| **Read** | [`mean`](#mean) · [`median`](#median) · [`minimum`](#minimum) · [`maximum`](#maximum) · [`total`](#total) · [`variance`](#variance) · [`stdev`](#stdev) |
| **Export** | [`to_dict()`](#to-dict) · [`len(stats)`](#supported-operations) |

```python
from stopwatch import Statistics

stats = Statistics([0.1, 0.2, 0.3, 0.4, 0.5])

print(len(stats))       # 5
print(stats.mean)       # 0.3
print(stats.minimum)    # 0.1
print(stats.median)     # 0.3
print(stats.maximum)    # 0.5
print(stats.total)      # 1.5
print(stats.variance)   # 0.02
print(stats.stdev)      # 0.1414213562373095
```

## Supported operations

```python
len(stats)   # 5
repr(stats)  # <Statistics values=[0.1, 0.2, 0.3, 0.4, 0.5]>
```

## Initialization

```python
def __init__(self, values: list[float] | None = None) -> None:
```

| Parameter | Type | Default | Description |
|---|---|---|---|
| `values` | `list[float] \| None` | `None` | Initial values, in seconds. Copied, so later changes to your list do not affect the statistics. |

```python
values = [1.0, 2.0]
stats = Statistics(values)

stats.add(3.0)
print(values)       # [1.0, 2.0]  -- untouched
print(len(stats))   # 3
```

::: danger Empty statistics raise
With no values, `mean`, `median`, `variance` and `stdev` raise
[`StatisticsError`](https://docs.python.org/3/library/statistics.html#statistics.StatisticsError),
and `maximum` and `minimum` raise `ValueError`. Only `total` is defined, as
`0.0`. Guard with `len()` when the set may be empty:

```python
if len(stats):
    print(stats.mean)
```
:::

## Attributes

Every value is in seconds. Pass them through
[`format_elapsed_time`](/api/utils#format-elapsed-time) for readable units.

### mean

The arithmetic mean.

**Type:** [`float`](https://docs.python.org/3/library/functions.html#float)

```python
print(Statistics([0.1, 0.2, 0.3, 0.4, 0.5]).mean)  # 0.3
```

### maximum

The largest value — the slowest lap or call, which is usually the interesting
one.

**Type:** [`float`](https://docs.python.org/3/library/functions.html#float)

```python
print(Statistics([0.1, 0.2, 0.3, 0.4, 0.5]).maximum)  # 0.5
```

### median

The middle value. Less sensitive to one outlier than [`mean`](#mean), so
comparing the two tells you whether a single slow run is dragging the average.

**Type:** [`float`](https://docs.python.org/3/library/functions.html#float)

```python
print(Statistics([0.1, 0.2, 0.3, 0.4, 0.5]).median)  # 0.3
print(Statistics([0.1, 0.1, 0.1, 0.1, 9.9]).median)  # 0.1
print(Statistics([0.1, 0.1, 0.1, 0.1, 9.9]).mean)    # 2.06
```

### minimum

The smallest value — the best case, closest to the cost without interference.

**Type:** [`float`](https://docs.python.org/3/library/functions.html#float)

```python
print(Statistics([0.1, 0.2, 0.3, 0.4, 0.5]).minimum)  # 0.1
```

### total

The sum. This is the only attribute defined for an empty `Statistics`, where it
is `0.0`.

**Type:** [`float`](https://docs.python.org/3/library/functions.html#float)

```python
print(Statistics([0.1, 0.2, 0.3, 0.4, 0.5]).total)  # 1.5
print(Statistics().total)                            # 0.0
```

### variance

The population variance. See [`stdev`](#stdev) for the same spread in seconds
rather than seconds squared.

**Type:** [`float`](https://docs.python.org/3/library/functions.html#float)

```python
print(Statistics([0.1, 0.2, 0.3, 0.4, 0.5]).variance)  # 0.02
```

### stdev

The population standard deviation, the square root of [`variance`](#variance).
This is the `dev` field of the [reports](/api/stopwatch#report): a small value
means the measurements agree, a large one means they scatter and the mean is not
telling you much.

**Type:** [`float`](https://docs.python.org/3/library/functions.html#float)

```python
print(Statistics([0.1, 0.2, 0.3, 0.4, 0.5]).stdev)  # 0.1414213562373095
print(Statistics([0.3, 0.3, 0.3, 0.3, 0.3]).stdev)  # 0.0
```

## Methods

### add

```python
def add(self, value: float) -> None:
```

Appends a value, in seconds.

| Parameter | Type | Description |
|---|---|---|
| `value` | [`float`](https://docs.python.org/3/library/functions.html#float) | The duration to record. |

```python
stats = Statistics()
stats.add(0.1)
stats.add(0.3)

print(len(stats))  # 2
print(stats.mean)  # 0.2
```

### to_dict

```python
def to_dict(self) -> dict[str, float]:
```

Every statistic as a plain dictionary, handy for logging or JSON.

**Returns** `dict[str, float]`

```python
print(Statistics([0.1, 0.2, 0.3, 0.4, 0.5]).to_dict())
# {'mean': 0.3, 'maximum': 0.5, 'median': 0.3, 'minimum': 0.1, 'total': 1.5, 'variance': 0.02}
```

::: info
[`stdev`](#stdev) is deliberately not in the dictionary, so the keys stay stable
for anything already consuming it. Read it from the attribute.
:::

## See also

- [`Stopwatch.statistics`](/api/stopwatch#statistics) — where these usually come
  from.
- [Measuring laps](/guide/measuring-laps) — building up a set of measurements.
