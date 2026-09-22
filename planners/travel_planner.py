"""Orchestration logic for building AI travel plans."""

from datetime import datetime

from models.trip import Trip
from services.ai_service import AIService


class TravelPlanner:
    """Creates detailed trip plans by prompting the AI service."""

    def __init__(self, ai_service: AIService) -> None:
        self.ai_service = ai_service

    def create_trip_plan(
        self,
        destination: str,
        days: int,
        budget: str,
        travel_style: str,
    ) -> Trip:
        """Generate itinerary text and wrap it in a Trip object."""
        prompt = self._build_prompt(destination, days, budget, travel_style)
        itinerary = self.ai_service.generate_completion(prompt)
        return Trip(
            destination=destination,
            days=days,
            budget=budget,
            travel_style=travel_style,
            itinerary=itinerary,
            created_at=datetime.now(),
        )

    @staticmethod
    def _build_prompt(destination: str, days: int, budget: str, travel_style: str) -> str:
        """Build a structured prompt so output is consistent and beginner-friendly."""
        return (
            "Create a complete travel plan using simple, clear language.\n"
            f"Destination: {destination}\n"
            f"Number of days: {days}\n"
            f"Budget level: {budget}\n"
            f"Travel style: {travel_style}\n\n"
            "Include all sections below with headings:\n"
            "1) Day-wise itinerary\n"
            "2) Top attractions\n"
            "3) Food recommendations\n"
            "4) Packing checklist\n"
            "5) Budget-saving tips\n"
            "6) Local transportation suggestions\n"
            "7) Best time to visit\n"
            "Use bullet points where helpful."
        )
