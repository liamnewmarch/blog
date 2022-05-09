FROM python:3.9-slim

WORKDIR /usr/src/app
COPY src/requirements*.txt src/

RUN pip install \
    --no-cache-dir \
    --requirement src/requirements.txt \
    --requirement src/requirements-dev.txt
