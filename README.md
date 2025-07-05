
# 🤖 chAild – AI Baby Care Assistant

chAild is an AI-powered multimodal baby care assistant designed to help parents track vaccinations, ask questions about child care, and analyze voice or image inputs for better parenting support.

---

## 🚀 Features

### ✅ Vaccine Tracker
- Register baby's name and date of birth.
- Automatically generates a vaccination schedule based on WHO-recommended timelines.
- View completed and upcoming vaccines with status indicators.
- Upload vaccine card images.
- (Planned) Export schedule as PDF.
- Map view to locate nearby vaccination centers using geolocation.

### 🤔 Q&A Assistant
- Ask any baby-related health or care question.
- Powered by Groq/Large Language Models (LLMs).
- Text-to-text question answering interface.

### 🎤 Voice & 📸 Image Assistant *(Planned / In progress)*
- Upload voice queries via microphone or audio files.
- Upload baby-related images (e.g., rashes, CTG scans) for classification or health guidance.

---

<!-- ## 🛠️ Tech Stack

| Layer         | Tools Used                             |
|---------------|-----------------------------------------|
| Frontend      | `Streamlit`, `HTML/CSS`, `JavaScript`   |
| Backend       | `Flask`, `FastAPI` (optional), `APScheduler`, `TinyDB/SQLite` |
| AI Models     | `scikit-learn`, `transformers`, `BLIP`, `Whisper` |
| Map Services  | `Leaflet.js`, `OpenStreetMap`, `RoutingMachine` |
| Dev Tools     | `Git`, `VS Code`, `Postman`, `Python 3.10+` |

--- -->

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/project_baby.git
cd project_baby
```

### 2. Set up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

### Backend (Flask API)

```bash
cd backend
python main.py
```

### Frontend (Streamlit)

```bash
cd frontend
streamlit run streamlit_app.py
```

---

## 🌐 Live Demo

> To preview map functionality, ensure `vaccine_map.html` is served from `/static/` and location access is enabled in the browser.

---

## 📌 To-Do

- [ ] Integrate calendar reminders
- [ ] Enable voice transcription with Whisper
- [ ] Add baby image health classification
- [ ] Save full vaccine status per child in DB


---

## 🙋‍♀️ Made By

**Team chAild**
