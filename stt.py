import whisper
import soundfile as sf
import numpy as np

# model load karo (CPU par)
model = whisper.load_model("base", device="cpu")


def speech_to_text(audio_file: str) -> str:
    # ffmpeg ke bina audio load
    audio, sr = sf.read(audio_file)

    # agar stereo hai to mono banado
    if len(audio.shape) > 1:
        audio = np.mean(audio, axis=1)

    # whisper ko 16kHz chahiye
    if sr != 16000:
        import librosa
        audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)
        sr = 16000

    # numpy ko torch tensor me convert
    import torch
    audio_tensor = torch.tensor(audio, dtype=torch.float32)

    # transcription
    result = model.transcribe(audio_tensor)
    return result["text"]
