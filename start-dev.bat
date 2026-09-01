@echo off
echo ========================================================
echo   CodePulse Academy - Full-Stack Platform Launcher
echo ========================================================
echo Starting Backend API Server on http://localhost:8000...
start cmd /k "cd backend && python -m uvicorn app.main:app --reload --port 8000"
echo Starting Frontend Dev Server on http://localhost:5173...
start cmd /k "cd frontend && npm run dev"
echo Platform running!
