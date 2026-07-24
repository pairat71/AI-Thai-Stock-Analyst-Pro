import yfinance as yf

class YahooProvider:

    def get_stock(self, symbol):

        stock = yf.Ticker(symbol)
        info = stock.info

        return {
            "symbol": symbol,
            "name": info.get("longName"),
            "price": info.get("currentPrice")
        }