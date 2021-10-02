# How to develop on this project


**This instructions are for linux base systems. (Linux, MacOS, BSD, etc.)**

## Setting up your own virtual environment

Run `make virtualenv` to create a virtual environment.
then activate it with `source .venv/bin/activate`.

## Install the project in develop mode

Run `make install` to install the project in develop mode.

## Create a new branch to work on your contribution

Run `git checkout -b feat/my_contribute`  
## Make your changes

Edit the files using your preferred editor.

## Format the code

Run `make format` to format the code.

## Run the linter

Run `make lint` to run the linter.

## Test your changes

Run `make test` to run the tests.

Ensure code coverage report shows `100%` coverage, add tests to your PR.


## Commit your changes

This project uses [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0/).

Example: `fix(package): update setup.py arguments 🎉` (emojis are fine too)

## Push your changes to your fork

Run `git push origin feat/my_contribute`

## Submit a merge request

On git.paas.vn, click on `Pull Request` button.


## Makefile utilities

This project comes with a `Makefile` that contains a number of useful utility.

```bash 
❯ make
Usage: make <target>

Targets:
help:             ## Show the help.
virtualenv:       ## Create a virtual environment.
install:          ## Install the project in dev mode.
format:           ## Format code using black & isort.
lint:             ## Run black, mypy, pylint linters.
format_changes:   ## Format modified code using darker & isort.
lint_changes:     ## Run darker, mypy, pylint linters on modified code.
test:             ## Run tests and generate coverage report.
release:          ## Create a new tag for release.
init:             ## Initialize the project based on an application template.
```

## Making a new release(For Maintainer)

This project uses [semantic versioning](https://semver.org/) and tags releases with `X.Y.Z`  

To trigger a new release all you need to do is.

1. Run the tests to ensure everything is working.
2. Run `make release` to create a new tag.
3. `git push -u origin HEAD --tags` to push it to the remote repo

The `make release` will ask you the version number to create the tag, ex: type `0.1.1` when you are asked.

> **CAUTION**:  The make release will change local changelog files and commit all the unstaged changes you have.