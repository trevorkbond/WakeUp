# main.py
import pygame
import requests
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import FileResponse

from challenge.challenge_getter import ChallengeGetter
from challenge.scripture_challenge_getter import ScriptureChallengeGetter

ALARM_PATH = "../alarm/alarm.mp3"
# WEBHOOK_URL = ""
# with open("webhook_url.txt", "r") as f:
#     WEBHOOK_URL = f.read().strip()
# requests.post(WEBHOOK_URL)

pygame.mixer.init()
pygame.mixer.music.load(ALARM_PATH)
pygame.mixer.music.play()
app = FastAPI()
challenge_getter: ChallengeGetter = ScriptureChallengeGetter()


@app.post("/start")
async def start_alarm():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(ALARM_PATH)
        pygame.mixer.music.play()
    return {"message": "Started alarm"}

@app.post("/stop")
async def stop_alarm():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    return {"message": "Stopped alarm"}

@app.post("/speech")
async def check_speech(request: Request):
    data = await request.json() 
    text = data.get("text", "")
    print(text)

@app.get("/challenge")
def get_challenge():
    challenge = challenge_getter.get_challenge()
    return {"challenge": challenge}

@app.get("/")
def read_index():
    return FileResponse("index.html")
