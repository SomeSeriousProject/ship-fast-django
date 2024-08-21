CURRENT_FOLDER := $(notdir $(CURDIR))

PROJ_NAME_DEV := $(CURRENT_FOLDER)"_dev"
PROJ_NAME_DEPLOY := $(CURRENT_FOLDER)"_deploy"

COMPOSE_FILE_DEV := "docker/compose.yml"
COMPOSE_FILE_DEPLOY := "docker/compose.deploy.yml"

test:
	docker compose -p $(PROJ_NAME_DEV) run --rm app python manage.py test

makemigrations:
	docker compose -p $(PROJ_NAME_DEV) run --rm app python manage.py makemigrations

init:
	cd tailwind && npm install

start:
	make start_parallel -j2

start_parallel: start_tailwind start_django

start_django:
	docker compose -p $(PROJ_NAME_DEV) -f $(COMPOSE_FILE_DEV) up

start_tailwind:
	cd tailwind && npm start


# Deploy commands
deploy:
	git pull && \
	docker compose -p $(PROJ_NAME_DEPLOY) -f $(COMPOSE_FILE_DEPLOY) up -d --build

deploy-down:
	docker compose -p $(PROJ_NAME_DEPLOY) -f $(COMPOSE_FILE_DEPLOY) down