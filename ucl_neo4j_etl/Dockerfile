FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-traditional

COPY ./src/ /app

COPY ./pyproject.toml /code/pyproject.toml
RUN pip install /code/.

#CMD ["sh", "entrypoint.sh"]