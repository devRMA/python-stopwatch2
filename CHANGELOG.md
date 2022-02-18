
# Change Log

All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](http://semver.org/).

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
