.PHONY: install test test_integration

install:
	python setup.py install

clean:
	rm -r build
	rm -r dist
	rm -r *.egg-info

test: install
	py.test test/unit_tests

test_integration: install
	py.test test/integration_tests
