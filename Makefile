DC = sudo docker compose
APP_FILE = docker_compose/app.yaml
POSTGRES_FILE = docker_compose/postgres.yaml
NGINX_FILE = docker_compose/nginx.yaml

all:

start_all: start_postgres start_app start_nginx

drop_all: drop_postgres drop_app drop_nginx

start_app:
	$(DC) -f $(APP_FILE) up --build -d

drop_app:
	$(DC) -f $(APP_FILE) down

start_postgres:
	$(DC) -f $(POSTGRES_FILE) up --build -d

drop_postgres:
	$(DC) -f $(POSTGRES_FILE) down

start_nginx:
	$(DC) -f $(NGINX_FILE) up --build -d

drop_nginx:
	$(DC) -f $(NGINX_FILE) down

logs_all: 
	$(DC) -f $(APP_FILE) -f $(POSTGRES_FILE) -f $(NGINX_FILE) logs -f

logs_app:
	$(DC) -f $(APP_FILE) logs -f

logs_postgres:
	$(DC) -f $(POSTGRES_FILE) logs -f

logs_nginx:
	$(DC) -f $(NGINX_FILE) logs -f

lint:
	black  --config .black src/
	flake8 --verbose --enable-extensions=flake8-bugbear,flake8-simplify,flake8-async,flake8-unused-arguments,flake8-commas,flake8-comprehensions,flake8-quotes,flake8-builtins,pep8-naming,flake8-functions,flake8-alphabetize,flake8-import-order,flake8-annotations-coverage --config .flake8 src/
	mypy  --config-file .mypy.ini src/
