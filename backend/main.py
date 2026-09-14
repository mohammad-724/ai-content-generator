import os
import urllib.parse
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from openai import OpenAI
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY was not found in the environment or .env file.")

client = OpenAI(api_key=api_key)

app = FastAPI(
    title="AI Content Generation & Publishing Platform",
    version="2.0.0",
    description="A learning-focused Generative AI content creation and publishing simulation platform.",
)


class ContentRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=1000)
    content_type: str = Field(min_length=1, max_length=100)
    tone: str = Field(min_length=1, max_length=100)
    length: str = Field(min_length=1, max_length=100)


class ImageRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=1500)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/status")
def api_status():
    return {
        "status": "online",
        "service": "AI Content Generation & Publishing Platform",
        "version": app.version,
    }


@app.post("/generate-content")
def generate_content(request: ContentRequest):
    prompt = f"""
Create {request.content_type} content about the following topic:

Topic: {request.topic}

Tone: {request.tone}

Length: {request.length}

Requirements:
- Make the content clear and engaging.
- Use appropriate language for the selected content type.
- Keep the response focused on the topic.
- Do not add unnecessary explanations before or after the content.
"""

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt,
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"AI generation failed: {exc}") from exc

    return {
        "topic": request.topic,
        "content_type": request.content_type,
        "tone": request.tone,
        "length": request.length,
        "generated_content": response.output_text,
    }


@app.post("/generate-image")
def generate_image(request: ImageRequest):
    encoded_prompt = urllib.parse.quote(request.prompt, safe="")

    image_url = (
        "https://image.pollinations.ai/prompt/"
        f"{encoded_prompt}"
        "?model=flux"
        "&width=1024"
        "&height=1024"
        "&safe=true"
    )

    return {
        "image": image_url,
        "prompt": request.prompt,
    }


@app.get("/")
def home():
    index_file = FRONTEND_DIR / "index.html"
    if not index_file.exists():
        raise HTTPException(status_code=404, detail="Frontend not found.")
    return FileResponse(index_file)


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port, reload=False)
