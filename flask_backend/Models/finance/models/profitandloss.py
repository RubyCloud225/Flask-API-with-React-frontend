import json
import pandas as pd

class ProfitAndLossCalculator:
    def __init__(self, income, expenditure, start_date, end_date):
        self.income = income
        self.expenditure = expenditure
        self.start_date = start_date
        self.end_date = end_date
    
    def calculate_gross_profit(self):
        total_income = sum(self.income)
        total_cost_of_sales = sum([x for x in self.expenditure if x['type'] == 'cost_of_sales'])
        return total_income - total_cost_of_sales
    
    def calculate_net_profit(self):
        gross_profit = self.calculate_gross_profit()
        total_expenditure = sum([x['amount'] for x in self.expenditure])
        return gross_profit - total_expenditure
    
    def get_profit_and_loss_statement(self):
        total_income = sum(self.income)
        total_cost_of_goods_sold = sum([x['amount'] for x in self.expenditure if x['type'] == 'cost_of_goods_sold'])
        gross_profit = self.calculate_gross_profit()
        total_operating_expenses = sum([x['amount'] for x in self.expenditure if x['type'] == 'operating_expense'])
        net_profit = self.calculate_net_profit()

        cost_of_goods_sold_items = [{'description': x['description'], 'amount': x['amount']} for x in self.expenditure if x['type'] == 'cost_of_goods_sold']
        operating_expenses_items = [{'description': x['description'], 'amount': x['amount']} for x in self.expenditure if x['type'] == 'operating_expense']

        data = {
            'totalIncome': total_income,
            'costOfGoodsSold': {
                'total': total_cost_of_goods_sold,
                'items': cost_of_goods_sold_items
            },
            'grossProfit': gross_profit,
            'operatingExpenses': {
                'total': total_operating_expenses,
                'items': operating_expenses_items
            },
            'netProfit': net_profit
        }
        df = pd.DataFrame(data)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df[(df['Date'] >= self.start_date) & (df['Date' <= self.end_date])]

        return json.dumps(data)

