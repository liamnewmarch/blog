FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app
COPY requirements*.txt .

RUN pip install \
    --requirement requirements.txt \
    --requirement requirements-dev.txt \
    --no-cache-dir

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
