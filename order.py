"""Order processing functions with input validation."""

import math


def _validate_number(value: float, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def calculate_discount(price: float, discount_percent: float) -> float:
    """Return the price after applying a percentage discount."""
    _validate_number(price, "price")
    _validate_number(discount_percent, "discount_percent")

    if price < 0:
        raise ValueError("price cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")

    return price * (1 - discount_percent / 100)


def calculate_gst(amount: float, gst_rate: float = 18) -> float:
    """Return the GST amount for an order."""
    _validate_number(amount, "amount")
    _validate_number(gst_rate, "gst_rate")

    if amount < 0:
        raise ValueError("amount cannot be negative")
    if not 0 <= gst_rate <= 100:
        raise ValueError("gst_rate must be between 0 and 100")

    return amount * gst_rate / 100


def calculate_order_total(
    price: float,
    discount_percent: float,
    gst_rate: float = 18,
) -> float:
    """Return the final order total after discount and GST."""
    discounted_price = calculate_discount(price, discount_percent)
    gst_amount = calculate_gst(discounted_price, gst_rate)
    return discounted_price + gst_amount
