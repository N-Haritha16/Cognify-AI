
import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

api_key = os.getenv("GEMINI_API_KEY", "").strip()

if not api_key:
    print("ERROR: API key not found in .env")
    raise SystemExit(1)

try:
    client = genai.Client(api_key=api_key)

    print("Testing Gemini model...\n")

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents="Create a beginner-friendly three-step Python learning path."
    )

    print("API TEST SUCCESSFUL")
    print(response.text or "The API returned an empty response.")

except Exception as exc:
    print("API TEST FAILED")
    print("Error type:", type(exc).__name__)
    print("Error details:", str(exc))
