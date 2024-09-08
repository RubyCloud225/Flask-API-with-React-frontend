import json


class DCFModel:
    def __init__(self, revenue, net_profit_margin, depreciation, amortization, capital_expenditures, working_capital, tax_rate, discount_rate, growth_rate, terminal_growth_rate, debt, cash_and_equivalents, minority_interest, shares_outstanding):
        self.revenue = revenue
        self.net_profit_margin = net_profit_margin
        self.depreciation = depreciation
        self.amortization = amortization
        self.capital_expenditures = capital_expenditures
        self.working_capital = working_capital
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate
        self.growth_rate = growth_rate
        self.terminal_growth_rate = terminal_growth_rate
        self.debt = debt
        self.cash_and_equivalents = cash_and_equivalents
        self.minority_interest = minority_interest
        self.shares_outstanding = shares_outstanding
    
    def calculate_net_profit(self):
        net_profit = [rev * self.net_profit_margin for rev in self.revenue]
        return net_profit
    
    def calculate_ebitda(self, net_profit):
        ebitda = [np + self.depreciation + self.amortization for np in net_profit]
        return ebitda
    
    def calculate_cash_flow(self, ebitda):
        cash_flow = [ebit * (1 - self.tax_rate) + self.depreciation + self.amortization - self.capital_expenditures - self.working_capital for ebit in ebitda]
        return cash_flow
    
    def calculate_present_value(self, cash_flow):
        present_value = 0
        for i, cf in enumerate(cash_flow):
            present_value += cf / (1 + self.discount_rate) ** i
        return present_value
    
    def calculate_terminal_value(self, cash_flow):
        terminal_value = cash_flow[-1] * (1 + self.growth_rate) / (self.discount_rate - self.terminal_growth_rate)
        return terminal_value
    
    def calculate_enterprise_value(self, present_value, terminal_value, cash_flow):
        enterprise_value = present_value + terminal_value / (1 + self.discount_rate) ** len(cash_flow)
        return enterprise_value
    
    def calculate_equity_value(self, enterprise_value):
        share_price = enterprise_value - self.debt + self.cash_and_equivalents - self.minority_interest
        return share_price
    
    def run_model(self):
        net_profit = self.calculate_net_profit()
        ebitda = self.calculate_ebitda(net_profit)
        cash_flow = self.calculate_cash_flow(ebitda)
        present_value = self.calculate_present_value(cash_flow)
        terminal_value = self.calculate_terminal_value(cash_flow)
        enterprise_value = self.calculate_enterprise_value(present_value, terminal_value, cash_flow)
        equity_value = self.calculate_equity_value(enterprise_value)
        share_price = self.calculate_equity_value(equity_value)

        output = {
            "netProfit": net_profit,
            "ebitda": ebitda,
            "cashFlow": cash_flow,
            "presentValue": present_value,
            "terminalValue": terminal_value,
            "enterpriseValue": enterprise_value,
            "equityValue": equity_value,
            "sharePrice": share_price
        }

        with open("output.json", "w") as f: #use import output from './output.json in react
            json.dumpy(output, f, indent=4)

        print("Output saved to output.json")
    