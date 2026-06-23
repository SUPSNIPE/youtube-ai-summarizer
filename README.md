🧠 Smart Study Extractor

A full-stack web application that automatically extracts YouTube lecture transcripts and uses AI to generate concise study guides and flashcards. Built to help students quickly digest dense educational content.

🚀 Features

Automated Extraction: Bypasses manual transcription by scraping YouTube's hidden closed-caption data.

Smart URL Parsing: Safely handles both standard YouTube links and shortened mobile share links while stripping timestamps.

AI-Powered Analysis: Leverages Google's Gemini AI to digest massive text blocks and return structured, educational outputs.

Full-Stack Architecture: A responsive HTML/JS frontend communicating asynchronously with a Python FastAPI backend.

🛠️ Technologies & AI Stack

Frontend: HTML5, CSS3, Vanilla JavaScript, Fetch API

Backend: Python 3, FastAPI, Uvicorn (ASGI server)

Data Scraping: youtube-transcript-api (Object-Oriented .fetch() implementation)

AI Integration: * SDK: The modern google-genai Python library.

Model: gemini-2.5-flash (Google's latest, fastest model optimized for high-volume text processing).

Security: python-dotenv for API key management, CORS Middleware for secure cross-origin requests.

💻 Local Setup Instructions

Clone the repository:

git clone [https://github.com/yourusername/youtube-ai-summarizer.git](https://github.com/yourusername/youtube-ai-summarizer.git)
cd youtube-ai-summarizer


Create and activate a virtual environment:

# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install fastapi uvicorn pydantic python-dotenv youtube-transcript-api google-genai


Environment Variables:
Create a .env file in the root directory and add your Google Gemini API key:

GEMINI_API_KEY=your_actual_api_key_here


Run the Backend Server:

uvicorn main:app --reload


Launch the Frontend:
Open index.html in your preferred web browser, paste a YouTube link, and click "Extract Study Guide"!
