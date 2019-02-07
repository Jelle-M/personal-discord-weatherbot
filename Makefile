lint:
	poetry run flake8 weather_bot tests
mypy:
	poetry run mypy weather_bot
check: lint mypy
