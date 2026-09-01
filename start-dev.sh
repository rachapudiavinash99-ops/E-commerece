#!/usr/bin/env bash
echo "========================================================"
echo "  CodePulse Academy - Full-Stack Platform Launcher"
echo "========================================================"
(cd backend && uvicorn app.main:app --reload --port 8000) &
BACKEND_PID=$!
(cd frontend && npm run dev) &
FRONTEND_PID=$!
trap "kill $BACKEND_PID $FRONTEND_PID; exit" SIGINT SIGTERM
wait
