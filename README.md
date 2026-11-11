<!-- Speech Toolkit · README by Usama Shahid (fewgets) -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,55:0F3D3E,100:36FFC7&height=230&section=header&text=Speech%20Toolkit&fontSize=60&fontColor=FFFFFF&fontAlignY=36&desc=Voice%20AI%20API%3A%20speech%20to%20text%2C%20text%20to%20speech%2C%20speech%20to%20speech&descSize=17&descAlignY=58&animation=fadeIn" width="100%" alt="Speech Toolkit"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=700&color=36FFC7&center=true&vCenter=true&width=720&height=60&lines=Whisper+Speech-to-Text;Gemini-Powered+Answers;Talk+to+an+AI%2C+Hear+It+Reply" alt="Typing SVG"/>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Whisper-412991?style=for-the-badge&logo=openai&logoColor=white" alt="Whisper"/>
  <img src="https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" alt="Gemini"/>
  <img src="https://img.shields.io/badge/gTTS-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="gTTS"/>
</p>

</div>

---
## 📌 Overview

**Speech Toolkit** is a small, clean **voice-AI backend** built with **FastAPI**. It gives any app
four ready-made endpoints to **listen, think and talk**:

| | Capability | Powered by |
|:-:|---|---|
| 🎙️ | **Speech → Text** | OpenAI **Whisper** (runs locally, no API cost) |
| 🔊 | **Text → Speech** | Google **gTTS** |
| 💬 | **Text → AI answer** | Google **Gemini 2.5 Flash** ("CyberBot", a cybersecurity assistant) |
| 🔁 | **Speech → Speech** | Whisper → Gemini → gTTS: ask a question out loud and hear the answer |

Plug it into a website, chatbot or mobile app to add a voice assistant in minutes.

---

## 🔁 Speech-to-Speech Pipeline

```mermaid
flowchart LR
    MIC[🎙️ Your voice<br/>audio file] --> STT[📝 Whisper<br/>speech → text]
    STT --> LLM[🧠 Gemini<br/>CyberBot answer]
    LLM --> TTS[🔊 gTTS<br/>text → speech]
    TTS --> OUT[🎧 MP3 reply]
```

---

## 🔌 API Endpoints

| Method | Endpoint | Input | Output |
|---|---|---|---|
| `GET` | `/` | | Welcome message |
| `POST` | `/stt` | `file`: audio (WAV, MP3…) | `{ "text": "..." }` |
| `POST` | `/tts` | `text`: form field | MP3 audio stream |
| `POST` | `/text_response` | `text`: form field | `{ "response": "..." }` |
| `POST` | `/sts` | `file`: audio question | MP3 audio answer |

Interactive docs: **http://127.0.0.1:8000/docs**

---

## 🚀 Run Locally

```bash
git clone https://github.com/fewgets/SpeechTollkit.git
cd SpeechTollkit

python -m venv .venv
.venv\Scripts\activate          # macOS / Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Set your Gemini API key ([get one free](https://aistudio.google.com/)):

```bash
# Windows (PowerShell)
$env:GEMINI_API_KEY="your-key"
# macOS / Linux
export GEMINI_API_KEY="your-key"
```

Start the server:

```bash
uvicorn api:app --reload
```

### 🧪 Try it

```bash
# Speech → Text (a sample file is included)
curl -X POST -F "file=@harvard.wav" http://127.0.0.1:8000/stt

# Text → Speech
curl -X POST -F "text=Hello from Speech Toolkit" http://127.0.0.1:8000/tts --output hello.mp3

# Ask the AI by voice and get a spoken answer
curl -X POST -F "file=@harvard.wav" http://127.0.0.1:8000/sts --output answer.mp3
```

---

## 📁 Project Structure

```text
SpeechToolkit/
├── api.py              # FastAPI app and endpoints
├── stt.py              # Whisper speech-to-text (CPU, 16 kHz mono)
├── tts.py              # gTTS text-to-speech (in-memory MP3)
├── text_response.py    # CyberBot: Gemini chat wrapper
├── sts.py              # Full voice pipeline
├── test.py             # Bonus: local LLM chat server via Ollama
├── harvard.wav         # Sample audio for testing
└── requirements.txt
```

---

## 🧰 Tech Stack

| Component | Technology |
|---|---|
| API | FastAPI, Uvicorn |
| Speech-to-Text | OpenAI Whisper (`base` model), SoundFile, Librosa, PyTorch |
| LLM | Google Gemini 2.5 Flash (`google-genai`) |
| Text-to-Speech | gTTS |
| Local LLM (optional) | Ollama |

## 🔭 Roadmap

- [ ] Streaming responses for lower latency
- [ ] Urdu and multilingual voices
- [ ] Conversation memory across turns
- [ ] Swap gTTS for a neural TTS voice

---

## 🤝 Let's Work Together

<div align="center">

**Have an idea, a freelance project, or want to collaborate on something in AI?**
I'm always open to collaborations, freelance work and full-time opportunities.

<a href="mailto:shaikhusama541@gmail.com?subject=Collaboration%20-%20Speech%20Toolkit">
  <img src="https://img.shields.io/badge/Email-shaikhusama541%40gmail.com-36FFC7?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0D1117" alt="Email"/>
</a>
<a href="https://www.linkedin.com/in/-usamashahid/">
  <img src="https://img.shields.io/badge/LinkedIn-Usama%20Shahid-36FFC7?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0D1117" alt="LinkedIn"/>
</a>
<a href="https://github.com/fewgets">
  <img src="https://img.shields.io/badge/GitHub-fewgets-36FFC7?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117" alt="GitHub"/>
</a>

<br/><br/>

⭐ **If you like this project, please give it a star. It really helps!** ⭐

<br/>

<h3>"The most natural interface is your own voice."</h3>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:36FFC7,55:0F3D3E,100:0D1117&height=150&section=footer&animation=twinkling" width="100%" alt="footer"/>

</div>
