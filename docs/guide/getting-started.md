# Getting Started

This section will help you install the library and basic usage of the stopwatch class.

::: info Requirements
Python **3.10 or newer**. The only runtime dependency is
[colorama](https://pypi.org/project/colorama/), for the colored reports.

Using Python 3.7, 3.8 or 3.9? Those are end-of-life upstream and supported only
up to `python-stopwatch2` 1.1.1.
:::

- **Step. 1:** Install the library.

  ::: code-group

  ```bash [Poetry]
  poetry add python-stopwatch2
  ```

  ```bash [PIP Linux/macOS]
  python3 -m pip install python-stopwatch2
  ```

  ```bash [PIP Windows]
  py -3 -m pip install python-stopwatch2
  ```

  :::

- **Step. 2:** Import the Stopwatch class.

  ```python
  from stopwatch import Stopwatch
  ```

- **Step. 3:** Create a new Stopwatch object.

  ```python
  sw = Stopwatch()
  ```

- **Step. 4:** Do what you want.

  ```python
  from time import sleep
  sleep(2)
  ```

- **Step. 5:** Stop the stopwatch.

  ```python
  sw.stop()
  ```

- **Step. 6:** Get the elapsed time.

  ```python
  print(f'Time elapsed: {sw.elapsed}')  # Time elapsed: 2.0031827000002522
  # or
  print(f'Time elapsed: {sw}')  # Time elapsed: 2.00s
  ```

- **Full example**

  ```python{1,4,6-7}
  from stopwatch import Stopwatch
  from time import sleep

  sw = Stopwatch()
  sleep(2)
  sw.stop()
  print(f'Time elapsed: {sw}')  # Time elapsed: 2.00s
  ```

- **Where to go next**

  - [With statement](/guide/with-statement) — let the stopwatch start and stop
    itself around a block.
  - [Measuring laps](/guide/measuring-laps) — time each iteration separately and
    get statistics across them.
  - [Profiling a function](/guide/profiling-function) — measure every call to a
    function with a decorator.
