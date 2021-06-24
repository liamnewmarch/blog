# liam.nwmr.ch

## Local development

This project uses Docker Compose to run the front-end, back-end and database as separate services. The easiest way to get started is to install Docker Desktop and run:

```sh
make
```

This should create an `.env` file, and build and start three containers: `datastore`, `django` and `static`. With that running, in a new shell run:

```sh
make setup
```

This should apply migrations, prompt you to create an admin user, and load placeholder fixtures for local development. Once this is done you can view the site by visiting [localhost:3000](http://localhost:3000), and the admin by visiting [localhost:3000/admin/](http://localhost:3000/admin/).

You can interact with Django, npm, etc via Docker Compose:

```sh
# Django
docker compose exec django python manage.py help

# npm
docker compose exec static npm run
```

In order to prevent Django from generating a new secret key each time the project is run, you can generate your own and add it to the `.env` file as `DJANGO_SECRET_KEY=<your secret key>`.

## Deploying to Google Cloud

A new version is deployed by Cloud Build when commits are pushed to the `main` branch in this repo. Manual builds can be triggered by installing [gcloud](https://cloud.google.com/sdk/gcloud) and running this in the root of the repo:

```sh
gcloud builds submit .
```
