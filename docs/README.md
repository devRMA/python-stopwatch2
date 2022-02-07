# Python-Stopwatch2 Documentation

Description and examples of all lib classes/functions.

## stopwatch.Stopwatch

### class *stopwatch.Stopwatch* (name: Optional[str] = None)

- **name**
  - The name of the timer, which is used in the ``report`` method. This can be set during initialisation.
  - Type:
    - Optional[[str](https://docs.python.org/3/library/stdtypes.html#str)]
  - Example:

  ```python
    with Stopwatch('foo') as sw:
        sleep(2)
    print(sw.report())  # [Stopwatch#foo] total=2.0003s
  ```

- *property* **laps**
  - The list of laps.
  - Type:
    - List[[float](https://docs.python.org/3/library/functions.html#float)]
  - Example:

  ```python
    with Stopwatch('foo') as sw:
        sleep(2)
    print(sw.laps)  # [2.0020971080011805]
  ```

- *property* **elapsed**
  - The elapsed time in seconds. (sum of all laps)
  - Type:
    - [float](https://docs.python.org/3/library/functions.html#float)
  - Example:

  ```python
    with Stopwatch('foo') as sw:
        sleep(2)
    print(sw.elapsed)  # 2.0020971080011805
  ```

- *contextmanager* **lap**()
  - Context manager for add a new lap.
  - Example:

  ```python
    with Stopwatch() as sw:
        for i in range(5):
            with sw.lap():
                sleep(i / 10)
    print(f'{sw}')  # 1.00s
    print(len(sw.laps))  # 5
  ```

- **start**()
  - Starts the stopwatch.
- **stop**()
  - Stops the stopwatch, freezing the duration.
  - Example:
  
  ```python
    sw = Stopwatch()
    sw.start()
    for i in range(5):
        sleep(i / 10)
    sw.stop()
    print(sw.elapsed)  # 1.0009550329996273
  ```

- **reset**()
  - Resets the Stopwatch to 0 duration.
  - Example:

  ```python
    with Stopwatch() as sw:
        sleep(1)
    sw.reset()
    print(sw.elapsed)  # 0
  ```

- **report**()
  - Return a report of the stopwatch statistics.
  - Example:

  ```python
    with Stopwatch() as sw:
        for i in range(5):
            with sw.lap():
                sleep(i / 10)
    print(sw.report())  # [Stopwatch] total=1.5017s, mean=0.3003s, min=0.1002s, median=0.3004s, max=0.5006s, dev=0.1416s
  ```

#### I'll be adding the rest soon
