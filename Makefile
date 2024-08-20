test:
	docker compose run --rm app python manage.py test

makemigrations:
	docker compose run --rm app python manage.py makemigrations

up:
	docker compose up

init:
	cd tailwind && npm install

start:
	make start_parallel -j2

start_parallel: start_tailwind start_django

start_django:
	docker compose up

start_tailwind:
	cd tailwind && npm start