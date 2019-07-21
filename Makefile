
.PHONY: tests

tests:
	poetry run pytest --cov=caleb tests

