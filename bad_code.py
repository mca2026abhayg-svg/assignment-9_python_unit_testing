"""Demonstrate Ruff-clean Python code."""


def calculate_shipping_cost(distance_km: float) -> float:
    """Calculate a flat shipping cost based on the travel distance."""
    if distance_km < 0:
        raise ValueError("distance_km cannot be negative")
    if distance_km == 0:
        return 0.0
    return 50.0 + distance_km * 2.5


def main() -> None:
    """Run the code-quality demonstration."""
    cost = calculate_shipping_cost(10)
    print(f"Shipping cost: {cost:.2f}")


if __name__ == "__main__":
    main()
