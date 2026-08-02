---
layout: home

title: Stopwatch 2
description: A simple library to measure code performance.

hero:
  name: Python Stopwatch 2
  text: A simple library to measure code performance.
  tagline: Time a block, a loop, or every call to a function — in three lines, with statistics.
  image:
    src: /logo_shadow.svg
    alt: Python Stopwatch 2 Logo
  actions:
    - theme: brand
      text: Get Started
      link: /guide/getting-started
    - theme: alt
      text: API Reference
      link: /api/stopwatch
    - theme: alt
      text: Demo
      link: https://replit.com/@devRMA/Python-Stopwatch-2-Example#main.py
    - theme: alt
      text: View on GitHub
      link: https://github.com/devRMA/python-stopwatch2

features:
  - icon: ⏱️
    title: Three ways to measure
    details: A context manager around a block, laps inside a loop, or a decorator on a function.
    link: /guide/measuring-laps
    linkText: Measuring laps
  - icon: 📊
    title: Statistics, not just totals
    details: Mean, median, min, max and standard deviation across every lap or call, formatted for you.
    link: /api/statistics
    linkText: Statistics API
  - icon: 🔑
    title: Fully typed
    details: Ships a py.typed marker, so mypy and your editor see the real signatures. Checked under mypy strict.
    link: /api/stopwatch
    linkText: Stopwatch API
  - icon: ☂️
    title: Tested to 100%
    details: 100% line and branch coverage, on Python 3.10 through 3.14, on Linux and Windows.
  - icon: 🪶
    title: One dependency
    details: Only colorama, for the colored reports. Nothing else comes along for the ride.
  - icon: 🎯
    title: Cheap to use
    details: Measuring costs under a microsecond of overhead, so the instrument stays out of the measurement.

---
