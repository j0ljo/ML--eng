
FastAPI Project — Quick Setup
Prerequisites

Python 3.11+ installed (or use a version manager: pyenv / asdf / pn).

Git (optional).

Quick setup (copy & run)

Create and activate a virtual environment
Unix / macOS

python -m venv .venv
source .venv/bin/activate


Windows (PowerShell)

python -m venv .venv
.\.venv\Scripts\Activate.ps1


Create requirements.txt (top-level) with:

fastapi
uvicorn[standard]


Install dependencies

pip install -r requirements.txt


Ensure your app entrypoint exposes app (example)

store_api/
  └─ main.py   # contains: app = FastAPI()


Create .gitignore (top-level) — minimal example:

.venv/
__pycache__/
*.pyc
.DS_Store
.env
.vscode/


Run the app (development, auto-reload)

uvicorn store_api.main:app --reload


Test endpoints

GET root:

curl -v http://127.0.0.1:8000/


POST JSON:

curl -X POST http://127.0.0.1:8000/post \
  -H "Content-Type: application/json" \
  -d '{"body":"hello"}'