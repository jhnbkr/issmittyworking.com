.PHONY: install run web

install:
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000

web:
	gunicorn app:app --log-file -