FROM python:3.12-slim-bookworm

EXPOSE 8080

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY pyproject.toml /app
COPY uv.lock /app

RUN uv sync --frozen

COPY . /app

# Add execution permission to entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
