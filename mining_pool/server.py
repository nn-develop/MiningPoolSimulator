from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Načteme .env soubor
load_dotenv()

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/connect")
async def connect():
    return {"message": "Spojení navázáno!"}

@app.get("/connect")
async def connect():
    return {"message": "Spojení navázáno!"}
