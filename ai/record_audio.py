# record_audio.py

import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(filename="question.wav", duration=8, fs=44100):
    # 🔁 Remove existing file if present
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f"🧹 Old '{filename}' removed.")
        except Exception as e:
            print(f"⚠️ Error deleting old file: {e}")

    print("🎤 Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print(f"✅ New audio saved as '{filename}'")

