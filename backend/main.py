from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()



# Allow frontend (React) requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    email: EmailStr
    password: str


# Load mock matchup data
DATA_PATH = Path(__file__).parent / "data" / "mock_matchups.json"
if DATA_PATH.exists():
    matchups = json.loads(DATA_PATH.read_text())
else:
    matchups = {}

#Load test file
DATA_PATH = Path(__file__).parent / "data" / "test.json"
if DATA_PATH.exists():
    test_matchups = json.loads(DATA_PATH.read_text())
else:
    test_matchups = {}

@app.get("/")
def root():
    return {"message": "AI Fighter Matchup backend running!"}

@app.get("/home/login")
def login():
    return{"login page working!"}

@app.get("/home/matchup/{name}")
def get_fighter(name: str):

    #Converts inputted name to have proper captilization
    name=name.lower()
    name=name.title()
    
    fighter = test_matchups.get(name)
    fighter_list=fighter["matchups"]
    End=len(fighter_list)
    worst_matchup=fighter_list[End-3:End]
    if fighter:
        return {"fighter": name, 
                "matchups": fighter_list,
                "best": fighter_list[0:3],
                "worst":worst_matchup[::-1],
                "summary":fighter["summary"]
                }
    else:
        return {"error": "Fighter not found" } 

