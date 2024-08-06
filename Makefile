lint:
	black  --config .black src/
	flake8 --verbose --enable-extensions=flake8-bugbear,flake8-simplify,flake8-async,flake8-unused-arguments,flake8-commas,flake8-comprehensions,flake8-quotes,flake8-builtins,pep8-naming,flake8-functions,flake8-alphabetize,flake8-import-order,flake8-annotations-coverage --config .flake8 src/
	mypy  --config-file .mypy.ini src/