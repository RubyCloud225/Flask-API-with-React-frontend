from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    company_name = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.company_name}', '{self.country}', '{self.email}')"
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

# Create the database tables
db.create_all()

# Example data
user1 = User(username='john Doe', company_name='ABC Inc.', country='USA', email='johndoe@example.com', password='password123')
user2 = User(username='jane Doe', company_name='XYZ Corp.', country='Canada', email='janedoe@example.com', password='password123')

# Add the example data to the database
db.session.add(user1)
db.session.add(user2)

# Commit the changes
db.session.commit()