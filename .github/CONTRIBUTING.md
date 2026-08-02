# Contributing

Contributions are **welcome**.

We accept contributions via Pull Requests on [Github](https://github.com/devRMA/python-stopwatch2).

## Pull Requests

- **[PEP 8 -- Style Guide](https://www.python.org/dev/peps/pep-0008/)** - Follow PEP 8 style and do static typing.

- **Add tests!** - Your patch won't be accepted if it doesn't have tests.

- **Document any behavior change** - Make sure the `README.md` and any other relevant documentation are kept up-to-date.

- **Consider our release cycle** - We try to follow [SemVer v2.0.0](http://semver.org/). Randomly breaking public APIs is not an option.

- **Create feature branches** - Don't ask us to pull from your master branch.

- **One pull request per feature** - If you want to do more than one thing, send multiple pull requests.

## Setup

This project targets Python 3.10+ and is managed with [Poetry](https://python-poetry.org/).
The exact interpreter and Poetry versions are pinned in `.tool-versions` for
[asdf](https://asdf-vm.com/) users.

```bash
poetry install
```

## Running Tests

```bash
poetry run pytest --cov=stopwatch --cov-report=term-missing
```

## Linting and Formatting

Linting, import sorting and formatting are all handled by [Ruff](https://docs.astral.sh/ruff/),
and type checking by [mypy](https://mypy-lang.org/):

```bash
poetry run ruff check --fix .   # lint and sort imports
poetry run ruff format .        # format
poetry run mypy stopwatch       # type check
```

CI runs the same commands with `--check`, so run them before pushing.

**Happy coding**!
