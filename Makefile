.PHONY: install test test_integration

install:
	python setup.py install

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

test: install
	py.test test/unit_tests

test_integration: install
	py.test test/integration_tests