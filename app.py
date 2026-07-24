from src.data.yahoo_provider import YahooProvider

provider = YahooProvider()

stock = provider.get_stock("PTT.BK")

print("=" * 40)
print("AI Thai Stock Analyst Pro")
print("=" * 40)

print(f"Symbol : {stock['symbol']}")
print(f"Name   : {stock['name']}")
print(f"Price  : {stock['price']}")