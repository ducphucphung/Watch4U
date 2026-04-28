.PHONY: up down backend streamlit logs clean

# Spin up backend + Streamlit prototype
up:
	docker compose up --build

# Stop everything
down:
	docker compose down

# Run backend only (FastAPI on http://localhost:8000)
backend:
	docker compose up --build backend

# Run Streamlit only (http://localhost:8501)
streamlit:
	docker compose up --build streamlit

# Tail logs
logs:
	docker compose logs -f

# Remove containers + volumes
clean:
	docker compose down -v
