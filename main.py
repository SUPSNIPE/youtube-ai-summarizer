import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = API_KEY)
yt_client = YouTubeTranscriptApi()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str

@app.post("/summarize")
async def summarize_video(request: VideoRequest):

    user_url = request.url.strip()
    
    if "v=" in user_url:
        video_id = user_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in user_url:
        video_id = user_url.split("youtu.be/")[1].split("?")[0]
    else:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL format.")
    try:
        transcript_data = yt_client.fetch(video_id)
        full_transcript_string = " ".join([snippet.text for snippet in transcript_data.snippets])
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to fetch transcript.")

    prompt = f"""
    You are an expert tutor. Read the following lecture transcript and create a concise summary and 5 flashcards with questions and answers for studying and return:
    1. A brief 3-sentence summary of the core concepts.
    2. 5 key flashcards (Question and Answer format) to help me study.

    Transcript:
    {full_transcript_string}
    """
    try:
        response = client.models.generate_content(model = 'gemini-2.5-flash', contents = prompt)
        return {"study_guide": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail="AI generation failed.")