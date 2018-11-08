prepare:
	source .venv/bin/activate; python setup.py sdist bdist_wheel

upload:
	source .venv/bin/activate; twine upload dist/*

