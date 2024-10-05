from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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

class JournalEntries(db.Model):
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

