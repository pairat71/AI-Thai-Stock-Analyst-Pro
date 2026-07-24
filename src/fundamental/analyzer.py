import yfinance as yf

class FundamentalAnalyzer:

    def analyze(self, symbol):

        info = yf.Ticker(symbol).info

        return {
            "PE": info.get("trailingPE"),
            "PBV": info.get("priceToBook"),
            "ROE": info.get("returnOnEquity"),
            "Dividend": info.get("dividendYield")
        }