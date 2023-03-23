import lxml
from datetime import datetime
import requests
import pygal

print('Stock Data Visualizer')

def askCharts():
    ChartMenu()
    chartType = ChartType()
    return chartType

def ChartMenu():
    print('\nChart Types:')
    print('1. Bar')
    print('2. Line') 
   
def ChartType():
    while(True):
        try:
            chartType = int(input('\nPlease enter the chart type that you want: Either 1 or 2 '))
            if chartType == 1:
                print('You selected chart type 1:')
            elif chartType == 2:
                print('You selected chart type 2:')
            elif chartType not in range(1,3): 
                print("You can only choose 1 or 2")
                continue
        except ValueError: 
            print("You can only choose 1 or 2")
            continue
        else:
            break
    return chartType
    
def askSeries():
    TimeSeriesMenu()
    askTimeSeries()
    
def TimeSeriesMenu():
    print('\nSelect the Time Series of the chart you want to generate:')
    print('1. Intraday')
    print('2. Daily')
    print('3. Weekly')
    print('4. Monthly')
 
def askTimeSeries(stockSymbol):
    stock = stockSymbol
    while(True):

        try:
            timeSeries = int(input('\nWhat time series option would you like: Options (1-4): '))
            apiKey = 'VVYFBPRGDKHX0K93'
            
            if timeSeries == 1:
                url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + stock + '&interval=60min&apikey=' + apiKey
                
            elif timeSeries == 2:
                url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock + '&apikey=' + apiKey
                
            elif timeSeries == 3:
                url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + stock + '&apikey=' + apiKey
                
            elif timeSeries == 4:
                url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=' + stock + '&apikey=' + apiKey
                
            elif timeSeries not in range(1,5): 
                print("You can select options 1 through 4 only.")
                continue
        except ValueError: 
            print("You can select options 1 through 4 only.")
            continue
        else:
            break
    r = requests.get(url)
    data = r.json()
    return data, timeSeries
