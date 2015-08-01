VENV = venv
PYTHON = $(VENV)/bin/python
DJANGO = $(VENV)/bin/django-admin.py


all: $(DJANGO)

help:
	@echo 'make ubuntu     install the necessary system packages (requires sudo)'
	@echo 'make            set up the development environment'
	@echo 'make run        start the development web server'
	@echo 'make test       run project test suite'
	@echo 'make test-fast  run project test suite with in momory sqlite database settings'

ubuntu:
	sudo apt-get update
	sudo apt-get -y build-dep python-psycopg2
	sudo apt-get -y install build-essential python-dev python-virtualenv

run: $(DJANGO) ; $(PYTHON) manage.py runserver

test: $(DJANGO)
	$(VENV)/bin/coverage erase
	$(VENV)/bin/coverage run --source=misago manage.py test --nologcapture misago
	$(VENV)/bin/coverage report --show-missing

test-fast: $(DJANGO)
	$(VENV)/bin/coverage erase
	$(VENV)/bin/coverage run --source=misago manage.py test --settings=misago.settings.fasttesting --nologcapture misago
	$(VENV)/bin/coverage report --show-missing

manage.cfg:
	echo '[default]' > $@
	echo 'settings = misago.settings.development' >> $@
	echo '' >> $@
	echo '[test]' >> $@
	echo 'settings = misago.settings.testing' >> $@


$(PYTHON): ; virtualenv --no-site-packages --python=python $@
$(DJANGO): $(PYTHON) manage.cfg requirements.txt setup.py ; $(VENV)/bin/pip install -e .[postgresql] && touch -c $@

.PHONY: all help ubuntu run test
