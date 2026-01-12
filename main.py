from fastapi import FastAPI
from fastapi.responses import FileResponse
import edge_tts
import os

app = FastAPI()

@app.get("/speak")
async def speak(text: str, voice: str = "pt-BR-FranciscaNeural"):
    output = "audio.mp3"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output)
    return FileResponse(output, media_type="audio/mpeg")
