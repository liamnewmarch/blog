# liam.nwmr.ch

## Local development

This project uses Docker Compose to run the front-end, back-end and database as separate services. The easiest way to get started is to install Docker Desktop and run:

```sh
touch .env
docker-compose up
```

This should build and start three containers: `datastore`, `django` and `static`. View the site by visiting [localhost:3000](http://localhost:3000).

You can interact with Django, npm, etc by addressing the relevant service:

```sh
# Create a Django superuser
docker-compose exec django python manage.py createsuperuser

# Run a static build
docker-compose exec static npm run build
```

In order to prevent Django from generating a new secret key each time the project is run, generate your own and add `DJANGO_SECRET_KEY=<your secret key>` to the `.env` file.

## Deploying to Google Cloud

A new version is deployed by Cloud Build when commits are pushed to the `main` branch in this repo. Manual builds can be triggered by running this in the root of the repo:

```sh
gcloud builds submit .
```
