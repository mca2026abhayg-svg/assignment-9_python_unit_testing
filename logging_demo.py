"""Demonstrate DEBUG, INFO, WARNING, and ERROR logging for order processing."""

import logging

from order import calculate_discount, calculate_gst

LOG_FILE = "application.log"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="w"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def process_order(price: float, discount_percent: float, gst_rate: float = 18) -> float:
    """Process an order and record each stage."""
    logger.debug("Starting order processing")
    logger.debug(
        "Received price=%r, discount=%r%%, gst_rate=%r%%",
        price,
        discount_percent,
        gst_rate,
    )

    try:
        discounted_price = calculate_discount(price, discount_percent)
        logger.info("Discount applied: discounted price is %.2f", discounted_price)

        gst_amount = calculate_gst(discounted_price, gst_rate)
        total = discounted_price + gst_amount
        logger.info("GST calculated: %.2f", gst_amount)
        logger.info("Order total calculated: %.2f", total)

        if discount_percent == 0:
            logger.warning("No discount was applied")

        if gst_rate == 0:
            logger.warning("No GST was applied")

        return total
    except (TypeError, ValueError) as exc:
        logger.error("Order processing failed: %s", exc)
        raise


if __name__ == "__main__":
    process_order(1000, 10, 18)
    process_order(500, 0, 18)
    try:
        process_order(-100, 10, 18)
    except ValueError:
        logger.error("An invalid order was rejected")
