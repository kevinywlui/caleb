
.PHONY: tests lint

tests:
	mypy --ignore-missing-imports caleb
	pytest --cov=caleb tests

lint:
	black --exclude ".*setup\.py|\.eggs" --check .
