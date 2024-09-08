from flask import Flask, request, Numeric, jsonify, String, Integer, Date, Enum
from flask_sqlalchemy import SQLAlchemy
from models.fixed_asset_register import FixedAssetRegister

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sql://fixedassets.db"
db = SQLAlchemy(app)

class fixedassets(db.Model):
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForignKey('Users.id'))
    asset_name = db.Column(String(100), nullable=True)
    asset_type = db.Column(String(100), nullable=True)
    purchase_date = db.Column(Date, nullable=True)
    purchase_price = db.Column(db.Integer, db.ForignKey('Transaction.id'))
    depreciate_rate = db.Column(Numeric(5, 4), nullable=True)
    depreciation_method = db.Column(Enum(('straight_line', 'reducing_balance'), nullable = True))
    useful_life = db.Column(Numeric(5, 4), nullable=True)
    residual_value = db.Column(Numeric(5, 4), nullable=True)
    depreciation_charge = db.Column(Numeric(5, 4), nullable=True)
    asset_status = db.Column(Enum(('active', 'inactive'), nullable=True))
    created_at = db.Column(Date, nullable=True)
    updated_at = db.Column(Date, nullable=True)


@app.route("/fixed_assets", methods=["POST"])
def create_fixed_asset():
    data = request.json
    user_id = data["user_id"]
    fixedasset = fixedassets(
        user_id=user_id,
        asset_name=data["asset_name"],
        asset_type=data["asset_type"],
        purchase_date=data["purchase_date"],
        purchase_price=data["purchase_price"],
        depreciate_rate=data["depreciate_rate"],
        depreciation_method=data["depreciation_method"],
        useful_life=data["useful_life"],
        residual_value=data["residual_value"],
        asset_status=data["asset_status"],
        created_at=data["created_at"],
        updated_at=data["updated_at"],
        )
    db.session.add(fixedasset)
    db.session.commit()
    return jsonify({"message": "Fixed asset created successfully"}), 201

@app.route("/fixed_assets/ <int:user_id>", methods=["GET"])
def get_fixed_assets(user_id):
    fixedassets = fixedassets.query.filterby(user_id=user_id).all()
    return jsonify([fixedassets.to_dict() for fixedassets in fixedassets])

@app.route("/fixed_assets", methods=["POST"])
def get_fixed_asset_register(user_id):
    fixedassets = fixedassets.query.filter_by(user_id=user_id).all()
    register = FixedAssetRegister()
    fa = register.add_asset(fixedassets)
    fadep = register.calculate_depreciation(fa)
    return jsonify([fa, fadep])


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)