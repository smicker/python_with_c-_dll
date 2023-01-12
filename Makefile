
check_lint:
	pylint python_wrapper
	flake8 python_wrapper

check_types:
	mypy python_wrapper --ignore-missing-imports

check_format:
	black --check python_wrapper

fix_format:
	black python_wrapper

check_unit_tests:
	$(info Running unit tests...)
	pytest -m unit -ra --junitxml=reports/test_results_unit_tests.xml

check_all: check_lint check_types check_format check_unit_tests

build_c_code:
	cd c_lib && make && cd ..

run_python:
	cd python_wrapper && ./do_math.py