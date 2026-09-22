"""AI Travel Planner terminal application entry point."""

from __future__ import annotations

from pathlib import Path

from planners.travel_planner import TravelPlanner
from services.ai_service import AIService, AIServiceError
from storage.file_storage import FileStorage

BUDGET_OPTIONS = {"low", "medium", "high"}
STYLE_OPTIONS = {"adventure", "luxury", "family", "backpacking"}


def _prompt_non_empty(message: str) -> str:
    """Prompt until user provides a non-empty value."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def _prompt_days() -> int:
    """Prompt for a valid number of travel days."""
    while True:
        raw = input("Number of days: ").strip()
        if not raw.isdigit():
            print("Please enter a positive whole number.")
            continue
        days = int(raw)
        if days <= 0:
            print("Number of days must be greater than 0.")
            continue
        return days


def _prompt_choice(message: str, allowed_values: set[str]) -> str:
    """Prompt user for a value from allowed options."""
    while True:
        value = input(message).strip().lower()
        if value in allowed_values:
            return value.capitalize()
        print(f"Invalid choice. Allowed options: {', '.join(sorted(allowed_values))}")


def create_trip_plan(planner: TravelPlanner, storage: FileStorage) -> None:
    """Collect user input, generate an itinerary, and save it."""
    print("\n=== Create Trip Plan ===")
    destination = _prompt_non_empty("Destination: ")
    days = _prompt_days()
    budget = _prompt_choice("Budget (Low/Medium/High): ", BUDGET_OPTIONS)
    travel_style = _prompt_choice(
        "Travel style (Adventure/Luxury/Family/Backpacking): ", STYLE_OPTIONS
    )

    try:
        # AI call can fail due to key/network/API issues, so handle gracefully.
        trip = planner.create_trip_plan(destination, days, budget, travel_style)
        saved_path = storage.save_trip(trip)
    except AIServiceError as exc:
        print(f"\nCould not generate trip plan: {exc}")
        return

    print("\n=== Generated Itinerary ===\n")
    print(trip.itinerary)
    print(f"\nTrip saved to: {saved_path}")


def view_saved_trips(storage: FileStorage) -> None:
    """Display available saved trips and optionally show one."""
    files = storage.list_trip_files()
    if not files:
        print("\nNo saved trips found.")
        return

    print("\n=== Saved Trips ===")
    for index, file_path in enumerate(files, start=1):
        print(f"{index}. {file_path.name}")

    choice = input("\nEnter trip number to view (or press Enter to return): ").strip()
    if not choice:
        return
    if not choice.isdigit() or not (1 <= int(choice) <= len(files)):
        print("Invalid selection.")
        return

    selected = files[int(choice) - 1]
    print("\n" + storage.read_trip(selected.name))


def delete_saved_trip(storage: FileStorage) -> None:
    """Delete a selected saved trip file."""
    files = storage.list_trip_files()
    if not files:
        print("\nNo saved trips to delete.")
        return

    print("\n=== Delete Saved Trip ===")
    for index, file_path in enumerate(files, start=1):
        print(f"{index}. {file_path.name}")

    choice = input("\nEnter trip number to delete (or press Enter to cancel): ").strip()
    if not choice:
        return
    if not choice.isdigit() or not (1 <= int(choice) <= len(files)):
        print("Invalid selection.")
        return

    selected = files[int(choice) - 1]
    if storage.delete_trip(selected.name):
        print(f"Deleted: {selected.name}")
    else:
        print("Could not delete file.")


def main() -> None:
    """Run the menu-driven terminal app."""
    storage = FileStorage(Path("trips"))
    planner = TravelPlanner(AIService())

    while True:
        print(
            "\n=== AI Travel Planner ===\n"
            "1. Create Trip Plan\n"
            "2. View Saved Trips\n"
            "3. Delete Saved Trip\n"
            "4. Exit"
        )
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            create_trip_plan(planner, storage)
        elif choice == "2":
            view_saved_trips(storage)
        elif choice == "3":
            delete_saved_trip(storage)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
