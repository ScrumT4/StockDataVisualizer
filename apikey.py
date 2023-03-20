from requests import *

class DataQuery:  
    def stocksymbol():
        try:
            print("Stock Data Visulaizer")
            print("-------------------------")
            global symbol  
            symbol = input("Enter the symbol of the stock you would like to see:")
        except ValueError:
            print("Your input was invaild")

    stocksymbol()
    def query(ticker, function, interval):
        apiKey = "VVYFBPRGDKHX0K93"
        url = 'https://www.alphavantage.co/query?function=%s&symbol=%s&interval=%s&apikey=%s' % (ticker, symbol, interval, apiKey)
        r = get(url)
        data = r.json()
        return data
