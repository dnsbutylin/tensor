PROJECT := tensor
VERSION := 0.1.0

REPORTS := .reports

TESTS := tests
SOURCES := src

IMAGE_NAME := $(PROJECT)
SSH_KEY_PATH := $(HOME)/.ssh/id_rsa

ifeq ($(OS),Windows_NT)
    PY_FILES := $(shell powershell -Command "Get-ChildItem $(SOURCES) -Recurse -Filter '*.py' | Select-Object -ExpandProperty FullName")
else
    PY_FILES := $(shell find $(SOURCES) $(TESTS) -name "*.py")
endif

$(VENV):
	poetry install --no-root

$(REPORTS):
	mkdir $(REPORTS)

setup: $(VENV) $(REPORTS) ## Настройка рабочего окружения

flake8: setup
	poetry run flake8 $(SOURCES)
	poetry run flake8-markdown "*.md"

mypy: setup
	poetry run mypy $(SOURCES)

bandit: setup
	poetry run bandit -qr $(SOURCES)  -c .bandit.yml -o $(REPORTS)/bandit.json -f json

pylint: setup
	poetry run pylint -v $(SOURCES) > $(REPORTS)/pylint.txt

isort: setup
	poetry run isort $(SOURCES)

isort-lint: setup
	poetry run isort -c $(SOURCES)

black: setup
	poetry run black $(SOURCES) --quiet

black-lint: setup
	poetry run black $(SOURCES) --check

yesqa: setup
	poetry run yesqa $(PY_FILES)

cyclonedx-bom: setup
	poetry run cyclonedx-py -p -i poetry.lock -o $(REPORTS)/cyclonedx-bom.xml --force

ui-tests: setup  ## Запуск интеграционных тестов
	poetry run pytest $(TESTS)

all-tests: ui-tests  ## Запуск всех тестов

format: yesqa isort black ## Форматирование исходного кода

lint: flake8 bandit mypy pylint isort-lint black-lint cyclonedx-bom  ## Запуск статического анализа

all: format lint all-tests

.DEFAULT_GOAL := all
