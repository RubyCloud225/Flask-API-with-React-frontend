from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_backend.db.database import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data['username']
    company_name = data['companyName']
    country = data['country']
    email = data['email']
    password = data['password']
    confirm_password = data['confirmPassword']

    #Validate the user's input data
    if password != confirm_password:
        return jsonify({'error': 'Passwords do not match'}), 400
    
    #create a new user account
    user = User(username, company_name, country, email, password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User account created successfully'}), 201
