import pygal

class DataQuery:
    def chartType(self):
        #ask for Chart Type
        try:
            print("Chart Types")
            print("-------------------------")
            print("1. Bar")
            print("2. Line")
            self.chart_type = input("Enter the Chart Type you want (1, 2):")
        except ValueError:
            print("Your input was invaild(Enter '1' or '2')")

    # Create graph based on user's selection
    def createGraph(self, x_data, y_data):
        # Create graph type
        if self.chart_type == "1":
            chart = pygal.Bar()
            chart.render_in_browser()
        elif self.chart_type == "2":
            chart = pygal.Line()
            chart.render_in_browser()
        else:
            print("Invalid chart type entered. Defaulting to line chart.")
            chart = pygal.Line()
            chart.render_in_browser()


