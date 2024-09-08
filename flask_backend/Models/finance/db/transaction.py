from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.profitandloss import ProfitAndLossCalculator
from models.trial_balance import TrialBalance, GeneralLedger
from models.balancesheet import BalanceSheet

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sql:///transactions.db"
db = SQLAlchemy(app)

class IncomeInvoices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForignKey('Users.id'))
    date = db.Column(db.DateTime, nullable=False)
    nominal_id = db.Column(db.Integer, db.ForignKey('Nominal.id'))
    AccountType_id = db.Column(db.Integer, db.ForignKey('AccountType.id'))
    description = db.Column(db.String(100), nullable=False)
    credit_account = db.Column(db.String(50), nullable=False)
    credit_amount = db.Column(db.Float, nullable=False)
    debit_account = db.Column(db.String(50), nullable=False)
    debit_amount = db.Column(db.Float, nullable=False)

    user = db.relationship('User', backref=db.backref('IncomeInvoices', lazy=True))

class PurchaseInvoices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForignKey('Users.id'))
    date = db.Column(db.DateTime, nullable=False)
    nominal_id = db.Column(db.Integer, db.ForignKey('Nominal.id'))
    AccountType_id = db.Column(db.Integer, db.ForignKey('AccountType.id'))
    description = db.Column(db.String(100), nullable=False)
    credit_account = db.Column(db.String(50), nullable=False)
    credit_amount = db.Column(db.Float, nullable=False)
    debit_account = db.Column(db.String(50), nullable=False)
    debit_amount = db.Column(db.Float, nullable=False)

    user = db.relationship('User', backref=db.backref('PurchaseInvoices', lazy=True))

class Reciepts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForignKey('Users.id'))
    date = db.Column(db.DateTime, nullable=False)
    nominal_id = db.Column(db.Integer, db.ForignKey('Nominal.id'))
    AccountType_id = db.Column(db.Integer, db.ForignKey('AccountType.id'))
    description = db.Column(db.String(100), nullable=False)
    credit_account = db.Column(db.String(50), nullable=False)
    credit_amount = db.Column(db.Float, nullable=False)
    debit_account = db.Column(db.String(50), nullable=False)
    debit_amount = db.Column(db.Float, nullable=False)

    user = db.relationship('User', backref=db.backref('Reciepts', lazy=True))

class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForignKey('Users.id'))
    date = db.Column(db.DateTime, nullable=False)
    nominal_id = db.Column(db.Integer, db.ForignKey('Nominal.id'))
    AccountType_id = db.Column(db.Integer, db.ForignKey('AccountType.id'))
    description = db.Column(db.String(100), nullable=False)
    credit_account = db.Column(db.String(50), nullable=False)
    credit_amount = db.Column(db.Float, nullable=False)
    debit_account = db.Column(db.String(50), nullable=False)
    debit_amount = db.Column(db.Float, nullable=False)

    user = db.relationship('User', backref=db.backref('Payments', lazy=True))

@app.route("/invoices", methods=["POST"])
def add_invoices():
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

@app.route('/ageddebtors', methods=['GET'])
def get_aged_debtors():
    data = request.get_json()
    Purchaseinvoices = data.PurchaseInvoices()
    payments = data.Payments()
    ageddebtors = data.AgedTradeDebtors(PurchaseInvoices, payments)
    return jsonify(ageddebtors)

@app.route('/agedcreditors', methods=['GET'])
def get_aged_creditors():
    data = request.get_json()
    Invoices = data.Invoices()
    Reciepts = data.Reciepts()
    ageddebtors = data.AgedTradeDebtors(Invoices, Reciepts)
    return jsonify(ageddebtors)


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)