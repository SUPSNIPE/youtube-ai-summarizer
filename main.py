import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai

# 1. Setup the clients
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = API_KEY)
yt_client = YouTubeTranscriptApi()

# 2. Initialize the server
app = FastAPI()

# CORS setup to allow requests from any origin (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows local HTML file to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define exact data structure that frontend will send
class VideoRequest(BaseModel):
    url: str

# 3. The Endpoint
@app.post("/summarize")
async def summarize_video(request: VideoRequest):

    user_url = request.url.strip() # Remove any leading/trailing whitespace

    # Url slicing
    if "v=" in user_url:
        # Split the standard URL at "v=" and takes the right side [1].
        # The second .split("&")[0] safely chops off time stamps
        video_id = user_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in user_url:
        # Handles the link obtained from the share button on YouTube
        video_id = user_url.split("youtu.be/")[1].split("?")[0]
    else:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL format.")

    # Get the transcript
    try:
        transcript_data = yt_client.fetch(video_id)
        full_transcript_string = " ".join([snippet.text for snippet in transcript_data.snippets])
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to fetch transcript.")

    # AI prompt
    prompt = f"""
    You are an expert tutor. Read the following lecture transcript and create a concise summary and 5 flashcards with questions and answers for studying and return:
    1. A brief 3-sentence summary of the core concepts.
    2. 5 key flashcards (Question and Answer format) to help me study.

    Transcript:
    {full_transcript_string}
    """

    # Output
    try:
        response = client.models.generate_content(model = 'gemini-2.5-flash', contents = prompt)
        # Send back as a JSON object
        return {"study_guide": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail="AI generation failed.")