FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app


COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate"]

CMD ["sh", "-c", "python manage.py load_profiles && gunicorn wall_tracker_app.wsgi:application --bind 0.0.0.0:8000"]