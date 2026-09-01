# CodePulse Academy Build Automation
.PHONY: help install start test lint format clean seed docker-up docker-down

help:
	@echo "Available commands:"
	@echo "  make install     - Install backend & frontend dependencies"
	@echo "  make start       - Start both backend and frontend servers"
	@echo "  make test        - Run backend and frontend test suites"
	@echo "  make seed        - Populate database with realistic courses & topics"
	@echo "  make docker-up   - Start application with Docker Compose"
	@echo "  make docker-down - Stop Docker Compose containers"

install:
	cd backend && pip install -r requirements.txt
	cd frontend && npm install

start:
	./start-dev.sh

test:
	cd backend && pytest -v
	cd frontend && npm test

seed:
	cd backend && python -m app.seeds.runner

docker-up:
	docker-compose up --build -d

docker-down:
	docker-compose down
