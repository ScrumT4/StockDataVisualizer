from requests import *

class DataQuery:
    def query(ticker, function, interval):
        apiKey = "VVYFBPRGDKHX0K93"
        # Ask user for chart type
        chart_type = input("Enter Chart Type (line/bar): ")
        
        url = 'https://www.alphavantage.co/query?function=%s&symbol=%s&interval=%s&apikey=%s' % (ticker, function, interval, apiKey)
        r = get(url)
        data = r.json()
        return data