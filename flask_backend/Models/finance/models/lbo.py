

class LBOModel:
    def __init__(self, enterprise_value, equity_value, debt_value, cash_flow, growth_rate, discount_rate, years):
        self.enterprise_value = enterprise_value
        self.equity_value = equity_value
        self.debt_value = debt_value
        self.cash_flow = cash_flow
        self.growth_rate = growth_rate
        self.discount_rate = discount_rate
        self.years = years

    def calculate_equity_value(self):
        equity_value = self.cash_flow * (1 + self.growth_rate) / (self.discount_rate - self.growth_rate) * (1 - (1 + self.growth_rate) ** (-self.years))
        return equity_value

    def calculate_debt_value(self):
        debt_value = self.debt_value * (1 + self.discount_rate) ** (-self.years)
        return debt_value

    def calculate_enterprise_value(self):
        enterprise_value = self.calculate_equity_value() + self.calculate_debt_value() - self.cash_flow
        return enterprise_value

    def calculate_lbo_return(self):
        lbo_return = (self.calculate_enterprise_value() - self.equity_value) / self.equity_value
        return lbo_return

    def calculate_lbo_multiple(self):
        lbo_multiple = self.calculate_enterprise_value() / self.cash_flow
        return lbo_multiple