import os
os.environ["SDL_AUDIODRIVER"] = "alsa"
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
import requests
import threading
import time
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import FileResponse
from challenge.challenge_getter import ChallengeGetter
from challenge.scripture_challenge_getter import ScriptureChallengeGetter

ALARM_PATH = "../alarm/alarm.mp3"
WEBHOOK_URL = ""
with open("webhook_url.txt", "r") as f:
    WEBHOOK_URL = f.read().strip()

requests.post(WEBHOOK_URL)

app = FastAPI()

challenge_getter: ChallengeGetter = ScriptureChallengeGetter()
alarm_thread = None
alarm_cancel_event = threading.Event()
audio_lock = threading.Lock()

def start_alarm():
    with audio_lock:
        for attempt in range(30):
            try:
                if not pygame.mixer.get_init():
                    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)
                
                pygame.mixer.music.load(ALARM_PATH)
                pygame.mixer.music.play(-1)
                print(f"Alarm started successfully on attempt {attempt + 1}")
                return
            except Exception as e:
                print(f"Alarm start failed (attempt {attempt + 1}): {e}")
                if pygame.mixer.get_init():
                    pygame.mixer.quit()
                time.sleep(5)
        
        print("CRITICAL: Failed to start alarm after all retries!")

def stop_alarm():
    with audio_lock:
        pygame.mixer.music.stop()

def schedule_alarm(delay):
    global alarm_thread
    if alarm_thread and alarm_thread.is_alive():
        alarm_cancel_event.set()
        alarm_thread.join()
    
    alarm_cancel_event.clear()
    
    def alarm_worker():
        remaining = delay
        while remaining > 0:
            if alarm_cancel_event.is_set():
                return
            time.sleep(0.1)
            remaining -= 0.1
        start_alarm()
    
    alarm_thread = threading.Thread(target=alarm_worker, daemon=True)
    alarm_thread.start()

@app.post("/snooze")
async def snooze_alarm():
    schedule_alarm(5 * 60)
    stop_alarm()
    return {"message": "Snoozed alarm for 5 minutes"}

@app.post("/stop")
async def stop():
    alarm_cancel_event.set()
    stop_alarm()
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

time.sleep(10)
start_alarm()
