from flask import Flask, request, jsonify
from db.transaction import IncomeInvoices, PurchaseInvoices, Reciepts, Payments
from models.profitandloss import ProfitAndLossCalculator
from models.trial_balance import TrialBalance, GeneralLedger
from models.balancesheet import BalanceSheet

db = IncomeInvoices, PurchaseInvoices, Reciepts, Payments
app = Flask(__name__)

@app.route("/IncomeInvoices", methods=["POST"])
def add_IncomeInvoices():
    data = request.get_json()
    user_id = data["user_id"]
    transaction = transaction(
        user_id=user_id,
        date=data["date"],
        description=data["description"],
        credit_account=data["credit_account"],
        credit_amount=data["credit_amount"],
        debit_account=data["debit_account"],
        debit_amount=data["debit_amount"],
        )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added successfully"})

@app.route("/PurchaseInvoices", methods=["POST"])
def add_PurchaseInvoices():
    data = request.get_json()
    user_id = data["user_id"]
    transaction = transaction(
        user_id=user_id,
        date=data["date"],
        description=data["description"],
        credit_account=data["credit_account"],
        credit_amount=data["credit_amount"],
        debit_account=data["debit_account"],
        debit_amount=data["debit_amount"],
        )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added successfully"})

@app.route("/Reciepts", methods=["POST"])
def add_Receipts():
    data = request.get_json()
    user_id = data["user_id"]
    transaction = transaction(
        user_id=user_id,
        date=data["date"],
        description=data["description"],
        credit_account=data["credit_account"],
        credit_amount=data["credit_amount"],
        debit_account=data["debit_account"],
        debit_amount=data["debit_amount"],
        )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added successfully"})

@app.route("/Payments", methods=["POST"])
def add_Payments():
    data = request.get_json()
    user_id = data["user_id"]
    transaction = transaction(
        user_id=user_id,
        date=data["date"],
        description=data["description"],
        credit_account=data["credit_account"],
        credit_amount=data["credit_amount"],
        debit_account=data["debit_account"],
        debit_amount=data["debit_amount"],
        )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added successfully"})

@app.route("/JournalEntries", methods=["POST"])
def add_JournalEntries():
    data = request.get_json()
    user_id = data["user_id"]
    transaction = transaction(
        user_id=user_id,
        date=data["date"],
        description=data["description"],
        credit_account=data["credit_account"],
        credit_amount=data["credit_amount"],
        debit_account=data["debit_account"],
        debit_amount=data["debit_amount"],
        )
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added successfully"})

@app.route('/profit-and-loss', methods=['GET', 'POST'])
def get_profit_and_loss():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        data = request.get_json(start_date, end_date)
        income = data["AccountType_id.income"]
        expenditure = data["AccountType_id.expenditure"]
        calculator = ProfitAndLossCalculator(income, expenditure)
        profitloss = calculator.get_profit_and_loss_statement()
        return jsonify(profitloss.to_dict)
    else:
        return jsonify({'"error': "invalid request method"})

@app.route('/balancesheet', methods=['GET'])
def get_balance_sheet():
    data = request.get_json()
    balancesheet = data.BalanceSheet(BalanceSheet)
    return jsonify(balancesheet)

@app.route('/trial_balance', method=['GET'])
def get_trail_balance():
    data = request.get_json()
    trailbalance = data.TrialBalance(TrialBalance)
    return jsonify(trailbalance)

@app.route('/general_ledger', method=['GET'])
def get_general_ledger():
    data = request.get_json()
    generalledger = data.GeneralLedger(GeneralLedger)
    return jsonify(generalledger)

@app.route('/agedcredtors', methods=['GET'])
def get_aged_credtors():
    data = request.get_json()
    PurchaseInvoices = data.PurchaseInvoices()
    payments = data.Payments()
    ageddebtors = data.AgedTradeCredtors(PurchaseInvoices, payments)
    return jsonify(ageddebtors)

@app.route('/ageddebtors', methods=['GET'])
def get_aged_debtors():
    data = request.get_json()
    Invoices = data.Invoices()
    Reciepts = data.Reciepts()
    ageddebtors = data.AgedTradeDebtors(Invoices, Reciepts)
    return jsonify(ageddebtors)

@app.route("/Sales", methods=["GET"])
def get_sales():
    sales = IncomeInvoices.query.all()
    data = []
    for sale in sales:
        data.append({
            "ID": sale.id,
            "date": sale.date.strftime("%y-%m-%d"),
            "nominal_id": sale.nominal_id,
            "AccountType_id": sale.AccountType_id,
            "description": sale.description,
            "credit_account": sale.credit_account,
            "credit_amount": sale.credit_amount,
            "debit_account": sale.debit_account,
            "debit_amount": sale.debit_amount,
        })
    return jsonify(data)

@app.route("export_csv", methods=["GET"])
def export_csv():
    sales = IncomeInvoices.query.all()
    csv_data = "id, date, nominal_id, AccountType_id,description,credit_account,credit_amount,debit_account,debit_amount\n"
    for sale in sales:
        csv_data += f"{sale.id},{sale.user_id},{sale.date.strftime('%Y-%m-%d')},{sale.nominal_id},{sale.AccountType_id},{sale.description},{sale.credit_account},{sale.credit_amount},{sale.debit_account},{sale.debit_amount}\n"
    return jsonify(csv_data, mimetype="text/csv", headers={"Content-disposition": "attachment; filename=sales.csv"})

if __name__ == '__main__':
    app.run(debug=True)