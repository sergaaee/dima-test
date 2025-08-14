FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y postgresql-client

COPY app/requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the wait-for-postgres.sh script into the container
COPY app/wait-for-postgres.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-postgres.sh

COPY app /code/

CMD ["sh", "-c", "wait-for-postgres.sh db gunicorn -k uvicorn.workers.UvicornWorker -c gunicorn_config.py main:app"]


