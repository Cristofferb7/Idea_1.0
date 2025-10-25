# backend/services/gemini_agent.py
import os, json, re
from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv
import google.generativeai as genai

# Load env and configure Gemini
load_dotenv(Path(__file__).resolve().parents[1] / ".env")
genai.configure(api_key=os.getenv("GEMINI_KEY"))

# Choose a fast model; swap to 1.5-pro if you want stronger reasoning
_MODEL = genai.GenerativeModel("gemini-1.5-flash")

# Strict schema prompt: keeps output predictable for the frontend
_SCHEMA_PROMPT = """You are a fighting game matchup analyst.

Return ONLY valid JSON in this exact schema:
{
  "fighter": string,
  "summary": string,
  "counters": [ { "name": string, "reason": string } ],
  "victims":  [ { "name": string, "reason": string } ],
  "notes": string
}

Rules:
- If the input is ambiguous, set "summary" to "Needs clarification" and leave lists empty.
- Prefer 3–5 items in each list. Be concise. Avoid patch/version speculation unless necessary.
"""

def _parse_json(text: str) -> Dict[str, Any]:
    text = (text or "").strip()
    # Extract the last JSON object if the model added extra prose
    m = re.search(r"\{.*\}\s*$", text, re.S)
    blob = m.group(0) if m else text
    try:
        data = json.loads(blob)
    except Exception:
        data = {"fighter": "", "summary": text, "counters": [], "victims": [], "notes": "Unparsed"}
    # Normalize keys
    data.setdefault("summary", "")
    data.setdefault("counters", [])
    data.setdefault("victims", [])
    data.setdefault("notes", "")
    # Trim to at most 5
    data["counters"] = data["counters"][:5]
    data["victims"]  = data["victims"][:5]
    return data

def analyze_fighter(fighter: str, game: str | None = None) -> Dict[str, Any]:
    user = f"Character: {fighter}\nGame/Franchise: {game or 'unspecified'}"
    resp = _MODEL.generate_content([_SCHEMA_PROMPT, user])
    return _parse_json(resp.text)