test:
	pytest -v

publish: clean
	python setup.py sdist bdist_wheel
	twine upload -s dist/*

clean:
	rm -rf *.egg-info *.egg dist build .pytest_cache


install-from-git-via-pipx:
	pipx install git+git://github.com/mvtango/jinja2-cli@feature-load-tsv#egg=jinja2-cli

.PHONY: test publish clean
