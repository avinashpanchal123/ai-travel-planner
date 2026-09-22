"""Service layer for OpenRouter AI communication."""

from __future__ import annotations

import os
from typing import Any

import requests
from dotenv import load_dotenv


class AIServiceError(Exception):
    """Raised when the AI service cannot return a valid response."""


class AIService:
    """Handles OpenRouter API requests for itinerary generation."""

    API_URL = "https://openrouter.ai/api/v1/chat/completions"
    MODEL = "openrouter/free"

    def __init__(self) -> None:
        load_dotenv()
        self.api_key = os.getenv("OPENROUTER_API_KEY", "").strip()

    def generate_completion(self, prompt: str) -> str:
        """Send a prompt to OpenRouter and return the generated text."""
        if not self.api_key:
            raise AIServiceError(
                "Missing OpenRouter API key. Set OPENROUTER_API_KEY in your .env file."
            )

        payload: dict[str, Any] = {
            "model": self.MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful travel planner assistant.",
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.7,
        }

        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json",
        }

        try:
            response = requests.post(
                self.API_URL,
                json=payload,
                headers=headers,
                timeout=45,
            )
            response.raise_for_status()
        except requests.RequestException as exc:
            raise AIServiceError(f"Network/API error while contacting OpenRouter: {exc}") from exc

        try:
            data = response.json()
            content = data["choices"][0]["message"]["content"].strip()
        except (KeyError, IndexError, TypeError, ValueError) as exc:
            raise AIServiceError("Received an unexpected response format from OpenRouter.") from exc

        if not content:
            raise AIServiceError("OpenRouter returned an empty response.")

        return content
