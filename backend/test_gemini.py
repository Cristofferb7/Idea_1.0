import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(Path(__file__).parent / ".env")
api_key = os.getenv("GEMINI_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
resp = model.generate_content("Say hello from Gemini AI!")
print(resp.text)    