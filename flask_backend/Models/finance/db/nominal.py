from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nominals.db'
db = SQLAlchemy(app)

class Nominal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(100), nullable=False, unique=True)
    type = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f'<Nominal {self.name}>'
    
db.create_all()

# Insert Sample Data
nominals = [
    {'account_name': 'Nominal 1', 'code': '001'},
    {'account_name': 'Nominal 2', 'code': '002'},
    {'account_name': 'Nominal 3', 'code': '003'}
]

for nominal in nominals:
    db.session.add(Nominal(**nominal))
db.session.commit()

@app.route('/nominals', methods=['GET'])
def get_nominals():
    nominals = Nominal.query.all()
    return jsonify([{'id': nominal.id, 'name': nominal.name, 'code': nominal.code} for nominal in nominals])

@app.route('/nominals/<string:type>', methods=['GET'])
def get_nominals_by_type(type):
    nominals = Nominal.query.filter_by(type=type).all()
    return jsonify([{'id': nominal.id, 'name': nominal.name, 'code': nominal.code} for nominal in nominals])