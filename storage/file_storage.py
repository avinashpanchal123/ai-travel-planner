"""File storage utilities for persisting generated trips."""

from __future__ import annotations

from pathlib import Path

from models.trip import Trip


class FileStorage:
    """Handles saving, listing, reading, and deleting trip plan files."""

    def __init__(self, base_dir: Path | None = None) -> None:
        self.base_dir = base_dir or Path("trips")
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save_trip(self, trip: Trip) -> Path:
        """Save a trip to a timestamped text file and return file path."""
        timestamp = trip.created_at.strftime("%Y%m%d_%H%M%S")
        filename = f"{trip.slug}_{timestamp}.txt"
        path = self.base_dir / filename
        path.write_text(trip.to_text(), encoding="utf-8")
        return path

    def list_trip_files(self) -> list[Path]:
        """Return all saved trip text files sorted by newest first."""
        return sorted(self.base_dir.glob("*.txt"), key=lambda p: p.stat().st_mtime, reverse=True)

    def read_trip(self, filename: str) -> str:
        """Read a saved trip file by filename."""
        path = self.base_dir / filename
        return path.read_text(encoding="utf-8")

    def delete_trip(self, filename: str) -> bool:
        """Delete a saved trip file by filename if it exists."""
        path = self.base_dir / filename
        if not path.exists() or not path.is_file():
            return False
        path.unlink()
        return True
