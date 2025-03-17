dependencies:
	pip freeze > requirements.txt

server:
	python -B -m uvicorn backend.main:app --reload