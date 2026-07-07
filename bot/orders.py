from .client import BinanceClient
from .logs import logger
broker=BinanceClient()
def create_order(symbol,side,quantity,order_type,price=None):
  if order_type=="MARKET":
    res=broker.create_market_order(symbol=symbol,side=side,quantity=quantity)
    return res
  elif order_type=="LIMIT":
    res=broker.create_limit_order(symbol=symbol,side=side,quantity=quantity,price=price)
    return res
  else:
    logger.error(f"Invalid order type:{order_type}")
    raise ValueError("Invalid Error Type")