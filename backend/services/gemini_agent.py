# backend/services/gemini_agent.py
import os, json, re
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv
import google.generativeai as genai
import google.ai.generativelanguage as genai_types

# Load env and configure Gemini
env_path = Path(__file__).resolve().parents[1] / ".env"
print(f"Loading .env from: {env_path}")
load_dotenv(env_path)

api_key = os.getenv("GEMINI_KEY")
if not api_key:
    raise ValueError("GEMINI_KEY not found in .env file")
print(f"API Key found (first 4 chars): {api_key[:4]}...")

genai.configure(api_key=api_key)

# Configure generation parameters
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

# Initialize the model with the correct name and version
_MODEL = genai.GenerativeModel("gemini-2.5-flash", generation_config=generation_config)

print("Initializing Gemini model...")
try:
    # Test the model with a simple prompt to verify it works
    response = _MODEL.generate_content("Hello")
    print("Model initialized successfully")
except Exception as e:
    print(f"Error initializing model: {str(e)}")
    raise

# Optimized prompt for faster responses
_SCHEMA_PROMPT = """Fighting game analyst. Return ONLY JSON:
{
  "fighter": string,
  "summary": string (2-3 sentences max),
  "counters": [ {"name": string, "reason": string} ] (3 items),
  "victims": [ {"name": string, "reason": string} ] (3 items),
  "notes": string (1 sentence)
}
Be extremely concise. Focus on core strengths/weaknesses only."""

def _parse_json(text: str) -> Dict[str, Any]:
    """Extracts and parses JSON from a response text."""
    try:
        print(f"Attempting to parse text: {text[:200]}...")  # Print first 200 chars to avoid huge logs
        # Extract JSON block if it exists, otherwise try to parse the whole text
        match = re.search(r'\{.*\}', text.strip(), re.DOTALL)
        if match:
            print("Found JSON block in text")
            json_str = match.group(0)
        else:
            print("No JSON block found, attempting to parse entire text")
            json_str = text.strip()
        result = json.loads(json_str)
        print("Successfully parsed JSON")
        return result
    except Exception as e:
        print(f"Error parsing JSON: {str(e)}")
        raise

# Simple in-memory cache
_analysis_cache = {}

def analyze_fighter(fighter: str, game: Optional[str] = None) -> Dict[str, Any]:
    try:
        # Create cache key
        cache_key = f"{fighter.lower()}:{game.lower() if game else 'none'}"
        
        # Check cache first
        if cache_key in _analysis_cache:
            print(f"Found cached analysis for {fighter}")
            return _analysis_cache[cache_key]
            
        print(f"Analyzing fighter {fighter} from {game}")
        user = f"Character: {fighter}\nGame/Franchise: {game or 'unspecified'}"
        print("Sending request to Gemini...")
        resp = _MODEL.generate_content([_SCHEMA_PROMPT, user])
        print(f"Raw Gemini response: {resp.text}")
        result = _parse_json(resp.text)
        print(f"Parsed response: {result}")
        
        # Cache the result
        _analysis_cache[cache_key] = result
        return result
    except Exception as e:
        print(f"Error in analyze_fighter: {str(e)}")
        raise