---
layout: home

title: Python Stopwatch 2
titleTemplate: Measure Python code performance
description: A small, fully typed Python stopwatch and profiler. Time a block with a context manager, time each iteration with laps, or time every call to a function with a decorator — with mean, median and standard deviation included.

head:
  - - meta
    - name: keywords
      content: python stopwatch, python timer, python profiler, measure execution time python, benchmark python code, python performance, timeit alternative, python decorator timer, context manager timer
  - - link
    - rel: canonical
      href: https://stopwatch2.vercel.app/

hero:
  name: Python Stopwatch 2
  text: Measure code performance.
  tagline: Time a block, every iteration of a loop, or every call to a function. Three lines, real statistics, under a microsecond of overhead.
  image:
    src: /logo_shadow.svg
    alt: Python Stopwatch 2 logo, a stopwatch dial
  actions:
    - theme: brand
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: Why laps?
      link: /guide/measuring-laps
    - theme: alt
      text: API Reference
      link: /api/stopwatch
    - theme: alt
      text: GitHub
      link: https://github.com/devRMA/python-stopwatch2

features:
  - icon: ⏱️
    title: Three ways to measure
    details: A context manager around a block, laps inside a loop, or a decorator on a function. Pick whichever fits the code you already have.
    link: /guide/measuring-laps
    linkText: Measuring laps
  - icon: 📊
    title: Statistics, not just totals
    details: Mean, median, min, max and standard deviation across every lap or call, already formatted into readable units.
    link: /api/statistics
    linkText: Statistics API
  - icon: 🔑
    title: Fully typed
    details: Ships a py.typed marker, so mypy and your editor see the real signatures. The library itself is checked under mypy strict.
    link: /api/stopwatch
    linkText: Stopwatch API
  - icon: 🎯
    title: Cheap enough to leave in
    details: Creating a reporting stopwatch costs under a microsecond, so the instrument stays out of the measurement it is reporting.
  - icon: 🪶
    title: One dependency
    details: Only colorama, for the coloured reports. Nothing else comes along for the ride.
  - icon: ☂️
    title: Tested to 100%
    details: 100% line and branch coverage, on Python 3.10 through 3.14, on Linux and Windows.
---

## Install

::: code-group

```bash [pip]
python3 -m pip install python-stopwatch2
```

```bash [poetry]
poetry add python-stopwatch2
```

```bash [uv]
uv add python-stopwatch2
```

:::

Requires Python 3.10 or newer.

## Pick the shape that fits your code

::: code-group

```python [A block]
from stopwatch import Stopwatch

with Stopwatch(print_report=True):
    build_the_index()

# [__main__:<module>:4] ~ 1.20s
```

```python [Each iteration]
from stopwatch import Stopwatch

sw = Stopwatch(autostart=False)
for document in documents:
    with sw.lap():
        index(document)

print(sw.report())
# [Stopwatch] total=0.60s, mean=0.20s, min=0.10s, median=0.20s, max=0.30s, dev=0.08s
```

```python [Every call]
from stopwatch import profile

@profile()
def parse(payload: bytes) -> dict:
    ...

# [__main__#parse] hits=1, mean=80.13ms, min=80.13ms, median=80.13ms, max=80.13ms, dev=0.00μs
# [__main__#parse] hits=2, mean=100.19ms, min=80.13ms, median=100.19ms, max=120.24ms, dev=20.06ms
# [__main__#parse] hits=3, mean=100.16ms, min=80.13ms, median=100.11ms, max=120.24ms, dev=16.38ms
```

:::

## Why not `time.perf_counter()`?

For a single measurement, use `perf_counter` — it is two lines and no dependency.
This library earns its place when you want the parts around the measurement:

- The stopwatch **stops itself**, including when the block raises, so a failure
  cannot leave you reading a number that keeps growing.
- **Laps** give you one measurement per iteration instead of a total you then
  have to divide.
- **Statistics** come with it: mean, median, min, max, standard deviation.
- **Units** are picked for you — `1.20s`, `80.13ms`, `1.32μs` — instead of
  `0.08012700000000141`.
- The **report says where it came from**, so several timers in one file stay
  apart.

Compared with `timeit`, this measures your real code in place rather than a
snippet run in isolation, and compared with `cProfile` it measures only what you
asked about instead of everything.

## Next

- [Getting Started](/guide/getting-started) — install and the first measurement.
- [With statement](/guide/with-statement) — the context manager in detail.
- [Measuring laps](/guide/measuring-laps) — loops, statistics and nesting.
- [Profiling a function](/guide/profiling-function) — the decorator, including
  `async def`.
- [Other libraries](/guide/other-libraries) — how this compares.
