FROM python:3.11-slim

WORKDIR /app
COPY ./src/ /app

RUN apt-get update && apt-get install -y netcat-traditional


COPY ./pyproject.toml /code/pyproject.toml
RUN pip install /code/.

EXPOSE 8000

#CMD ["sh", "entrypoint.sh"]