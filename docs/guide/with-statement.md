---
title: With statement
description: Use a Stopwatch as a context manager so it starts and stops itself around a block, and have it print the report for you.
---

# With statement

You can use the Stopwatch Class with the [with statement](https://www.geeksforgeeks.org/with-statement-in-python/).

```python{4}
from stopwatch import Stopwatch
from time import sleep

with Stopwatch() as my_stopwatch:
    sleep(3)
print(f'Time elapsed: {my_stopwatch}')  # Time elapsed: 3.00s
```

When you are using the [with statement](https://www.geeksforgeeks.org/with-statement-in-python/), you can pass the ``print_report`` parameter to the Stopwatch class, to print the report at the end of execution.

```python{4}
from stopwatch import Stopwatch
from time import sleep

with Stopwatch(print_report=True):
    sleep(2)

# [__main__:<module>:4] ~ 2.00s
```

The prefix is `[module:function:line]` and points at the line where the
stopwatch was created, so you can tell several reports apart. Pass a name to
label it as well:

```python{4}
from stopwatch import Stopwatch
from time import sleep

with Stopwatch('my custom message', print_report=True):
    sleep(1)

# [__main__:<module>:4] ~ 1.00s - my custom message
```

::: tip
Timing several iterations instead of one block? See
[measuring laps](/guide/measuring-laps).
:::
