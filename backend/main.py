from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from pathlib import Path
from typing import Optional
from services.gemini_agent import analyze_fighter

class LoginRequest(BaseModel):
    username: str
    password: str

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

@app.post("/api/login")
async def login(credentials: LoginRequest):
    # For demo purposes - you should implement proper authentication
    if credentials.username and credentials.password:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.get("/api/fighter/{name}")
def get_fighter(name: str, game: Optional[str] = None):
    # Try mock data first
    fighter = matchups.get(name)
    if fighter:
        return {"fighter": name, "source": "mock", **fighter}
    
    # If no mock data, use Gemini
    try:
        analysis = analyze_fighter(name, game)
        return {"source": "gemini", **analysis}
    except Exception as e:
        return {"error": f"Analysis failed: {str(e)}"}