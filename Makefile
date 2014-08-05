
default: test

detox-test:
	detox

travis-test: test

test: env
	.env/bin/nosetests

coverage-test: env
	.env/bin/coverage run .env/bin/nosetests

env: .env/.up-to-date

.env/.up-to-date: setup.py Makefile
	virtualenv .env
	.env/bin/pip install -e .
	.env/bin/pip install nose
	.env/bin/pip install python-coveralls
	touch .env/.up-to-date

doc: env
	.env/bin/python setup.py build_sphinx

.PHONY: doc
