
def stocksymbol():
    try:
        print("Stock Data Visulaizer")
        print("-------------------------")
        global symbol  
        symbol = input("Enter the symbol of the stock you would like to see:")
    except ValueError:
        print("Your input was invaild")

stocksymbol()