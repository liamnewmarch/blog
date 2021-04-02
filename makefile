CONTAINER := docker-compose
DJANGO := $(CONTAINER) exec django python manage.py
NPM :=  $(CONTAINER) exec npm

.PHONY: default
default:
	$(MAKE) start

.env:
	touch .env

.PHONY: setup
setup:
	$(DJANGO) migrate
	$(DJANGO) createsuperuser
	$(DJANGO) loaddata fixtures/placeholder.yaml

.PHONY: start
start:
	$(MAKE) .env
	$(CONTAINER) up

.PHONY: stop
stop:
	$(CONTAINER) stop

.PHONY: test
test:
	$(DJANGO) test
	$(NPM) test
