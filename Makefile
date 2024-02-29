# Makefile for Edward the Editor.
#
# by torstein@skybert.net
#
SOURCES = src

default = run

all: format

install:
	pipenv install

format:
	pipenv run black $(SOURCES)

lint:
	pipenv run pylint $(SOURCES)

run:
	pipenv run python3 $(SOURCES)/edward.py
