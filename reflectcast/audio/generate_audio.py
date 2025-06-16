import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")

def text_to_podcast(script_text, emotion, output_path="outputs/audio"):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": script_text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.7}
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        filename = f"{emotion}_podcast.mp3"
        path = os.path.join(output_path, filename)
        with open(path, "wb") as f:
            f.write(response.content)
        return path
    else:
        raise Exception("Failed to generate audio: " + response.text)
