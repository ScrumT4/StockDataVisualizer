def timeSeriesFunction():
    try:
        print("Select the Time Series of the chart you would like to generate\n------------------------------------------------")
        print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
        global tsf
        tsf = input("\nEnter Time Series option (1, 2, 3, 4): \n")
    except ValueError:
        print("Invalid input. Please input 1, 2, 3, or 4")

timeSeriesFunction()