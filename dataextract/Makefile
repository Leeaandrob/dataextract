clean:
	find . -name "*.pyc" -exec rm -rf {} \;

run: clean
	python manage.py runserver

shell: clean
	python manage.py shell
celeryd: clean
	python manage.py celeryd -v 2 -B -s celery -E -l INFO
