
init:
	pip install -r requirements.txt

test:
	py.test tests

.PHONY: init test


publish:
	rm -rf dist
	python setup.py sdist
	twine upload dist/*
