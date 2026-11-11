from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse
from stt import speech_to_text
from tts import text_to_speech
from sts import speech_to_speech
from text_response import CyberBot
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI(title="CyberBot Voice API", version="1.0")

# Initialize CyberBot (you can replace api_key if needed)
bot = CyberBot()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to CyberBot Voice API. Use /stt, /tts, /sts, or /text_response endpoints."}

# -----------------------------
# Endpoint 1: Speech-to-Text
# -----------------------------
@app.post("/stt")
async def stt_endpoint(file: UploadFile = File(...)):
    """
    Convert uploaded audio file to text.
    """
    try:
        contents = await file.read()
        audio_fp = f"temp_{file.filename}"
        with open(audio_fp, "wb") as f:
            f.write(contents)

        text = speech_to_text(audio_fp)
        return {"text": text}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# -----------------------------
# Endpoint 2: Text-to-Speech
# -----------------------------
@app.post("/tts")
async def tts_endpoint(text: str = Form(...)):
    """
    Convert text to speech (MP3).
    """
    try:
        audio_data = text_to_speech(text)
        audio_data.seek(0)
        return StreamingResponse(audio_data, media_type="audio/mpeg", headers={
            "Content-Disposition": "inline; filename=response.mp3"
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# -----------------------------
# Endpoint 3: Speech-to-Speech
# -----------------------------
@app.post("/sts")
async def sts_endpoint(file: UploadFile = File(...)):
    """
    Full pipeline: audio → text → CyberBot → audio response.
    """
    try:
        contents = await file.read()
        audio_fp = f"temp_{file.filename}"
        with open(audio_fp, "wb") as f:
            f.write(contents)

        audio_data = speech_to_speech(audio_fp)
        return StreamingResponse(audio_data, media_type="audio/mpeg", headers={
            "Content-Disposition": "inline; filename=response.mp3"
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# -----------------------------
# Endpoint 4: Text Response (Chat)
# -----------------------------
@app.post("/text_response")
async def text_response_endpoint(text: str = Form(...)):
    """
    Send text to CyberBot and get text response.
    """
    try:
        response = bot.ask(text)
        return {"response": response}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
