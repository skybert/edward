# Makefile for Edward the Editor.
#
# by torstein@skybert.net
#
SOURCES = src

default: format lint

all: install format lint run

install:
	pipenv install

format:
	pipenv run black $(SOURCES)

lint:
	pipenv run pylint $(SOURCES)

run:
	pipenv run python3 $(SOURCES)/edward.py
