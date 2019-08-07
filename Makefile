
.PHONY: tests lint

tests:
	mypy caleb
	poetry run pytest --cov=caleb tests

lint:
	black --exclude ".*setup\.py|\.eggs" --check .
