"""Provide seasonal gardening advice for flowers and vegetables."""

SEASON_ADVICE = {
    "summer": "Water your plants regulary and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
}


def get_gardening_advice(season, plant_type):
    """Return advice for the selected season and plant type."""
    season_tip = SEASON_ADVICE.get(season, "No advice for this season.")
    plant_tip = PLANT_ADVICE.get(
        plant_type, "No advice for this type of plant."
    )

    return f"{season_tip}\n{plant_tip}"


def main():
    """Ask the user for choices and print gardening advice."""
    season = input("Enter a season (summer or winter): ").strip().lower()
    plant_type = input(
        "Enter a plant type (flower or vegetable): "
    ).strip().lower()

    advice = get_gardening_advice(season, plant_type)
    print("\nYour gardening advice:")
    print(advice)


if __name__ == "__main__":
    main()
