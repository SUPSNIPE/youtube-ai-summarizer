# 🧠 Smart Study Extractor

A full-stack web application that automatically extracts YouTube lecture transcripts and uses AI to generate concise study guides and flashcards. Built to help students quickly digest dense educational content.

## 🚀 Features

* **Automated Extraction:** Bypasses manual transcription by scraping YouTube's hidden closed-caption data.
* **Smart URL Parsing:** Safely handles both standard YouTube links and shortened mobile share links while stripping timestamps.
* **AI-Powered Analysis:** Leverages Google's Gemini AI to digest massive text blocks and return structured, educational outputs.
* **Full-Stack Architecture:** A responsive HTML/JS frontend communicating asynchronously with a Python FastAPI backend.

## 🛠️ Technologies & AI Stack

* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Fetch API
* **Backend:** Python 3, FastAPI, Uvicorn (ASGI server)
* **Data Scraping:** `youtube-transcript-api` (Object-Oriented `.fetch()` implementation)
* **AI Integration:** * **SDK:** The modern `google-genai` Python library.
  * **Model:** `gemini-2.5-flash` (Google's latest, fastest model optimized for high-volume text processing).
* **Security:** `python-dotenv` for API key management, CORS Middleware for secure cross-origin requests.

## 💻 Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/youtube-ai-summarizer.git](https://github.com/yourusername/youtube-ai-summarizer.git)
   cd youtube-ai-summarizer
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn pydantic python-dotenv youtube-transcript-api google-genai
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add your Google Gemini API key:
   ```text
   GEMINI_API_KEY=your_actual_api_key_here
   ```

5. **Run the Backend Server:**
   ```bash
   uvicorn main:app --reload
   ```

6. **Launch the Frontend:**
   Open `index.html` in your preferred web browser, paste a YouTube link, and click "Extract Study Guide"!

---

## 📝 Resume Entry

**Smart Study Extractor (Full-Stack AI Web App)**

* **Developed a full-stack web application** using Python and FastAPI to dynamically generate educational study guides and flashcards from YouTube lecture URLs.
* **Engineered a robust backend data pipeline** utilizing the `youtube-transcript-api` to scrape closed captions and parse string data into contiguous text blocks for Large Language Model processing.
* **Integrated the modern `google-genai` SDK (Gemini 2.5 Flash)** to analyze dense lecture transcripts, enforcing strict prompt constraints to return structured JSON/text outputs.
* **Built a responsive, asynchronous frontend** using vanilla JavaScript and the Fetch API, implementing CORS middleware on the server to securely handle cross-origin HTTP requests.
* **Managed project environments and security** by utilizing Python virtual environments (`venv`) for strict dependency versioning and `.env` files to protect sensitive API credentials from version control.
