from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AccountType(Base):
    __tablename__ = 'account_types'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    type = Column(Enum('asset', 'liability', 'equity', 'revenue', 'expenses'))

    def __repr__(self):
        return f"AccountType(id={self.id}, name='{self.name}', description='{self.description}', type='{self.type}')"
    
"""
#Example Use Case

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///accounting.db')  # Replace with your database URL
Session = sessionmaker(bind=engine)
session = Session()

# Create a new AccountType instance
new_account_type = AccountType(name='Accounts Receivable', description='Amounts owed to us', type='asset')

# Add the new account type to the session
session.add(new_account_type)

# Commit the changes to the database
session.commit()

"""