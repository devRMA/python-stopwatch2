
# Change Log

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](http://semver.org/).

## [2.0.0](https://github.com/devRMA/python-stopwatch2/compare/v1.1.1...v2.0.0) (02/08/2026)

Version `1.1.2` was bumped in `pyproject.toml` but never released or
tagged, and contained no library changes, so this release covers
everything since `1.1.1`.

### Removed

- **Breaking**: dropped support for Python 3.7, 3.8 and 3.9. All three
  reached end-of-life upstream, and `pytest` 9.x, which carries the fix
  for CVE-2025-71176, requires Python 3.10 or newer. Supported versions
  are now 3.10 to 3.14.

### Added

- `Statistics.stdev`, the population standard deviation. It replaces
  computing `math.sqrt(statistics.variance)` by hand.
- `profile` now measures `async def` functions. They were previously
  timed only for building the coroutine, which reported microseconds for
  a call that awaited for milliseconds.
- Windows consoles now render the colored reports, by calling
  `colorama.just_fix_windows_console()`. `colorama` had always been a
  dependency for this, but nothing initialized it, so the ANSI escapes
  were printed raw.

### Changed

- **Breaking**: `profile` takes explicit keyword-only `name` and
  `report_every` parameters instead of `**kwargs`. Calls such as
  `profile(name='x')` are unaffected; a misspelled argument name is now
  an error rather than being silently ignored.
- **Breaking**: `profile(report_every=...)` rejects values below 1 with
  `ValueError`. `0` used to raise `ZeroDivisionError` on the first call
  and `-1` used to report on every call.
- **Breaking**: nested `Stopwatch.lap()` blocks each record their own
  lap. The inner block used to close the outer lap, so the outer block's
  time was silently discarded and any code after the inner block went
  unmeasured.
- **Breaking**: `Statistics(values)` copies the list it is given. It used
  to keep a reference for a non-empty list, so `add()` mutated the
  caller's list and later edits to that list changed the statistics.
- **Breaking**: `Stopwatch.running` reports whether any lap is running,
  rather than tracking a single current lap.
- `Stopwatch.laps` and the other attributes are per-instance. `laps` was
  a mutable class attribute shared by every instance, which leaked laps
  between instances of any subclass that overrode `__init__`.
- `inspect_caller` uses `sys._getframe` instead of `inspect.stack`, which
  read the source file of every frame on the stack. Constructing a
  `Stopwatch(print_report=True)` went from about 376µs of overhead to
  under 1µs.

### Fixed

- `Stopwatch.lap()` closes its lap when the wrapped block raises. The lap
  used to stay open forever, and because a running lap measures against
  the current clock, `elapsed`, `statistics` and `report()` then returned
  a different value on every read.
- `profile` records a call that raises. The measurement used to be
  discarded, so exactly the calls worth investigating went unrecorded.
- `profile` no longer prints the same report twice on exit when the last
  call already triggered one.
- `format_elapsed_time` picks the unit by magnitude, so negative values
  are no longer always rendered in microseconds. One negative hour used
  to format as `-3600000000.00μs`.
- `Lap.stop()` on an already stopped lap does nothing. It used to record
  the machine uptime as a lap fraction.
- `Statistics.total` returns a float when there are no values, as its
  annotation states.

## [1.1.1](https://github.com/devRMA/python-stopwatch2/compare/v1.1.0...v1.1.1) (20/02/2022)

### Added

- Coming back with the colored prints, using colorama (removed in [40ece4f](https://github.com/devRMA/python-stopwatch2/commit/40ece4f023cadd6fe20af5de93b54c7cb1b3e8d6)).

### Changed

- README.md changed.

## 1.1.0 (18/02/2022)

### Added

- Added new "to_dict" method to `Statistics` class.
- Added new "statistics" property to `Stopwatch` class.

### Changed

- The "laps" property of the `Stopwatch` class is now an attribute, which has a list of `Lap` objects.

## 1.0.11 (08/02/2022)

### Added

- Now the `Stopwatch` class accept the `precision` for print in initalization.
- Added the `precision` parameter to the `format_elapsed_time` function.

## 1.0.10 (07/02/2022)

### Changed

- Reorganization of files

## 1.0.9 (07/02/2022)

### Added

- Added new "running" property to `Stopwatch` class.
- Added new "restart" method to `Stopwatch` class.
- Added new "running" attribute to `Lap` class.

## 1.0.8 (06/02/2022)

### Removed

- Dropped termcolor dependency.
  
### Fixed

- Fixed PEP 561
  
## 1.0.7 (06/02/2022)

### Fixed

- Fixed fstring bug.

## 1.0.6 (06/02/2022)

### Removed

- Removed the nanosecond return, from `format_elapsed_time` function.

### Fixed

- Fixed typing hinting in `Stopwatch` class.

## 1.0.5 (05/02/2022)

### Added

- Added docstring in all methods and functions.
- Added `return self` in some methods of `Stopwatch` class.
- Added type hinting to `profile` decorator

## 1.0.4 (02/02/2022)

### Added

- Added new `__str__` and `__repr__` methods to `Stopwatch` class.
- Added static typing in all methods, attributes and functions.
