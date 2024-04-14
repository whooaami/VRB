#!/bin/bash
echo Starting server
poetry shell
poetry run alembic upgrade head
poetry run uvicorn main:app --reload --workers 3 --host 0.0.0.0 --port 80 --proxy-headers --forwarded-allow-ips='*'
