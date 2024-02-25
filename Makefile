# Makefile for Edward the Editor.
#
# by torstein@skybert.net
#
SOURCES = src

all: format

format:
	pipenv run black $(SOURCES)

run:
	pipenv run python3 $(SOURCES)/edward.py
