
import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from google import genai

# --------------------------------------------------
# 1. PROJECT CONFIGURATION
# --------------------------------------------------

ROOT = Path(__file__).resolve().parent
TEMPLATES_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"

# Load API key from .env
load_dotenv(ROOT / ".env")
API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

# Initialize Gemini client
client = genai.Client(api_key=API_KEY) if API_KEY else None

# Create FastAPI application
app = FastAPI(title="Cognify AI - Learning Assistant")

# Check required directories
if not TEMPLATES_DIR.is_dir():
    raise RuntimeError(f"Templates folder not found: {TEMPLATES_DIR}")

if not STATIC_DIR.is_dir():
    raise RuntimeError(f"Static folder not found: {STATIC_DIR}")

# Configure static files and templates
app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static",
)

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


# --------------------------------------------------
# 2. GEMINI AI RESPONSE GENERATION
# --------------------------------------------------

def generate_answer(prompt: str) -> str:
    """Generate a response using the Gemini AI model."""

    if client is None:
        return (
            "Gemini API key is missing. Please add "
            "GEMINI_API_KEY=your_api_key to your .env file "
            "and restart the server."
        )

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt,
        )

        answer = response.text

        if answer and answer.strip():
            return answer.strip()

        return (
            "The AI did not generate a response. "
            "Please try again with a different prompt."
        )

    except Exception as exc:
        print(f"Gemini API error: {exc}")

        return (
            "Sorry, Cognify AI could not generate a response. "
            "Please check your API key, internet connection, "
            "and Gemini model availability, then try again."
        )


# --------------------------------------------------
# 3. HOME PAGE
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Display the Cognify AI dashboard."""

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": None,
            "feature": None,
            "prompt": "",
        },
    )


# --------------------------------------------------
# 4. PROCESS SELECTED LEARNING TOOL
# --------------------------------------------------

@app.post("/ask", response_class=HTMLResponse)
async def ask(
    request: Request,
    feature: str = Form(...),
    prompt: str = Form(...),
):
    """Process user input and display results on a separate page."""

    prompt = prompt.strip()

    # Different instructions for each learning tool
    tasks = {
        "Question Answering": (
            "You are Cognify AI, an educational question-answering "
            "assistant. Answer the user's question directly and "
            "accurately. Start with the answer, then explain it "
            "in simple language. Include an example when useful. "
            "Do not automatically create a quiz or learning roadmap.\n\n"
            f"User question:\n{prompt}"
        ),

        "Concept Explanation": (
            "You are Cognify AI, a patient teacher explaining concepts "
            "to beginners. Explain the requested concept using these "
            "sections:\n"
            "1. Simple definition\n"
            "2. How it works\n"
            "3. Real-life example\n"
            "4. Why it is useful\n"
            "5. Short takeaway\n\n"
            "Use easy language and explain technical terms.\n\n"
            f"Concept to explain:\n{prompt}"
        ),

        "Quiz Generation": (
            "You are Cognify AI, a quiz creator. Generate exactly "
            "5 multiple-choice questions about the requested topic. "
            "Number every question and provide four options labeled "
            "A, B, C, and D. After all questions, provide a separate "
            "answer key with the correct option and a brief explanation. "
            "Do not start with a long lesson about the topic.\n\n"
            f"Quiz topic:\n{prompt}"
        ),

        "Text Summarization": (
            "You are Cognify AI, a text summarization assistant. "
            "Summarize only the text supplied by the user. Begin with "
            "a one-sentence overview, followed by 4 to 7 concise "
            "bullet points covering the main ideas. Preserve important "
            "facts, names, and figures. Do not invent details or turn "
            "the response into a quiz or learning plan.\n\n"
            f"Text to summarize:\n{prompt}"
        ),

        "Learning Path": (
            "You are Cognify AI, a learning-roadmap designer. Create "
            "a practical, beginner-friendly learning path for the "
            "requested subject. Include:\n"
            "1. Learning goal\n"
            "2. Prerequisites\n"
            "3. Week-by-week study schedule\n"
            "4. Topics to learn in order\n"
            "5. Hands-on practice tasks\n"
            "6. A mini-project and a final project\n"
            "7. Recommended ways to measure progress\n\n"
            "Adapt the plan to the subject and its difficulty. "
            "Make the steps achievable and specific.\n\n"
            f"Subject to learn:\n{prompt}"
        ),
    }

    # Validate user input and selected feature
    if not prompt:
        result = "Please enter a topic, question, or text."
        feature = feature if feature in tasks else "Question Answering"

    elif feature not in tasks:
        feature = "Question Answering"
        result = "Invalid learning tool selected. Please return to the dashboard."

    else:
        # Generate the response using the selected tool's instructions
        result = generate_answer(tasks[feature])

    # Display the result on a separate HTML page
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "result": result,
            "feature": feature,
            "prompt": prompt,
        },
    )


# --------------------------------------------------
# 5. HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
async def health():
    """Check whether the application is running."""

    return {
        "status": "running",
        "application": "Cognify AI",
        "gemini_configured": client is not None,
    }
