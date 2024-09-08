import json

class BalanceSheet:
    def __init__(self, assets, liabilities, equity):
        self.assets = assets
        self.liabilities = liabilities
        self.equity = equity
    
    def get_balance_sheet(self):
        #Fixed Assets
        tangible_assets = sum([x['amount'] for x in self.assets if x['type'] == 'tangible_asset'])
        intangible_assets = sum([x['amount'] for x in self.assets if x['type'] == 'intangible_asset'])
        investments = sum([x['amount'] for x in self.assets if x['type'] == 'investment'])

        #Current Assets
        stock = sum([x['amount'] for x in self.assets if x['type'] == 'stock'])
        debtors = sum([x['amount'] for x in self.assets if x['type'] == 'debtor'])
        cash = sum([x['amount'] for x in self.assets if x['type'] == 'cash'])
        
        #Current Liabilities 
        creditors = sum([x['amount'] for x in self.liabilities if x['type'] == 'creditors'])
        short_term_loans = sum([x['amount'] for x in self.liabilities if x['type'] == 'short_term_loans'])
        other_creditors = sum([x['amount'] for x in self.liabilities if x['type'] =='other_creditors'])

        #Non Current liabilities
        long_term_loans = sum([x['amount'] for x in self.liabilities if x['type'] == 'long_term_loans'])
        other_non_current_creditors = sum([x['amount'] for x in self.liabilities if x['type'] == 'other_non_current_creditors'])

        #Equity
        share_capital = sum([x['amount'] for x in self.assets if x['type'] == 'share_capital'])
        retained_earnings = sum([x['amount'] for x in self.equity if x['type'] == 'retained_earnings'])

        data = {
            'fixedAssets': {
                'tangibleAssets': tangible_assets,
                'intangibleAssets': intangible_assets,
                'investments': investments
            },
            'currentAssets': {
                'stock': stock,
                'debtors': debtors,
                'cash': cash
            },
            'currentLiabilities': {
                'creditors': creditors,
                'shortTermLoans': short_term_loans,
                'otherCreditors': other_creditors
            },
            'nonCurrentLiabilities': {
                'longTermLoans': long_term_loans,
                'otherNonCurrentCreditors': other_non_current_creditors
            },
            'equity': {
                'shareCapital': share_capital,
                'retainedEarnings': retained_earnings
            }
        }

        return json.dumps(data)

"""
#Example usage:
assets = [
    {'description': 'Property', 'amount': 100000, 'type': 'tangible_asset'},
    {'description': 'Equipment', 'amount': 50000, 'type': 'tangible_asset'},
    {'description': 'Stock', 'amount': 20000, 'type': 'stock'},
    {'description': 'Debtors', 'amount': 30000, 'type': 'debtor'},
    {'description': 'Cash', 'amount': 10000, 'type': 'cash'}
]

liabilities = [
    {'description': 'Creditors', 'amount': 15000, 'type': 'creditor'},
    {'description': 'Short-term loan', 'amount': 20000, 'type': 'short_term_loan'},
    {'description': 'Long-term loan', 'amount': 50000, 'type': 'long_term_loan'}
]

equity = [
    {'description': 'Share capital', 'amount': 50000, 'type': 'share_capital'},
    {'description': 'Retained earnings', 'amount': 20000, 'type': 'retained_earnings'}
]

balance_sheet = BalanceSheet(assets, liabilities, equity)
print(balance_sheet.get_balance_sheet())

"""

