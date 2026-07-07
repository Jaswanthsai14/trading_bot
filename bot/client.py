from binance.client import Client

from dotenv import load_dotenv
import os
from binance.exceptions import BinanceAPIException
from.logs import logger

load_dotenv()
class BinanceClient:
  def __init__(self):
    

    self.client=Client( api_key=os.getenv("APIKEY"),
            api_secret=os.getenv("SECRETKEY"),
            testnet=True)
  def create_market_order(self,symbol,side,quantity):
    try:
      res=self.client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )
      logger.info(f"Order Successful | "
                f"OrderId={res.get('orderId')} | "
                f"Status={res.get('status')}")
      return res
      
    except BaseException as e:
      logger.error(f"Binance API Error: {e}")
      raise 
    except Exception as e:
      logger.error(f"Unexpected Error: {e}")
      raise
  def create_limit_order(self,symbol,side,quantity,price):
      try:
        res=self.client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )
        logger.info(f"Order Successful | "
                f"OrderId={res.get('orderId')} | "
                f"Status={res.get('status')}")
        return res
      except BaseException as e:
        logger.error(f"Binance API Error: {e}")
        raise 
      except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise 
