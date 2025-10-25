
# Standard library imports
import os  # For environment variable access
from pathlib import Path  # For file path operations

# Third-party imports
from dotenv import load_dotenv  # For loading environment variables from .env file
import google.generativeai as genai  # Gemini API client

# Load environment variables from backend/.env
load_dotenv(Path(__file__).parent / ".env")  # Ensures GEMINI_KEY is available

# Get Gemini API key from environment
api_key = os.getenv("GEMINI_KEY")  # Reads GEMINI_KEY from .env

# Configure Gemini API client with the key
genai.configure(api_key=api_key)

# Create a Gemini model instance for 'gemini-2.5-flash'
model = genai.GenerativeModel("gemini-2.5-flash")

# Send a prompt to Gemini and get the response
resp = model.generate_content("Say hello from Gemini AI!")

# Print the AI's response to the console
print(resp.text)