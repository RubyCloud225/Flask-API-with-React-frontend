import datetime
import json

class AgedTradeCreditors:
    def __init__(self, bills, payments):
        self.bills = bills
        self.payments = payments

    def get_aged_trade_creditors(self, as_at_date, payment_cutoff_date):
        creditors = {}
        for bill in self.bills:
            creditor = bill['creditor']
            if creditor not in creditors:
                creditors[creditor] = {
                    'categories': ['0-30 days', '31-60 days', '61-90 days', 'over 90 days'],
                    'data': [0, 0, 0, 0]
                }
            days_overdue = (as_at_date - bill['date']).days
            if days_overdue <= 30:
                creditors[creditor]['data'][0] += bill['amount']
            elif days_overdue <= 60:
                creditors[creditor]['data'][1] += bill['amount']
            elif days_overdue <= 90:
                creditors[creditor]['data'][2] += bill['amount']
            else:
                creditors[creditor]['data'][3] += bill['amount']

        for payment in self.payments:
            if payment['date'] >= payment_cutoff_date:
                creditor = payment['creditor']
                if creditor in creditors:
                    creditors[creditor]['data'][0] -= payment['amount']
                    if creditors[creditor]['data'][0] < 0:
                        creditors[creditor]['data'][1] += creditors[creditor]['data'][0]
                        creditors[creditor]['data'][0] = 0
                    if creditors[creditor]['data'][1] < 0:
                        creditors[creditor]['data'][2] += creditors[creditor]['data'][1]
                        creditors[creditor]['data'][1] = 0
                    if creditors[creditor]['data'][2] < 0:
                        creditors[creditor]['data'][3] += creditors[creditor]['data'][2]
                        creditors[creditor]['data'][2] = 0

        total_outstanding = sum(sum(creditor['data']) for creditor in creditors.values())

        output = {
            'creditors': creditors,
            'total_outstanding': total_outstanding
        }

        return json.dumps(output)

"""
# Example usage:
bills = [
    {'date': datetime.date(2022, 1, 1), 'amount': 1000, 'creditor': 'Supplier A'},
    {'date': datetime.date(2022, 1, 15), 'amount': 2000, 'creditor': 'Supplier B'},
    {'date': datetime.date(2022, 2, 1), 'amount': 3000, 'creditor': 'Supplier A'},
    {'date': datetime.date(2022, 3, 1), 'amount': 4000, 'creditor': 'Supplier B'},
    {'date': datetime.date(2022, 4, 1), 'amount': 5000, 'creditor': 'Supplier C'}
]

payments = [
    {'date': datetime.date(2022, 4, 10), 'amount': 2000, 'creditor': 'Supplier A'},
    {'date': datetime.date(2022, 4, 12), 'amount': 1500, 'creditor': 'Supplier B'},
    {'date': datetime.date(2022, 4, 15), 'amount': 3000, 'creditor': 'Supplier C'}
]

as_at_date = datetime.date(2022, 4, 15)
payment_cutoff_date = datetime.date(2022, 4, 10)

aged_trade_creditors = AgedTradeCreditors(bills, payments)
print("Aged Trade Creditors as at", as_at_date.strftime("%d/%m/%Y"))
print(aged_trade_creditors.get_aged_trade_creditors(as_at_date, payment_cutoff_date))

"""