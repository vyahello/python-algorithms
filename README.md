[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![Build Status](https://travis-ci.org/vyahello/python-algorithms.svg?branch=master)](https://travis-ci.org/vyahello/python-algorithms)

# Python algorithms

> This project is aimed to discover algorithms using `python` programming language (for education mostly).
>
> All source code is located under [algorithms](algorithms) package.
>
> **Note:** it is under construction.

## Tools
- python 3.6, 3.7, 3.8
- code analysis
  - [black](https://black.readthedocs.io/en/stable/)
  - [pylint](https://www.pylint.org/)
  - [xdoctest](https://github.com/Erotemic/xdoctest)

## Content
- [Sorting](algorithms/sort)

## Development notes

### Run unittests

In order to execute just unittests, please run following command (note `xdoctest` tool is used as a test runner):
```
➜ python -m xdoctest algorithms
```

### CI

Project has Travis CI integration thus code analysis (`black`, `pylint`) and unittests (`xdoctest`) will be run automatically
after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
➜ ./run-code-analysis.sh
```

### Meta

Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
