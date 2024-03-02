FROM python:3.9.2-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --no-cache-dir Flask gunicorn
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install alembic
RUN pip install psycopg2-binary
RUN pip install Flask-SQLAlchemy

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

COPY ./app /app/

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]