FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=backend.settings
ENV PYTHONPATH="backend"

ENV DJANGO_SUPERUSER_USERNAME=admin \
    DJANGO_SUPERUSER_PASSWORD=admin123 \
    DJANGO_SUPERUSER_EMAIL=admin@admin.com

EXPOSE 8000

CMD python manage.py migrate && \
    python manage.py createsuperuser --noinput || true && \
    gunicorn backend.wsgi:application --bind 0.0.0.0:8000
