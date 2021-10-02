.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")

.PHONY: help
help:             ## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: virtualenv
virtualenv:       ## Create a virtual environment.
	@echo "creating virtualenv ..."
	@rm -rf .venv
	@virtualenv -p python3.6 .venv
	@./.venv/bin/pip install -U pip
	@echo
	@echo "!!! Please run 'source .venv/bin/activate' to enable the environment !!!"

.PHONY: show
show:             ## Show the current environment.
	@echo "Current environment:"
	@echo "Running using $(ENV_PREFIX)"
	@$(ENV_PREFIX)python -V
	@$(ENV_PREFIX)python -m site

.PHONY: install
install:          ## Install the project in dev mode.
	@echo "Don't forget to run 'make virtualenv' if you got errors."
	@echo "Don't forget to run 'source .venv/bin/activate' to enable the environment before installing"
	@echo -n "Press [ENTER] to continue..."
	@read anykeys
	$(ENV_PREFIX)pip install -e .[dev]

.PHONY: format
format:              ## Format code using black & isort.
	$(ENV_PREFIX)isort instagram_download/
	$(ENV_PREFIX)black instagram_download/


.PHONY: lint
lint:             ## Run black, mypy, pylint linters.
	$(ENV_PREFIX)isort --check-only instagram_download/
	$(ENV_PREFIX)black --check instagram_download/
	$(ENV_PREFIX)pylint instagram_download/
	$(ENV_PREFIX)mypy instagram_download/


.PHONY: format_changes
format_changes:              ## Format code using darker & isort.
	$(ENV_PREFIX)darker


.PHONY: lint_changes
lint_changes:             ## Run black, mypy, pylint linters.
	$(ENV_PREFIX)darker --lint pylint --lint mypy --check

.PHONY: clean
clean:            ## Clean unused files.
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@rm -rf .cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf .tox/
	@rm -rf docs/_build


.PHONY: release
release:          ## Create a new tag for release.
	@echo "WARNING: This operation will create a version tag"
	@echo "Don't forget to run 'source .venv/bin/activate' to enable the environment before release"
	@echo -n "Press [ENTER] to continue..."
	@read anykeys
	@read -p "Version? (provide the next x.y.z semver) : " TAG
	@echo "creating git tag : $${TAG}"
	@git tag $${TAG}
	@echo "$${TAG}" > instagram_download/VERSION
	@$(ENV_PREFIX)gitchangelog > HISTORY.md
	@git add instagram_download/VERSION HISTORY.md
	@git commit -m "release: version $${TAG} 🚀"