<!-- ================ SOCIAL CARD ================= -->

<p align="center"><img src="https://stopwatch2.vercel.app/social.png" alt="Social Card of Python Stopwatch 2"></p>

<!-- ================= TITLE/DESC ================= -->

<p align="center">This is a fork from <a href="https://pypi.org/project/python-stopwatch/">python-stopwatch</a>, which adds static typing and a few other things.
</p>

<!-- =================== BADGES =================== -->

[![PyPi Version](https://img.shields.io/pypi/v/python-stopwatch2?&style=for-the-badge)](https://pypi.org/project/python-stopwatch2)
[![PyPi Downloads](https://img.shields.io/pypi/dm/python-stopwatch2?style=for-the-badge)](https://pypistats.org/packages/python-stopwatch2)
[![Python Versions](https://img.shields.io/pypi/pyversions/python-stopwatch2?&style=for-the-badge)](https://www.python.org)
[![Repo Size](https://img.shields.io/github/repo-size/devRMA/python-stopwatch2?&style=for-the-badge)](https://github.com/devRMA/python-stopwatch2)
[![MIT Licensed](https://img.shields.io/github/license/devRMA/python-stopwatch2?&style=for-the-badge)](https://github.com/devRMA/python-stopwatch2/blob/main/LICENSE)
[![Stars](https://img.shields.io/github/stars/devRMA/python-stopwatch2?&style=for-the-badge)](https://github.com/devRMA/python-stopwatch2/stargazers)
[![Contributors](https://img.shields.io/github/contributors/devRMA/python-stopwatch2?&style=for-the-badge)](https://github.com/devRMA/python-stopwatch2/graphs/contributors)


[![Tests](https://github.com/devRMA/python-stopwatch2/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/devRMA/python-stopwatch2/actions/workflows/tests.yml)
[![Coverage Status](https://coveralls.io/repos/github/devRMA/python-stopwatch2/badge.svg?&style=for-the-badge)](https://coveralls.io/github/devRMA/python-stopwatch2)

<!-- ========== INSTALLATION AND TESTING ========== -->
<!-- INSTALLATION -->
<img src="https://github.com/Harlocks/design/blob/main/assets/inkscape/banners/InstallationTitle.png?raw=true">

- This package requires python 3.7 or higher.
#### **Step 1**. Install the library (Mac/Linux):
```sh
python3 -m pip install python-stopwatch2
```
> Other platform? ➜ https://stopwatch2.vercel.app/guide/getting-started.html
#### **Step 2**. Import the Stopwatch class:
```sh
from stopwatch import Stopwatch
```
#### **Step 3**. Create a new Stopwatch object:
```sh
sw = Stopwatch()
```
#### **Step 4**. Place your code here:
```sh
from time import sleep
sleep(2)
```
#### **Step 5**. Stop the stopwatch:
```sh
sw.stop()
```
#### **Step 6**. Get the elapsed time:
```sh
print(f'Time elapsed: {sw.elapsed}')  # Time elapsed: 2.0031827000002522
# or
print(f'Time elapsed: {sw}')  # Time elapsed: 2.00s
```

> You'll find installation instructions and full documentation on https://stopwatch2.vercel.app.
<!-- TESTING -->
<img src="https://github.com/Harlocks/design/blob/main/assets/inkscape/banners/TestingTitle.png?raw=true">

Run the tests with:

```bash
poetry run task test
```

<!-- =========== CHANGELOG, CONTRIBUTING AND LICENSE ============ -->
<!-- CHANGELOG -->
<img src="https://github.com/Harlocks/design/blob/main/assets/inkscape/banners/ChangelogTitle.png?raw=true">

> Please see [CHANGELOG](CHANGELOG.md) for detailed changes for each release.

<!-- CONTRIBUTING -->
<img src="https://github.com/Harlocks/design/blob/main/assets/inkscape/banners/ContributingTitle.png?raw=true">

> Please see [CONTRIBUTING](.github/CONTRIBUTING.md) for details.

<!-- LICENSE -->
<img src="https://github.com/Harlocks/design/blob/main/assets/inkscape/banners/LicenseTitle.png?raw=true">

- [MIT](https://opensource.org/licenses/MIT)

- Copyright (c) 2021-2022 Jonghwan Hyeon, 2022-present Rafael
