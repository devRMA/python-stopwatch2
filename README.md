<!-- ================ TITLE/DESC ================ -->

<div align='center'>
    <h2>Python-StopWatch-2</h2>
    <p>A simple stopwatch for measuring code performance. This is a fork from <a href='https://pypi.org/project/python-stopwatch/'>python-stopwatch</a>, which adds static typing and a few other things.</p>
</div>

<!-- ================ BADGES/LINKS ================ -->

<div align='center' width='50%'>
    <h3> → STATUS ←</h3>
    <a href="https://pepy.tech/project/python-stopwatch2">
        <img alt="Pypi Version" src='https://img.shields.io/pypi/v/python-stopwatch2?&style=for-the-badge'/>
    </a>
    <a href="https://www.python.org">
        <img alt="Python Versions" src='https://img.shields.io/pypi/pyversions/python-stopwatch2?&style=for-the-badge'/>
    </a>
    <a href="https://github.com/devRMA/python-stopwatch2">
        <img alt="Repo Size" src='https://img.shields.io/github/repo-size/devRMA/python-stopwatch2?&style=for-the-badge'/>
    </a>
    <a href="https://github.com/devRMA/python-stopwatch2/blob/main/LICENSE">
        <img alt="License" src='https://img.shields.io/github/license/devRMA/python-stopwatch2?&style=for-the-badge'/>
    </a>
    <a href="https://github.com/devRMA/python-stopwatch2/stargazers">
        <img alt="Stars" src='https://img.shields.io/github/stars/devRMA/python-stopwatch2?&style=for-the-badge'/>
    </a>
    <a href="https://github.com/devRMA/python-stopwatch2/graphs/contributors">
        <img alt="Contributors" src='https://img.shields.io/github/contributors/devRMA/python-stopwatch2?&style=for-the-badge'/>
    </a>
</div>

<hr>

<div align='center' width='50%'>
    <a href="https://github.com/devRMA/python-stopwatch2">
        <img alt="Tests" src='https://github.com/devRMA/python-stopwatch2/actions/workflows/tests.yml/badge.svg?&style=for-the-badge'/>
    </a>
    <a href="https://pepy.tech/project/python-stopwatch2">
        <img alt="Pypi Downloads" src='https://pepy.tech/badge/python-stopwatch2?&style=for-the-badge'/>
    </a>
    <a href="https://coveralls.io/github/devRMA/python-stopwatch2">
        <img alt="Coverage Status" src='https://coveralls.io/repos/github/devRMA/python-stopwatch2/badge.svg?&style=for-the-badge'/>
    </a>
</div>

<!-- ================ INTRODUCTION ================ -->
<div align='center'>
    <h3>→ USAGE ←</h3>
</div>

<h3>☍ INSTALLATION</h3>

To install the library, you can just run the following command:

```shell
poetry add python-stopwatch2
```

Or, using pip:

```shell
pip install python-stopwatch2
```

<h3>☍ BASIC USAGE</h3>

<p><b>ƒ stopwatch.Stopwatch</b></p>

You can use the [start()](https://stopwatch2.vercel.app/api/stopwatch.html#start) and [stop()](https://stopwatch2.vercel.app/api/stopwatch.html#stop) methods to starts or stops the stopwatch counter.

```python
from time import sleep

from stopwatch import Stopwatch

my_stopwatch = Stopwatch()
sleep(2)
my_stopwatch.stop()
print(my_stopwatch.elapsed)  # 2.0
sleep(1)
print(my_stopwatch.elapsed)  # 2.0
my_stopwatch.start()
sleep(1)
my_stopwatch.stop()
print(my_stopwatch.elapsed)  # 3.0
print(f'Time elapsed: {my_stopwatch}')  # Time elapsed: 3.00s
```

It is also possible to use [Stopwatch](https://stopwatch2.vercel.app/api/stopwatch.html#stopwatch) with the [with statement](https://www.geeksforgeeks.org/with-statement-in-python/).

```python
from time import sleep

from stopwatch import Stopwatch

with Stopwatch() as my_stopwatch:
    sleep(3)
print(my_stopwatch.elapsed)  # 3.0
print(f'Time elapsed: {my_stopwatch}')  # Time elapsed: 3.00s
```
<h3>☍ DOCUMENTATION</h3>

To check out the docs, visit [https://stopwatch2.vercel.app/](https://stopwatch2.vercel.app/)

<h3>☍ CHANGELOG</h3>

Detailed changes for each release are documented in the [CHANGELOG.md](/CHANGELOG.md).

<h3>CONTRIBUTING</h3>

Pull requests are welcome!

<h3>☍ 📑 LICENSE</h3>

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2021-2022 Jonghwan Hyeon, 2022-present Rafael
