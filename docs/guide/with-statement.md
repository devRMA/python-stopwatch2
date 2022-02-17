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
