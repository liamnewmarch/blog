FROM python:3.9-slim

WORKDIR /usr/src/app
COPY requirements*.txt .

RUN pip install \
    --no-cache-dir \
    --requirement requirements.txt \
    --requirement requirements-dev.txt
