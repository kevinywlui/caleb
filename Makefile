
.PHONY: tests lint

tests:
	poetry run pytest --cov=caleb tests

lint:
	flake8 --exclude=".git,__pycache__,.tox,.eggs,*.egg,consts.py" caleb bin tests
