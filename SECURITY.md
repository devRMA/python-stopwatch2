# Security Policy

## Supported Versions

Only the latest release of `python-stopwatch2` receives fixes. There are no
long-term support branches.

| Version | Supported |
| ------- | --------- |
| 2.0.x   | Yes       |
| < 2.0   | No        |

Supported Python versions follow the upstream Python release cycle: versions
that have reached end-of-life upstream are not supported here either.

## Reporting a Vulnerability

Please do not open a public issue for security problems.

Report privately through GitHub Security Advisories:
[**Report a vulnerability**](https://github.com/devRMA/python-stopwatch2/security/advisories/new).

This is a small, single-maintainer library maintained on a best-effort basis.
Expect an initial response within 14 days. If a report is confirmed, a fix is
released as a new version and credited in the advisory unless you prefer
otherwise.

## Scope

`python-stopwatch2` measures elapsed time and formats it for output. It does no
network I/O, no filesystem access, no deserialization and no subprocess
execution, and its only runtime dependency is `colorama`. Realistic issues are
limited to that dependency and to the output-formatting path.
