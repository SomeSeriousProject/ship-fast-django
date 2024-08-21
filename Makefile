CURRENT_FOLDER := $(notdir $(CURDIR))
PROJ_NAME_DEPLOY := $(CURRENT_FOLDER)"_deploy"

# Core commands for dev
test:
	docker compose run --rm app python manage.py test

makemigrations:
	docker compose run --rm app python manage.py makemigrations

up:
	docker compose up

up-rebuild:
	docker compose up --build

down:
	docker compose down

createsuperuser:
	docker compose run --rm app python manage.py createsuperuser

# Start dev environment
dev:
	make start_parallel -j2

start_parallel: start_tailwind up

start_tailwind:
	npm start


# Deploy commands
deploy:
	git pull && \
	docker compose -p $(PROJ_NAME_DEPLOY) up -d --build

deploy-down:
	docker compose -p $(PROJ_NAME_DEPLOY) down

deploy-createsuperuser:
	docker compose -p $(PROJ_NAME_DEPLOY) run --rm app python manage.py createsuperuser