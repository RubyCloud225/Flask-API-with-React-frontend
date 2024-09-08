


class FinancialRatios:
    def __init__(self, revenue, gross_profit, operating_profit, share_price, book_value_per_share, net_profit, total_assets, total_equity, total_debt, current_assets, current_liabilities, inventory, accounts_receivable, account_payable):
        self.revenue = revenue
        self.gross_profit = gross_profit
        self.operating_profit = operating_profit
        self.net_profit = net_profit
        self.total_assets = total_assets
        self.total_equity = total_equity
        self.total_debt = total_debt
        self.current_assets = current_assets
        self.current_liabilities = current_liabilities
        self.inventory = inventory 
        self.accounts_receivable = accounts_receivable
        self.account_payable = account_payable
        self.share_price = share_price
        self.book_value_per_share = book_value_per_share
    
    def calculate_gross_margin_ratio(self):
        return self.gross_profit / self.revenue
    
    def calculate_operating_margin(self):
        return self.operating_profit / self.revenue
    
    def calculate_net_profit_margin(self):
        return self.net_profit / self.revenue
    
    def calculate_return_on_capital_employed(self):
        return self.operating_profit / (self.total_assets - self.current_liabilities)
    
    def calculate_gearing_ratio(self):
        return self.total_debt / self.total_equity
    
    def calculate_debtor_days(self):
        return (self.accounts_receivable / self.revenue) * 365
    
    def calculate_creditor_days(self):
        return (self.account_payable / self.revenue) * 365
    
    def calculate_quick_ratio(self):
        return (self.current_assets - self.inventory) / self.current_liabilities
    
    def calculate_price_to_book_ratio(self):
        return self.share_price / self.book_value_per_share

    def calculate_price_to_equity_ratio(self):
        return self.share_price / (self.total_equity / self.total_assets)
    
    def run_ratios(self):
        output = {
            "Gross Margin Ratio": self.calculate_gross_margin_ratio(),
            "Operating Profit Margin Ratio": self.calculate_operating_profit_margin_ratio(),
            "Net Profit Margin Ratio": self.calculate_net_profit_margin_ratio(),
            "Return on Investment (ROI)": self.calculate_return_on_investment(),
            "Return on Capital Employed (ROCE)": self.calculate_return_on_capital_employed(),
            "Gearing Ratio": self.calculate_gearing_ratio(),
            "Debtor Days": self.calculate_debtor_days(),
            "Creditor Days": self.calculate_creditor_days(),
            "Current Ratio": self.calculate_current_ratio(),
            "Quick Ratio": self.calculate_quick_ratio(),
            "Price to Book Ratio": self.calculate_price_to_book_ratio(),
            "Price to Equity Ratio": self.calculate_price_to_equity_ratio()
        }

        
