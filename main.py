@app.get("/speak")
async def speak(
    text: str, 
    API_KEY: str = Query(None), 
    api_key: str = Query(None), 
    voice: str = "pt-BR-FranciscaNeural",
    rate: str = "+0%",
    pitch: str = "+0Hz"
):
    # Tenta pegar a chave de qualquer um dos dois parâmetros
    token_recebido = API_KEY or api_key
    
    if token_recebido != SECRET_KEY:
        raise HTTPException(status_code=403, detail="Chave API invalida")
    
    # ... resto do código igual ...
