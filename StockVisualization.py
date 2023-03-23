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
 
