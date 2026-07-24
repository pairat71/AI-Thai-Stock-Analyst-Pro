import yfinance as yf

class YahooProvider:

    def get_stock(self, symbol):

        stock = yf.Ticker(symbol)
        info = stock.info
        history = stock.history(period="5d")

        return {
            "symbol": symbol,
            "name": info.get("longName"),
            "price": info.get("currentPrice"),
            "open": history["Open"].iloc[-1],
            "high": history["High"].iloc[-1],
            "low": history["Low"].iloc[-1],
            "close": history["Close"].iloc[-1],
            "volume": int(history["Volume"].iloc[-1])
        }