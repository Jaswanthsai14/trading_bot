import argparse
from bot.validation import validate_order
from bot.orders import create_order

def main():
  parser=argparse.ArgumentParser(description="Binance Trading bot")
  parser.add_argument("--symbol",required=True,help="Trading example(e.g. BTCUSDT)")
  parser.add_argument("--side",required=True,help="order side",choices=["BUY","SELL"])
  parser.add_argument("--type",required=True,help="order type",choices=["MARKET","LIMIT"]) 
  parser.add_argument("--quantity",required=True,help="order Quantity",type=float)
  parser.add_argument("--price",help="req for LIMIT orders",type=float)
  args=parser.parse_args()
  try:
      validate_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price,
        )
      res= create_order(
            symbol=args.symbol,
            side=args.side,
            quantity=args.quantity,
            order_type=args.type,
            price=args.price,
        )
      print("\n----------Order Request---------------")
      print(f"Symbol   : {args.symbol}")
      print(f"Side     : {args.side}")
      print(f"Type     : {args.type}")
      print(f"Quantity : {args.quantity}")
      if args.type == "LIMIT":
            print(f"Price    : {args.price}")
      print("\n----------Order Response---------------")
      print(f"Order ID      : {res.get('orderId')}")
      print(f"Status        : {res.get('status')}")
      print(f"Executed Qty  : {res.get('executedQty')}")
      print(f"Average Price : {res.get('avgPrice')}")
      print("\n order placed successfully")
      
  except Exception as e:
      print(f"\n {e}")
if __name__=="__main__":
    main()
      
