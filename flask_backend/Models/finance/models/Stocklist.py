import json

class StockList:
    def __init__(self):
        self.stocks = []

    def add_stock(self, id, description, quantity, cost, selling_price, estimated_selling_costs):
        stock = {
            "id": id,
            "description": description,
            "quantity": quantity,
            "cost": cost,
            "selling_price": selling_price,
            "estimated_selling_costs": estimated_selling_costs,
            "net_realisable_value": self.calculate_net_realisable_value(selling_price, estimated_selling_costs)
        }
        self.stocks.append(stock)

    def calculate_net_realizable_value(self, selling_price, estimated_selling_expenses):
        return selling_price - estimated_selling_expenses

    def calculate_total_cost(self):
        return sum(stock["cost"] * stock["quantity"] for stock in self.stocks)

    def calculate_total_net_realizable_value(self):
        return sum(stock["net_realizable_value"] * stock["quantity"] for stock in self.stocks)

    def calculate_provision_for_obsolescence(self):
        total_cost = self.calculate_total_cost()
        total_net_realizable_value = self.calculate_total_net_realizable_value()
        if total_net_realizable_value < total_cost:
            return total_cost - total_net_realizable_value
        else:
            return 0

    def get_stocks(self):
        return self.stocks

    def to_json(self):
        return json.dumps(self.stocks, indent=4)
    
"""
# Create an instance of the StockList class
stock_list = StockList()

# Add some stocks to the list
stock_list.add_stock(1, "Product A", 100, 10.00, 15.00, 2.00)
stock_list.add_stock(2, "Product B", 50, 20.00, 25.00, 3.00)
stock_list.add_stock(3, "Product C", 200, 5.00, 10.00, 1.00)

# Calculate the total cost and net realizable value
total_cost = stock_list.calculate_total_cost()
total_net_realizable_value = stock_list.calculate_total_net_realizable_value()

# Calculate the provision for obsolescence
provision_for_obsolescence = stock_list.calculate_provision_for_obsolescence()

# Print the results
print("Total Cost: £", total_cost)
print("Total Net Realizable Value: £", total_net_realizable_value)
print("Provision for Obsolescence: £", provision_for_obsolescence)

# Get the stocks as a JSON string
stocks_json = stock_list.to_json()

# Print the JSON data
print(stocks_json)

"""