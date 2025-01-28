#!/bin/bash

# Aplicar as migrations
uv run flask db upgrade

# Executar o aplicativo Flask usando Gunicorn
# exec uv run gunicorn --bind 0.0.0.0:8080 "backend:create_app()" --timeout 100 --workers 4 --certfile=certs/certificate.crt --keyfile=certs/privatekey.key --access-logfile - --error-logfile -;
exec uv run gunicorn --bind 0.0.0.0:8080 "backend:create_app()" --timeout 100 --workers 4 --access-logfile - --error-logfile -;