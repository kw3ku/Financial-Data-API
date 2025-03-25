import os

class Config:
    # Database URI for PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:userpass@localhost/financial_data')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'pass1234'
    # TESTING = True  # Add this line
