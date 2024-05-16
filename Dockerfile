FROM python:3.11-alpine
EXPOSE 8001

WORKDIR /app

COPY ./pyproject.toml ./alembic.ini ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/

ENV ASYNC_DATABASE_URL="postgresql+asyncpg://admin:admin@localhost:5432/measurements"
ENV DATABASE_URL="postgresql://admin:admin@localhost:5432/measurements"


CMD alembic upgrade head && \
uvicorn app.main:app --port 8001 --host 0.0.0.0 --interface=asgi3