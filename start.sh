#!/bin/sh
set -e

cd frontend 
npm run lint && npm run format-fix
cd ..
cd backend
uvx ruff check
cd ..
docker compose up --build