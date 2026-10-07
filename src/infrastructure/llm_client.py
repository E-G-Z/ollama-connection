import requests
import json
from src.config.settings import settings

class LLMClient:
    def __init__(self):
        self.base_url = settings.OLLAMA_URL
        self.model = settings.OLLAMA_MODEL

    def generate(self, prompt:str):
        response = requests.post(
            self.base_url, 
            json={
                "model": self.model,
                "prompt": prompt, 
                "stream": False
            }
        )
        data = response.json()
        text = data.get("response", "")

        try:
            json.loads(text)
        except:
            return {"response": text}
