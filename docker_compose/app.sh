#!/bin/bash

alembic upgrade head
uvicorn app:create_app --factory --app-dir src/ --host=0.0.0.0 --port=8080 --workers 4