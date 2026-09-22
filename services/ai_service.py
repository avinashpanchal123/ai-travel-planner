import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


class AIService:

    def ask(self, prompt):

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization":
                f"Bearer {API_KEY}",
                "Content-Type":
                "application/json"
            },
            json={
                "model":
                "openrouter/free",

                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        data = response.json()

        return (
            data["choices"][0]
            ["message"]
            ["content"]
        )