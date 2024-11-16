import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')  # Use environment variable or fallback to default
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///site.db')  # Use environment variable
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret_key')  # Use environment variable or fallback
