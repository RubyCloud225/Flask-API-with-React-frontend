import json

class GeneralLedger:
    def __init__(self):
        self.ledger_accounts = []

    def add_journal_entry(self, account_name, debit, credit, description):
        self.ledger_accounts.append({
            'account_name': account_name,
            'debit': debit,
            'credit': credit,
            'description': description
        })

    def get_general_ledger(self):
        return json.dumps(self.ledger_accounts)

class TrialBalance:
    def __init__(self, general_ledger):
        self.general_ledger = general_ledger

    def get_trial_balance(self):
        debit_totals = {}
        credit_totals = {}

        for entry in self.general_ledger:
            if entry['debit'] > 0:
                if entry['account_name'] in debit_totals:
                    debit_totals[entry['account_name']] += entry['debit']
                else:
                    debit_totals[entry['account_name']] = entry['debit']
            if entry['credit'] > 0:
                if entry['account_name'] in credit_totals:
                    credit_totals[entry['account_name']] += entry['credit']
                else:
                    credit_totals[entry['account_name']] = entry['credit']
        trial_balance = {
            'debit': debit_totals,
            'credit': credit_totals
        }

        return json.dumps(trial_balance)

"""
# Example usage:
general_ledger = GeneralLedger()

general_ledger.add_journal_entry('Cash', 10000, 0, 'Initial investment')
general_ledger.add_journal_entry('Accounts Receivable', 20000, 0, 'Accounts receivable')
general_ledger.add_journal_entry('Sales', 0, 50000, 'Sales revenue')
general_ledger.add_journal_entry('Cost of Goods Sold', 30000, 0, 'Cost of goods sold')
general_ledger.add_journal_entry('Operating Expenses', 20000, 0, 'Operating expenses')
general_ledger.add_journal_entry('Retained Earnings', 0, 50000, 'Retained earnings')
general_ledger.add_journal_entry('Accounts Payable', 0, 15000, 'Accounts payable')

print("General Ledger:")
print(general_ledger.get_general_ledger())

trial_balance = TrialBalance(general_ledger.ledger_accounts)
print("\nTrial Balance:")
print(trial_balance.get_trial_balance())

"""
