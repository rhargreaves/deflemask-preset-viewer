PYTHONPATH := $(PWD)

all: test

test: build
	python3 -m pytest -vv
.PHONY: test

build:
	pip3 install --user -r requirements.txt
.PHONY: build

run:
	python3 -m deflemask_preset_viewer $(ARGS)
.PHONY: run

clean:
	rm -rf dist
.PHONY: clean

dist: build
	python3 -m pip install --upgrade build
	python3 -m build
.PHONY: dist

install: dist
	python3 -m pip install .
.PHONY: install

upload: dist
	python3 -m twine upload \
		--repository-url https://test.pypi.org/legacy/ \
		dist/*
.PHONY: upload
