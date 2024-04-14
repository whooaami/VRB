#!/bin/bash
echo Starting server
poetry shell
alembic upgrade head
uvicorn main:app --workers 3 --host 0.0.0.0 --port 80 --proxy-headers --forwarded-allow-ips='*'
