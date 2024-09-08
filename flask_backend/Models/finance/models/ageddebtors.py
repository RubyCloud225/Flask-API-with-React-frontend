import datetime
import json

class AgedTradeDebtors:
    def __init__(self, invoices, payments):
        self.invoices = invoices
        self.payments = payments

    def get_aged_trade_debtors(self, as_at_date, payment_cutoff_date):
        debtors = {}
        for invoice in self.invoices:
            debtor = invoice['debtor']
            if debtor not in debtors:
                debtors[debtor] = {
                    'categories': ['0-30 days', '31-60 days', '61-90 days', 'over 90 days'],
                    'data': [0, 0, 0, 0]
                }
            days_overdue = (as_at_date - invoice['date']).days
            if days_overdue <= 30:
                debtors[debtor]['data'][0] += invoice['amount']
            elif days_overdue <= 60:
                debtors[debtor]['data'][1] += invoice['amount']
            elif days_overdue <= 90:
                debtors[debtor]['data'][2] += invoice['amount']
            else:
                debtors[debtor]['data'][3] += invoice['amount']

        for payment in self.payments:
            if payment['date'] >= payment_cutoff_date:
                debtor = payment['debtor']
                if debtor in debtors:
                    debtors[debtor]['data'][0] -= payment['amount']
                    if debtors[debtor]['data'][0] < 0:
                        debtors[debtor]['data'][1] += debtors[debtor]['data'][0]
                        debtors[debtor]['data'][0] = 0
                    if debtors[debtor]['data'][1] < 0:
                        debtors[debtor]['data'][2] += debtors[debtor]['data'][1]
                        debtors[debtor]['data'][1] = 0
                    if debtors[debtor]['data'][2] < 0:
                        debtors[debtor]['data'][3] += debtors[debtor]['data'][2]
                        debtors[debtor]['data'][2] = 0

        total_outstanding = sum(sum(debtor['data']) for debtor in debtors.values())

        output = {
            'debtors': debtors,
            'total_outstanding': total_outstanding
        }

        return json.dumps(output)


"""
# Example usage:
invoices = [
    {'date': datetime.date(2022, 1, 1), 'amount': 1000, 'debtor': 'John'},
    {'date': datetime.date(2022, 1, 15), 'amount': 2000, 'debtor': 'Jane'},
    {'date': datetime.date(2022, 2, 1), 'amount': 3000, 'debtor': 'John'},
    {'date': datetime.date(2022, 3, 1), 'amount': 4000, 'debtor': 'Jane'},
    {'date': datetime.date(2022, 4, 1), 'amount': 5000, 'debtor': 'Bob'}
]

payments = [
    {'date': datetime.date(2022, 4, 10), 'amount': 2000, 'debtor': 'John'},
    {'date': datetime.date(2022, 4, 12), 'amount': 1500, 'debtor': 'Jane'},
    {'date': datetime.date(2022, 4, 15), 'amount': 3000, 'debtor': 'Bob'}
]

as_at_date = datetime.date(2022, 4, 15)
payment_cutoff_date = datetime.date(2022, 4, 10)

aged_trade_debtors = AgedTradeDebtors(invoices, payments)
print("Aged Trade Debtors as at", as_at_date.strftime("%d/%m/%Y"))
print(aged_trade_debtors.get_aged_trade_debtors(as_at_date, payment_cutoff_date))

"""