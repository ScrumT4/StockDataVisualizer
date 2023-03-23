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

def checkDates():
    format = "%Y-%m-%d"
    while(True):
        try:
            startDate = input('\nEnter the start date (format: YYYY-MM-DD): ')
            endDate = input('\nEnter the end date (format: YYYY-MM-DD): ')
            datetime.strptime(startDate, format)
            datetime.strptime(endDate, format)
            if endDate < startDate:
                print("End date must be after start date")
                continue
            break
        except ValueError as e:
            print("Incorrect start date format, should be YYYY-MM-DD")
            continue
        else:
            break
    return startDate, endDate

def generateGraph(stockSymbol, chartType, timeSeries, data, startDate, endDate):
    format2 = "%Y-%m-%d %H:%M:%S"
    format = "%Y-%m-%d"
    high = []
    low =[]
    close =[]
    open = []
    dateList = []
    stock = stockSymbol
    chart = chartType
    timeS = timeSeries
    sd = startDate
    ed = endDate
    datetime.strptime(sd, format)
    datetime.strptime(ed, format)
    dataList = data
    
    if timeS == 1:
        for date in dataList['Time Series (60min)']:
            datetime.strptime(date, format2)
            if date > ed:
                continue 
            if date <= sd:
                break
            dateList.append(date)
            open.append(dataList['Time Series (60min)'][date]['1. open'])
            high.append(dataList['Time Series (60min)'][date]['2. high'])
            low.append(dataList['Time Series (60min)'][date]['3. low'])
            close.append(dataList['Time Series (60min)'][date]['4. close'])

    if timeS == 2:
        for date in dataList['Time Series (Daily)']:
            datetime.strptime(date, format)
            if date > ed:
                continue 
            if date <= sd:
                break
            dateList.append(date)
            open.append(dataList['Time Series (Daily)'][date]['1. open'])
            high.append(dataList['Time Series (Daily)'][date]['2. high'])
            low.append(dataList['Time Series (Daily)'][date]['3. low'])
            close.append(dataList['Time Series (Daily)'][date]['4. close'])

    if timeS == 3:
        for date in dataList['Weekly Time Series']:
            datetime.strptime(date, format)
            if date > ed:
                continue 
            if date <= sd:
                break
            dateList.append(date)
            open.append(dataList['Weekly Time Series'][date]['1. open'])
            high.append(dataList['Weekly Time Series'][date]['2. high'])
            low.append(dataList['Weekly Time Series'][date]['3. low'])
            close.append(dataList['Weekly Time Series'][date]['4. close'])
            
    if timeS == 4:
        for date in dataList['Monthly Time Series']:
            datetime.strptime(date, format)
            if date > ed:
                continue 
            if date <= sd:
                break
            dateList.append(date)
            open.append(dataList['Monthly Time Series'][date]['1. open'])
            high.append(dataList['Monthly Time Series'][date]['2. high'])
            low.append(dataList['Monthly Time Series'][date]['3. low'])
            close.append(dataList['Monthly Time Series'][date]['4. close'])

    openFloat = [float(item) for item in open]
    highFloat = [float(item) for item in high]
    lowFloat = [float(item) for item in low]
    closeFloat = [float(item) for item in close]

    if chart == 1:
        bar = pygal.Bar(x_label_rotation=90)
        bar.title = stock
        bar.x_labels = map(str, dateList)
        bar.add('Open', openFloat)
        bar.add('High', highFloat)
        bar.add('Low', lowFloat)
        bar.add('Close', closeFloat)
        bar.render_in_browser()

    if chart == 2:
        line = pygal.Line(x_label_rotation=90)
        line.title = stock
        line.x_labels = map(str, dateList)
        line.add('Open', openFloat)
        line.add('High', highFloat)
        line.add('Low', lowFloat)
        line.add('Close', closeFloat)
        line.render_in_browser()
