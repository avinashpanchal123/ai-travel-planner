"""Trip model used across the AI Travel Planner app."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Trip:
    """Represents a travel planning request and generated itinerary content."""

    destination: str
    days: int
    budget: str
    travel_style: str
    itinerary: str
    created_at: datetime

    @property
    def slug(self) -> str:
        """Return a filename-safe slug for storing this trip."""
        base = self.destination.strip().lower().replace(" ", "-")
        safe = "".join(ch for ch in base if ch.isalnum() or ch == "-").strip("-")
        return safe or "trip"

    def to_text(self) -> str:
        """Render this trip as plain text for local file storage."""
        return (
            f"AI Travel Planner\n"
            f"Generated: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Destination: {self.destination}\n"
            f"Days: {self.days}\n"
            f"Budget: {self.budget}\n"
            f"Travel Style: {self.travel_style}\n"
            f"\n=== AI Itinerary ===\n\n"
            f"{self.itinerary.strip()}\n"
        )
