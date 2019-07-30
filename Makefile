
.PHONY: tests lint

tests:
	poetry run pytest --cov=caleb tests

lint:
	black --check .
