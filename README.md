# ✨ Cognify AI – Generative AI Learning Assistant

An AI-powered learning assistant built with **FastAPI, Python, and Google Gemini** that helps students understand concepts, answer questions, generate quizzes, summarize study material, and create personalized learning paths.

## 📌 About the Project

Cognify AI is a web-based educational application designed to make learning easier, faster, and more interactive. It uses generative AI to provide clear explanations and learning support based on user input.

The application offers five learning tools through a simple, user-friendly web interface.

## 🚀 Features

### 1. 💬 Question Answering
- Get answers to questions on different subjects.
- Understand difficult topics through clear explanations.
- Explore concepts with helpful examples.

### 2. 📚 Concept Explanation
- Learn complex concepts in simple language.
- Understand how concepts work through examples.
- Get beginner-friendly explanations.

### 3. 📝 Quiz Generation
- Generate multiple-choice questions on a selected topic.
- Receive four answer options for each question.
- Review the answer key to test your knowledge.

### 4. 📄 Text Summarization
- Summarize long study materials into concise key points.
- Identify the most important information.
- Make revision easier and more efficient.

### 5. 🗺️ Learning Path
- Generate step-by-step learning roadmaps.
- Organize subjects into topics and milestones.
- Get practice exercises and project suggestions.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web application framework |
| Google Gemini API | AI-powered response generation |
| HTML5 | Web page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Frontend interactions |
| Jinja2 | Dynamic HTML templates |
| Uvicorn | ASGI server |
| python-dotenv | Environment variable management |

## 📂 Project Structure

```text
Cognify_AI_Project/
│
├── main.py
├── test_gemini.py
├── .env
├── .gitignore
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    ├── style.css
    └── script.js
```

## ⚙️ Installation and Setup

### Prerequisites

Install the following before running the project:

- Python 3.10 or a compatible version supported by the dependencies
- Git
- A Google Gemini API key

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Cognify-AI.git
cd Cognify-AI
```

Replace `YOUR_USERNAME` with your GitHub username.

### Step 2: Create a Virtual Environment

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure the API Key

Create a `.env` file in the project root directory:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your own API key.

**Security:** Never upload your `.env` file or expose your API key in public repositories.

### Step 5: Run the Application

```bash
python -m uvicorn main:app --reload
```

### Step 6: Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8000
```

## 🧪 How to Use

1. Open the Cognify AI dashboard.
2. Select one of the five learning tools.
3. Enter a question, concept, topic, or text.
4. Click **Generate response**.
5. View the AI-generated result.
6. Return to the dashboard to try another tool.

## 🎯 Project Objectives

- Make AI-assisted learning accessible through a web application.
- Simplify complex educational concepts.
- Support interactive self-assessment through quizzes.
- Reduce study time through text summarization.
- Help learners organize their studies using personalized roadmaps.
- Demonstrate the integration of generative AI with a Python web framework.

## 🔮 Future Enhancements

- User registration and login.
- Save and review previous AI-generated responses.
- Download summaries and learning plans.
- Interactive quizzes with score tracking.
- Personalized recommendations based on learning progress.
- Additional AI models and language support.
- Deployment to a public hosting platform.

## 🔐 Security Notes

- Store API keys in environment variables.
- Keep `.env` out of version control.
- Do not commit passwords, tokens, or other secrets.
- Use environment variables for production configuration.

