from fastapi import APIRouter, UploadFile, File
import requests
from core.config import HUGGINGFACE_API_KEY

router = APIRouter()

@router.post("/speech")
async def transcribe(file: UploadFile = File(...)):
    audio = await file.read()

    response = requests.post(
        "https://api-inference.huggingface.co/models/openai/whisper-base",
        headers={"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"},
        data=audio
    )

    return response.json()