# record_audio.py
import sounddevice as sd
from scipy.io.wavfile import write

duration = 35  # seconds
fs = 44100  # sample rate
filename = "question.wav"

print("🎤 Recording...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished

write(filename, fs, recording)
print(f"✅ Saved: {filename}")
