"""Pytest tests for the order-processing functions."""

import pytest

from order import calculate_discount, calculate_gst, calculate_order_total


def test_calculate_discount_valid():
    assert calculate_discount(1000, 10) == pytest.approx(900)


def test_calculate_discount_zero():
    assert calculate_discount(500, 0) == pytest.approx(500)


@pytest.mark.parametrize("discount", [-1, 101])
def test_calculate_discount_invalid(discount):
    with pytest.raises(ValueError):
        calculate_discount(100, discount)


def test_calculate_discount_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)


def test_calculate_discount_invalid_types():
    with pytest.raises(TypeError):
        calculate_discount("100", 10)


def test_calculate_gst_valid():
    assert calculate_gst(100, 18) == pytest.approx(18)


def test_calculate_gst_default_rate():
    assert calculate_gst(100) == pytest.approx(18)


def test_calculate_order_total_valid():
    assert calculate_order_total(1000, 10, 18) == pytest.approx(1062)


def test_calculate_order_total_negative_price():
    with pytest.raises(ValueError):
        calculate_order_total(-100, 10)
