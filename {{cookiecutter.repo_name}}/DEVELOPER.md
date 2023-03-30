# Developer

## Table of Contents

* [Installation](#installation)
    * [Pre-requisites](#pre-requisites)
    * [Repository](#repository)
    * [Environment](#environment)
    * [Hooks](#hooks)
* [Linting](#linting)
* [Testing](#testing)

---

## Installation

### Pre-requisites

Please install the following:

1. [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2. [Python {{cookiecutter.python_version}}](https://www.python.org/downloads/)

### Repository

Clone the repository:

```bash
git clone https://github.com/{{cookiecutter.github_organisation}}/{{cookiecutter.repo_name}}
cd {{cookiecutter.repo_name}}
```

### Environment

Create and activate a virtual environment:

```bash
# Note: Make sure you are using Python {{cookiecutter.python_version}}!
python -m venv .env
source .env/bin/activate
```

Install the requirements:

```bash
python -m pip install -r requirements.txt
```

### Hooks

Install the hooks:

```bash
# Note: You must be in a git repository for pre-commit to work
pre-commit install
```

## Linting

To lint the project:

```bash
pre-commit run
```

## Testing

To test the project:

```bash
python -m pytest -v tests
```

To generate test coverage (optional):
```bash
coverage run -m pytest -v tests
coverage report --omit="tests/*"
```
