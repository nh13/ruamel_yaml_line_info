# `ruamel_yaml_line_info`

[![Language][language-badge]][language-link]
[![Python Versions][py-versions-badge]][py-versions-link]
[![Code Style][code-style-badge]][code-style-link]
[![Type Checked][type-checking-badge]][type-checking-link]
[![PEP8][pep-8-badge]][pep-8-link]
[![Code Coverage][code-coverage-badge]][code-coverage-link]
[![License][license-badge]][license-link]

---

[![Python package][python-package-badge]][python-package-link]
[![PyPI version][pypi-badge]][pypi-link]
[![Conda version][conda-badge]][conda-link]
[![PyPI download total][pypi-downloads-badge]][pypi-downloads-link]
[![Conda download total][conda-downloads-badge]][conda-downloads-link]

---

[language-badge]:        http://img.shields.io/badge/language-python-brightgreen.svg
[language-link]:         http://www.python.org/
[py-versions-badge]:     https://img.shields.io/badge/python-3.9_|_3.10_|_3.11_|_3.12_|_3.13-blue
[py-versions-link]:      https://github.com/nh13/ruamel_yaml_line_info
[code-style-badge]:      https://img.shields.io/badge/code%20style-black-000000.svg
[code-style-link]:       https://black.readthedocs.io/en/stable/
[type-checking-badge]:   http://www.mypy-lang.org/static/mypy_badge.svg
[type-checking-link]:    http://mypy-lang.org/
[pep-8-badge]:           https://img.shields.io/badge/code%20style-pep8-brightgreen.svg
[pep-8-link]:            https://www.python.org/dev/peps/pep-0008/
[code-coverage-badge]:   https://codecov.io/gh/nh13/ruamel_yaml_line_info/branch/main/graph/badge.svg
[code-coverage-link]:    https://codecov.io/gh/nh13/ruamel_yaml_line_info
[license-badge]:         http://img.shields.io/badge/license-MIT-blue.svg
[license-link]:          https://github.com/nh13/ruamel_yaml_line_info/blob/main/LICENSE
[python-package-badge]:  https://github.com/nh13/ruamel_yaml_line_info/actions/workflows/tests.yml/badge.svg?branch=main
[python-package-link]:   https://github.com/nh13/ruamel_yaml_line_info/actions/workflows/tests.yml
[pypi-badge]:            https://badge.fury.io/py/ruamel-yaml-line-info.svg
[pypi-link]:             https://pypi.python.org/pypi/ruamel-yaml-line-info
[pypi-downloads-badge]:  https://img.shields.io/pypi/dm/ruamel_yaml_line_info
[pypi-downloads-link]:   https://pypi.python.org/pypi/ruamel_yaml_line_info
[conda-badge]:           https://anaconda.org/conda-forge/ruamel-yaml-line-info/badges/version.svg
[conda-link]:            https://anaconda.org/conda-forge/ruamel-yaml-line-info
[conda-downloads-badge]: https://anaconda.org/conda-forge/ruamel-yaml-line-info/badges/downloads.svg
[conda-downloads-link]:  https://anaconda.org/conda-forge/ruamel-yaml-line-info


Line information for [`ruamel.yaml`](https://pypi.org/project/ruamel.yaml/).

## Quick Start

### Using an Alternative Constructor

Instead of:

```python
with open(yaml_path, encoding="utf-8") as fh:
    yaml = ruamel.yaml.YAML(typ="rt").load("".join(fh))
```

change the import:

```python
with open(yaml_path, encoding="utf-8") as fh:
    yaml = ruamel_yaml_line_info.YAML(typ="rt").load("".join(fh))
```

and voila!

### Example

Consider the following YAML:

```yaml
foo: bar
block: >
  this is not
  a multiline
  block
single_quote: 'single'
double_quote: "double"
```

then we can get line and column information with

```python
>>> with open(yaml_path, encoding="utf-8") as fh:
    yaml = ruamel_yaml_line_info.YAML(typ="rt").load("".join(fh))
>>> print(yaml["foo"].lc)
LineCol(0, 5)
>>> print(yaml["block"].lc)
LineCol(1, 7)
>>> print(yaml["single_quote"].lc)
LineCol(5, 14)
>>> print(yaml["double_quote"].lc)
LineCol(6, 14)
```

where the first value in `LineCol` is the 0-based line, and the second value in `LineCol` is the 0-based column.

See the test for more exapmles.

### Patching an existing YAML object

If you already have a `ruamel.yaml.YAML` instance, you can add line
numbers with:

```python
with open(yaml_path, encoding="utf-8") as fh:
    yaml = ruamel.yaml.YAML(typ="rt").load("".join(fh))
    yaml = ruamel_yaml_line_info.YAML.with_line_numbers(yaml=yaml)
```

## Recommended Installation

Install the Python package and dependency management tool [`poetry`](https://python-poetry.org/docs/#installation) using official documentation.
You must have Python 3.11 or greater available on your system path, which could be managed by [`mamba`](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html), [`pyenv`](https://github.com/pyenv/pyenv), or another package manager. 
Finally, install the dependencies of the project with:

```console
poetry install
```

To check successful installation, run:

```console
python -c "import ruamel_yaml_line_info"
```

## Installing with Conda

Install the environment manager [`mamba`](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) using official documentation.
Create and activate a conda environment with Python 3.11 or greater:

```console
mamba create -c conda-forge -n ruamel_yaml_line_info ruamel-yaml-line-info python=3.11
mamba activate ruamel_yaml_line_info
```

Alternatively, install into an existing conda environment:

```console
mamba install -n <ENVIRONMENT> -c conda-forge ruamel-yaml-line-info
```

To check successful installation, run:

```console
python -c "import ruamel_yaml_line_info"
```

## Development and Testing

See the [contributing guide](./CONTRIBUTING.md) for more information.
