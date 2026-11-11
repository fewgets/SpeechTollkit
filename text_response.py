import os

from google import genai

class CyberBot:
    def __init__(self, api_key: str | None = None, model: str = "gemini-2.5-flash"):
        """
        Initialize CyberBot with Gemini API key and model.
        """
        api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("Set the GEMINI_API_KEY environment variable.")
        self.client = genai.Client(api_key=api_key)
        self.model = model
        # conversation history (optional, future context)
        self.messages = [
            {"role": "system", "content": "You are a cybersecurity assistant. Answer clearly and concisely."}
        ]

    def ask(self, text: str) -> str:
        """
        Send input text to Gemini API and return the response.
        """
        self.messages.append({"role": "user", "content": text})

        # Gemini API request
        response = self.client.models.generate_content(
            model=self.model,
            contents=text
        )

        answer = response.text
        self.messages.append({"role": "assistant", "content": answer})
        return answer

