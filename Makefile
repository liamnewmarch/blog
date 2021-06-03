datastore := docker compose exec datastore
django := docker compose exec django
static :=  docker compose exec static

django-apps := contact blog pages projects
django-fixtures := fixtures/placeholder.yaml

.PHONY: default
default: start

.env:
	touch .env

.PHONY: setup
setup:
	$(django) python manage.py migrate
	$(django) python manage.py createsuperuser
	$(django) python manage.py loaddata $(django-fixtures)

.PHONY: start
start: .env
	docker compose up --detach

.PHONY: stop
stop:
	docker compose stop

.PHONY: test
test:
	$(django) flake8
	$(django) python -Wa manage.py test
	$(static) npm test

.PHONY: update-fixtures
update-fixtures:
	$(django) python manage.py dumpdata $(django-apps) --format=yaml --output=$(django-fixtures)
