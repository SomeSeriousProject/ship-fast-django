CURRENT_FOLDER := $(notdir $(CURDIR))

PROJ_NAME_DEPLOY := $(CURRENT_FOLDER)"_deploy"

COMPOSE_FILE_DEV := "docker/compose.yml"
COMPOSE_FILE_DEPLOY := "docker/compose.deploy.yml"

test:
	docker compose -f $(COMPOSE_FILE_DEV) run --rm app python manage.py test

makemigrations:
	docker compose -f $(COMPOSE_FILE_DEV) run --rm app python manage.py makemigrations

down:
	docker compose -f $(COMPOSE_FILE_DEV) down

up-rebuild:
	docker compose -f $(COMPOSE_FILE_DEV) up --build

init:
	cd tailwind && npm install

start:
	make start_parallel -j2

start_parallel: start_tailwind start_django

start_django:
	docker compose -f $(COMPOSE_FILE_DEV) -f $(COMPOSE_FILE_DEV) up

start_tailwind:
	cd tailwind && npm start


# Deploy commands
deploy:
	git pull && \
	docker compose -p $(PROJ_NAME_DEPLOY) -f $(COMPOSE_FILE_DEPLOY) up -d --build

deploy-down:
	docker compose -p $(PROJ_NAME_DEPLOY) -f $(COMPOSE_FILE_DEPLOY) down