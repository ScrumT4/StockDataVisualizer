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
