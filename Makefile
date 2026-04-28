.PHONY: up down restart backend streamlit logs clean

# Spin up backend + Streamlit prototype
up:
	docker compose up --build

# Stop everything
down:
	docker compose down

# Restart containers (stop + rebuild + start)
restart:
	docker compose down
	docker compose up --build

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
