from stt import speech_to_text
from tts import text_to_speech
from text_response import CyberBot

def speech_to_speech(audio_file: str):
    """
    Take input audio, convert to text, then back to speech.
    """
    # Step 1: STT
    result = speech_to_text(audio_file)
    bot = CyberBot()
    response = bot.ask(result)

    # Step 2: TTS
    audio_data = text_to_speech(response)
    return audio_data
