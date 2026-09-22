from planners.travel_planner import TravelPlanner


def main():

    print(
        "\n✈️ AI Travel Planner\n"
    )

    source = input(
        "Source: "
    )

    destination = input(
        "Destination: "
    )

    days = input(
        "Number of Days: "
    )

    budget = input(
        "Budget (Low/Medium/High): "
    )

    planner = TravelPlanner()

    result = planner.create_plan(
        source,
        destination,
        days,
        budget
    )

    print("\n")
    print("=" * 50)
    print(result)
    print("=" * 50)


if __name__ == "__main__":
    main()