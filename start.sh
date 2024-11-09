#!/bin/sh
cd frontend 
npm run lint && npm run format-fix
cd ..
cd backend
sh format.sh
cd ..
docker compose up --build