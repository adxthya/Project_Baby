
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import whisper
import time
import tempfile
import os
from dotenv import load_dotenv
import requests

# 🔐 Load Hugging Face API key from .env
load_dotenv()
api_key = os.getenv("TOKEN")

if not api_key:
    raise ValueError("❌ Groq API key not found in .env file.")

# ⚙️ Set temp folder for audio playback
custom_temp = os.path.join(os.getcwd(), "temp_audio")
os.makedirs(custom_temp, exist_ok=True)
tempfile.tempdir = custom_temp

# 🎙️ Record audio
def record_audio(filename="question.wav", duration=8, fs=44100):
    print("🎤 Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print(f"✅ Audio saved as {filename}")

# 🎧 Preprocess audio
def preprocess_audio(input_file="question.wav", output_file="question_fixed.wav"):
    print("🎧 Preprocessing audio...")
    sound = AudioSegment.from_file(input_file)
    sound = sound.set_channels(1).set_frame_rate(16000).set_sample_width(2)
    sound.export(output_file, format="wav")
    print(f"✅ Processed and saved as {output_file}")
    return output_file

# 🧠 Transcribe with Whisper
def transcribe_audio(filename="question_fixed.wav"):
    print("🧠 Transcribing...")
    model = whisper.load_model("base")
    result = model.transcribe(filename, language="en")
    print("📘 Detected language:", result.get("language", "unknown"))

    text = result["text"].strip()
    if not text:
        print("⚠️ No speech detected.")
        return "[No valid input]"

    print("📝 Transcription:", text)
    with open("transcribed.txt", "w", encoding="utf-8") as f:
        f.write(text)
    return text

def generate_reply(text):
    print("🗣️ Generating reply from Groq...")

    try:
        prompt = f"[INST] You are a helpful AI assistant for baby healthcare. The user said: '{text}'. What is your response? [/INST]"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": "llama-3.3-70b-versatile",  # or llama3-70b-8192 / llama3-8b-8192
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data
        )

        reply = response.json()["choices"][0]["message"]["content"]

        print("🤖 Groq Reply:", reply)

        # 🎤 Convert to speech
        tts = gTTS(reply)
        tts.save("reply.mp3")
        print("🔊 Playing reply...")
        audio = AudioSegment.from_mp3("reply.mp3")
        play(audio)

    except Exception as e:
        print("❌ Error generating reply:", repr(e))


# ▶️ Run the pipeline
if __name__ == "__main__":
    record_audio()
    time.sleep(1)
    fixed_audio = preprocess_audio()
    question = transcribe_audio(fixed_audio)
    generate_reply(question)
