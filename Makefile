
.PHONY: tests lint

tests:
	poetry run mypy --ignore-missing-imports caleb
	poetry run pytest --cov=caleb tests

lint:
	black --exclude ".*setup\.py|\.eggs" --check .
