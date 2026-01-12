from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
import edge_tts
import os

app = FastAPI()
SECRET_KEY = os.getenv("API_KEY")

@app.get("/speak")
async def speak(
    text: str, 
    api_key: str = Query(None), 
    voice: str = "pt-BR-FranciscaNeural",
    rate: str = "+0%",
    pitch: str = "+0Hz"
):
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Chave API invalida")
        
    output = "audio.mp3"
    # Agora passamos voice, rate e pitch para o motor do Edge
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(output)
    return FileResponse(output, media_type="audio/mpeg")
