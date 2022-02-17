# Profiling a function

You can use this decorator to profile a function. It will print a report every time the function is called and, at the end of the execution, the final report will be printed.

```python{5}
from stopwatch import profile
from time import sleep


@profile(name='My function')
def wait_for(time: float) -> None:
    sleep(time)


for time in [0.1, 0.2, 0.3, 0.4, 0.5]:
    wait_for(time)
print('end')

# [__main__#My function] hits=1, mean=100.14ms, min=100.14ms, median=100.14ms, max=100.14ms, dev=0.00μs
# [__main__#My function] hits=2, mean=150.20ms, min=100.14ms, median=150.20ms, max=200.26ms, dev=50.06ms
# [__main__#My function] hits=3, mean=200.25ms, min=100.14ms, median=200.26ms, max=300.35ms, dev=81.74ms
# [__main__#My function] hits=4, mean=250.30ms, min=100.14ms, median=250.30ms, max=400.44ms, dev=111.92ms
# [__main__#My function] hits=5, mean=300.35ms, min=100.14ms, median=300.35ms, max=500.55ms, dev=141.56ms
# end
# [__main__#My function] hits=5, mean=300.35ms, min=100.14ms, median=300.35ms, max=500.55ms, dev=141.56ms
```
