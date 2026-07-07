from .logs import logger


def validate_order(symbol, side, order_type, quantity, price=None):

    if not symbol:
        logger.error("Symbol cannot be empty.")
        raise ValueError("Symbol cannot be empty.")

    if side not in ["BUY", "SELL"]:
        logger.error(f"Invalid side: {side}")
        raise ValueError("Side must be BUY or SELL.")

    if order_type not in ["MARKET", "LIMIT"]:
        logger.error(f"Invalid order type: {order_type}")
        raise ValueError("Order type must be MARKET or LIMIT.")

    if quantity <= 0:
        logger.error(f"Invalid quantity: {quantity}")
        raise ValueError("Quantity must be greater than 0.")

    if order_type == "LIMIT":
        if price is None:
            logger.error("Price is required for LIMIT orders.")
            raise ValueError("Price is required for LIMIT orders.")

        if price <= 0:
            logger.error(f"Invalid price: {price}")
            raise ValueError("Price must be greater than 0.")

    logger.info("Input validation successful.")