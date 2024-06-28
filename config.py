import os

class Config:
    # Define the PostgreSQL URI directly
    SQLALCHEMY_DATABASE_URI = 'postgres://ubksl4tqlamln4:p1c21324f05453e39b2141da690c0b6b22f4d87c6f6e3af6a5c16f4fcb87bc1f1@cd5gks8n4kb20g.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d5qaspp2blgbc0'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'uploads/'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Ensure the DATABASE_URL environment variable is set
os.environ['DATABASE_URL'] = Config.SQLALCHEMY_DATABASE_URI
