## Purpose
Short, actionable guidance for AI coding agents working on the ai_fighter_matchup repository. Focus on where code lives, how components interact, and exact commands to run and verify changes.

## Big picture
- Two folders: `backend/` (FastAPI server) and `frontend/` (Create React App). The backend serves mock matchup data from `backend/data/mock_matchups.json` and exposes endpoints in `backend/main.py` (notably `/` and `/api/fighter/{name}`). The frontend is a standard CRA app in `frontend/` and uses `axios` for HTTP requests (see `frontend/package.json`).

## Key files and patterns (source-of-truth)
- `backend/main.py` — single-file FastAPI app. Add or change API routes here. It already registers `CORSMiddleware` with permissive origins ("*").
- `backend/data/mock_matchups.json` — JSON mock data used by the backend. Edit keys/values directly to change responses.
- `frontend/package.json` — frontend start/build/test scripts. Use `npm start` to run the dev server.
- `frontend/src/` — React app entry points. Modify `App.js` or add components that call the backend API.

## How to run locally (exact commands)
- Backend (use workspace virtualenv `.venv`):
  - Install deps (if missing):
    /Users/cristoffersmacbook/Documents/hackathonProject/.venv/bin/python -m pip install fastapi uvicorn
  - Start server (auto-reload):
    /Users/cristoffersmacbook/Documents/hackathonProject/.venv/bin/python -m uvicorn backend.main:app --reload

- Frontend (from `frontend/`):
  - Install and start:
    cd frontend
    npm install
    npm start

Notes: The backend listens on `127.0.0.1:8000` by default. CORS is already enabled in `backend/main.py` so the CRA front-end can call `http://127.0.0.1:8000` during development.

## Editor / environment notes
- The project uses a virtualenv at `.venv/` (workspace root). Point VS Code's Python interpreter to `/Users/cristoffersmacbook/Documents/hackathonProject/.venv/bin/python` so Pylance resolves imports (e.g., `fastapi`).
- If imports cannot be resolved, verify with:
  /Users/cristoffersmacbook/Documents/hackathonProject/.venv/bin/python -m pip show fastapi

## Examples for common agent tasks
- Add a new API route: edit `backend/main.py`, add a new `@app.get("/api/your-route")` function, run uvicorn and smoke-test with `curl`.
- Update mock data: edit `backend/data/mock_matchups.json`. The server will pick up changes after restart (or immediately if using reload).
- Frontend call example (JS): use `axios.get('http://127.0.0.1:8000/api/fighter/Ryu')` and expect JSON matching keys from `mock_matchups.json`.

## Conventions & caveats
- Backend is intentionally small and file-centered (no package/module layout). Keep API work inside `backend/main.py` or create `backend/` modules if adding complexity.
- CORS is permissive for local development. Tighten origins before any production deployment.
- No backend tests or requirements file present — pinning dependencies or adding `requirements.txt`/`pyproject.toml` should be done consciously and documented.

## Quick verification checklist for PRs
1. Start backend with the `.venv` Python and confirm `GET /` returns the running message.
2. Confirm `GET /api/fighter/{name}` returns expected mock response for an existing name (e.g., `Ryu`).
3. Run `npm start` in `frontend/` and verify the UI can call the backend (network tab or console errors).

If any of the above is unclear or you want the file to include more developer workflows (like Docker, CI, or test scaffolding), tell me which workflow to document and I will extend this file.
