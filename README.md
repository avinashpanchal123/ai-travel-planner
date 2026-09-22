# AI Travel Planner

AI Travel Planner is a beginner-friendly Python terminal application that uses the OpenRouter free AI API to generate complete trip plans.

## Features

- Collects user inputs: destination, trip length, budget, and travel style
- Generates:
  - Day-wise itinerary
  - Top attractions
  - Food recommendations
  - Packing checklist
  - Budget-saving tips
  - Local transportation suggestions
  - Best time to visit
- Saves generated trips as text files in a local `trips/` folder
- Menu-driven interface to create, view, and delete saved trips

## Tech Stack

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for dependency management
- `requests` for API calls
- `python-dotenv` for `.env` support
- OpenRouter free model: `openrouter/free`

## Installation (uv)

```bash
uv sync
```

## Environment Setup

1. Open `.env`
2. Set your API key:

```env
OPENROUTER_API_KEY=your_real_openrouter_key
```

## Run the Application

```bash
uv run python app.py
```

## Example Output

```text
=== AI Travel Planner ===
1. Create Trip Plan
2. View Saved Trips
3. Delete Saved Trip
4. Exit
Choose an option (1-4): 1

=== Generated Itinerary ===

1) Day-wise itinerary
- Day 1: ...
- Day 2: ...
...
```
