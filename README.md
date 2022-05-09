# liam.nwmr.ch

This is the source code for my blog. It’s a [Django](https://www.djangoproject.com) project that runs on [Google App Engine](https://cloud.google.com/appengine/) using [Djangae](https://gitlab.com/potato-oss/djangae/djangae).

## Local development

To run this project locally you’ll need Docker installed. It’s possible to run the project without Docker if you know what you’re doing. The easiest way to get up and running is to install [Docker Desktop](https://www.docker.com/products/docker-desktop/).

The project uses Docker Compose to run three separate containers, one for the Google Cloud Datastore emulator, one for the Django back-end, and one for the front-end server. You can run all three with:

```sh
make
```

This should create an empty `.env` file, and then build and start three containers: `datastore`, `django` and `static`. With that running, in a new shell run:

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
