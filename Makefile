all: test

test:
	python3 -m pytest -vv
.PHONY: test

build:
	pip3 install --user -r requirements.txt
.PHONY: build

run:
	python3 src/main.py
.PHONY: run

clean:
	rm -rf dist
.PHONY: clean

dist: build
	python3 setup.py sdist bdist_wheel
.PHONY: dist

upload: dist
	python3 -m twine upload \
		--repository-url https://test.pypi.org/legacy/ \
		dist/*
.PHONY: upload
