# main.py
import pygame
from fastapi import FastAPI

ALARM_PATH = "../alarm/alarm.mp3"

pygame.mixer.init()
app = FastAPI()

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
