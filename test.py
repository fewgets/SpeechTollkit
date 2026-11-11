# filename: main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama

app = FastAPI()

# ✅ Enable CORS (allow all origins for testing, later restrict)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # or ["http://localhost:3000"] for React only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# request body schema
class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = ollama.chat(
            model="qwen:4b",  # change to llama3, mistral, etc.
            messages=[{"role": "user", "content": request.prompt}]
        )
        return {"response": response["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"message": "Ollama FastAPI server running 🚀"}
