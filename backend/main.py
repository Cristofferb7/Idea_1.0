from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI()

# Allow frontend (React) requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load mock matchup data
DATA_PATH = Path(__file__).parent / "data" / "mock_matchups.json"
if DATA_PATH.exists():
    matchups = json.loads(DATA_PATH.read_text())
else:
    matchups = {}

@app.get("/")
def root():
    return {"message": "AI Fighter Matchup backend running!"}

@app.get("/api/fighter/{name}")
def get_fighter(name: str):
    fighter = matchups.get(name)
    if fighter:
        return {"fighter": name, "source": "mock", **fighter}
    return {"error": "Fighter not found"}