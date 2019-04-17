all: test

test:
	pytest -vv
.PHONY: test

build:
	pip3 install --user -r requirements.txt
.PHONY: build

run:
	python3 src/main.py
.PHONY: run
