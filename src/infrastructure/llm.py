import httpx
import json
from src.domain.interfaces import ISpiellinienGenerator
from src.domain.value_objects import Prompt
from src.infrastructure.config import settings

class LiteLLMGenerator(ISpiellinienGenerator):
    def __init__(self):
        self.model = settings.LLM_MODEL
        self.api_key = settings.LLM_API_KEY
        self.base_url = settings.LLM_BASE_URL.rstrip("/")

    def generate(self, prompt: Prompt) -> str:
        # Falls kein gültiger API-Key konfiguriert ist, Fehlermeldung
        if not self.api_key or self.api_key == "sk-1234":
            raise ValueError("LLM_API_KEY ist nicht konfiguriert. Bitte in .env Datei eintragen.")

        messages = []
        text = prompt.text
        if "SYSTEM:" in text and "ANWEISUNG:" in text:
            parts = text.split("ANWEISUNG:", 1)
            system_part = parts[0].replace("SYSTEM:", "").strip()
            user_part = parts[1].strip()
            
            messages = [
                {"role": "system", "content": system_part},
                {"role": "user", "content": f"ANWEISUNG: {user_part}"}
            ]
        else:
            messages = [
                {"role": "user", "content": text}
            ]

        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model,
                "messages": messages
            }

            # Direkter Call an die OpenAI-kompatible Chat-Completion API von LiteLLM
            with httpx.Client(timeout=60.0) as client:
                response = client.post(
                    f"{self.base_url}/v1/chat/completions",
                    json=payload,
                    headers=headers
                )
                
                if response.status_code != 200:
                    raise RuntimeError(f"API Error ({response.status_code}): {response.text}")
                
                result = response.json()
                return result["choices"][0]["message"]["content"]

        except Exception as e:
            print(f"Connection Error: {e}")
            raise RuntimeError(f"Fehler bei der Kommunikation mit dem LLM: {str(e)}")
