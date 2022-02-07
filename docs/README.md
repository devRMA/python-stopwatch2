# Python-Stopwatch2 Documentation

Description and examples of all lib classes/functions.

***

## stopwatch.Stopwatch

### class *stopwatch.Stopwatch* (name: Optional[str] = None)

#### stopwatch.Stopwatch().name

- The name of the timer, which is used in the [report](https://github.com/devRMA/python-stopwatch2/tree/main/docs#report) method. This can be set during initialisation.
- Type:
  - Optional[[str](https://docs.python.org/3/library/stdtypes.html#str)]
- Example:

```python
with Stopwatch('foo') as sw:
    sleep(2)
print(sw.report())  # [Stopwatch#foo] total=2.0003s
```

#### *property* stopwatch.Stopwatch().laps

- The list of duration of laps.
- Type:
  - List[[float](https://docs.python.org/3/library/functions.html#float)]
- Example:

```python
with Stopwatch('foo') as sw:
    sleep(2)
print(sw.laps)  # [2.0020971080011805]
```

#### *property* stopwatch.Stopwatch().elapsed

- The elapsed time in seconds. (sum of all [laps](https://github.com/devRMA/python-stopwatch2/tree/main/docs#property-laps))
- Type:
  - [float](https://docs.python.org/3/library/functions.html#float)
- Example:

```python
with Stopwatch('foo') as sw:
    sleep(2)
print(sw.elapsed)  # 2.0020971080011805
```

#### *property* stopwatch.Stopwatch().running

- If the stopwatch is running.
- Type:
  - [bool](https://docs.python.org/3/library/functions.html#bool)
- Example:

```python
sw = Stopwatch()
print(sw.running)  # True
sw.stop()
print(sw.running)  # False
sw.start()
print(sw.running)  # True
```

#### *contextmanager* stopwatch.Stopwatch().lap()

- Context manager for add a new [lap](https://github.com/devRMA/python-stopwatch2/tree/main/docs#property-laps).
- Example:

```python
with Stopwatch() as sw:
    for i in range(5):
        with sw.lap():
            sleep(i / 10)
print(f'{sw}')  # 1.00s
print(len(sw.laps))  # 5
```

#### stopwatch.Stopwatch().start()

- Starts the stopwatch if it isn't already running.

#### stopwatch.Stopwatch().stop()

- Stops the stopwatch, freezing the duration.
- Example:

```python
my_stopwatch = Stopwatch()
sleep(2)
my_stopwatch.stop()
print(my_stopwatch.elapsed)  # 2.00027129999944
sleep(1)
print(my_stopwatch.elapsed)  # 2.00027129999944
my_stopwatch.start()
sleep(1)
my_stopwatch.stop()
print(my_stopwatch.elapsed)  # 3.0158972999997786
print(f'Time elapsed: {my_stopwatch}')  # Time elapsed: 3.02s
```

#### stopwatch.Stopwatch().reset()

- Resets the Stopwatch to 0 duration and stops it.
- Example:

```python
with Stopwatch() as sw:
    sleep(1)
sw.reset()
sleep(1)
print(sw.elapsed)  # 0.0
```

#### stopwatch.Stopwatch().restart()

- Reset and start the stopwatch.
- Example:

```python
sw = Stopwatch()
sleep(1)
print(str(sw))  # 1.00s
sw.restart()
sleep(1)
print(str(sw))  # 1.00s
```

#### stopwatch.Stopwatch().report()

- Return a report of the stopwatch statistics.
- Example:

```python
with Stopwatch() as sw:
    for i in range(5):
        with sw.lap():
            sleep(i / 10)
print(sw.report())
# [Stopwatch] total=1.5017s, mean=0.3003s, min=0.1002s, median=0.3004s, max=0.5006s, dev=0.1416s
```

#### I'll be adding the rest soon
